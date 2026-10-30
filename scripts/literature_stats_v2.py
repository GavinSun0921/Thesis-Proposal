#!/usr/bin/env python3
"""Section 1.2: complete cached retrieval, formal-year correction, DOI/title dedup.
Usage: literature_stats_v2.py fetch|analyze|all [T1 T2 T3].
Original retrieval is preserved in raw/; new requests live in raw/v2/.
"""
import calendar, csv, datetime as dt, hashlib, html, json, re, sys, time, unicodedata
import urllib.error, urllib.parse, urllib.request
from collections import Counter
from pathlib import Path
from functools import lru_cache
ROOT = Path(__file__).resolve().parent.parent
STATS = ROOT / 'docs/literature_stats'
RAW = STATS / 'raw/v2'
API = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk'
FIELDS = 'title,abstract,year,venue,publicationVenue,externalIds,publicationDate,publicationTypes'
def norm(s):
    return re.sub(r'[^\w]+', ' ', unicodedata.normalize('NFKC', s or '').casefold()).strip()
def cfg(): return json.loads((STATS / 'queries.json').read_text())
@lru_cache(maxsize=1)
def official_titles():
    path=STATS/'official_titles.json'
    return json.loads(path.read_text()) if path.exists() else {}
@lru_cache(maxsize=None)
def crossref_message(doi):
    if not doi or doi.startswith('10.48550/'):return {}
    path=STATS/'raw/crossref'/(hashlib.sha256(doi.encode()).hexdigest()+'.json')
    return json.loads(path.read_text()).get('message',{}) if path.exists() else {}

def formal_container_venue(container):
    """Match whole canonical venue names, never a conference-name substring.

    Year/ordinal/proceedings wrappers and a trailing known acronym may vary;
    added subject words (ICCVDM, ICRAS, ICMLC, Findings...) must not match.
    """
    value=norm(html.unescape(re.sub(r'<[^>]+>','',container or '')))
    value=re.sub(r'\b(?:19|20)\d{2}\b',' ',value)
    value=re.sub(r'^proceedings(?: of)?(?: the)?\s+','',value)
    value=re.sub(r'\b\d+(?:st|nd|rd|th)\b',' ',value)
    ordinal='first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|twenty|thirtieth|thirty|fortieth|forty|fiftieth|fifty'
    value=re.sub(r'^(?:(?:'+ordinal+r')\s+)+','',value)
    value=re.sub(r'\s+(?:cvpr|iccv|3dv|wacv|icra|iros|icml|iclr|corl|rss|ijcai|aaai|tog|tpami|ijcv|tvcg|cviu|jmlr|tmlr)\s*$','',value)
    value=re.sub(r'\s+',' ',value).strip()
    aliases={
      'CVPR':['ieee cvf conference on computer vision and pattern recognition','ieee conference on computer vision and pattern recognition','conference on computer vision and pattern recognition'],
      'ICCV':['ieee cvf international conference on computer vision','ieee international conference on computer vision','international conference on computer vision'],
      'ECCV':['european conference on computer vision','computer vision eccv'],
      '3DV':['international conference on 3d vision'],
      'WACV':['ieee cvf winter conference on applications of computer vision','ieee winter conference on applications of computer vision','ieee winter applications of computer vision workshops'],
      'SIGGRAPH':['acm transactions on graphics','acm trans graph','acm siggraph conference papers','acm siggraph asia conference papers','siggraph asia conference papers','international conference on computer graphics and interactive techniques'],
      'TPAMI':['ieee transactions on pattern analysis and machine intelligence'],
      'IJCV':['international journal of computer vision'],
      'TVCG':['ieee transactions on visualization and computer graphics'],
      'CVIU':['computer vision and image understanding'],
      'ICLR':['international conference on learning representations'],
      'ICML':['international conference on machine learning'],
      'AAAI':['aaai conference on artificial intelligence','the aaai conference on artificial intelligence'],
      'IJCAI':['international joint conference on artificial intelligence'],
      'JMLR':['journal of machine learning research'],
      'TMLR':['transactions on machine learning research','trans mach learn res'],
      'RSS':['robotics science and systems'],
      'CoRL':['conference on robot learning'],
      'ICRA':['ieee international conference on robotics and automation','ieee international conference on robotics automation'],
      'IROS':['ieee rsj international conference on intelligent robots and systems','ieee rsj international conference on intelligent robots systems'],
      'RA-L':['ieee robotics and automation letters'],
      'T-RO':['ieee transactions on robotics'],
      'IJRR':['the international journal of robotics research','international journal of robotics research','int j robotics res'],
      'Science Robotics':['science robotics'],
      'Nature':['nature'],
      'Nature Machine Intelligence':['nature machine intelligence'],
    }
    if re.fullmatch(r'(?:advances in )?neural information processing systems(?: \d+)?',value):return 'NeurIPS'
    if re.fullmatch(r'robotics science and systems(?: [ivxlcdm]+)?',value):return 'RSS'
    return next((venue for venue,names in aliases.items() if value in names),'')

def date_window(parts):
    """Return bounds and precision; bounds are not invented publication dates."""
    try:
        year=int(parts[0])
        if len(parts)>=3:
            day=dt.date(year,int(parts[1]),int(parts[2]));return day,day,'day'
        if len(parts)==2:
            month=int(parts[1]);return dt.date(year,month,1),dt.date(year,month,calendar.monthrange(year,month)[1]),'month'
        return dt.date(year,1,1),dt.date(year,12,31),'year'
    except (ValueError,TypeError,IndexError):return None

def cutoff_evidence(rec,venue,year,config):
    cutoff=dt.date.fromisoformat(config.get('partial_year_cutoff',config['retrieval_date']))
    blank=dict(status='historical_full_year',date_parts='',precision='',evidence_url='',window_start='',window_end='')
    if year is None:return dict(blank,status='not_applicable_unresolved_formal_year')
    if year<cutoff.year:return blank
    if year>cutoff.year:return dict(blank,status='formal_year_after_cutoff')
    official=official_titles().get(norm(rec.get('title'))) or {}
    observed=official.get('cutoff_observed_on','')
    if official.get('year')==year and observed and dt.date.fromisoformat(observed)<=cutoff:
        return dict(blank,status='official_catalog_observed_by_cutoff',precision='catalog_observation',evidence_url=official.get('url') or official.get('catalog_url',''),window_end=observed)
    doi=((rec.get('externalIds') or {}).get('DOI') or '').casefold()
    message=crossref_message(doi)
    actual={formal_container_venue(s) for s in message.get('container-title',[])}-{''}
    if venue not in actual:return dict(blank,status='cutoff_formal_publication_evidence_missing')
    dates=[]
    for field in ('published-online','published-print','published'):
        parts=message.get(field,{}).get('date-parts',[[]])[0]
        window=date_window(parts)
        if window:dates.append((field,parts,*window))
    # A real online VOR date can precede the issue date. Registration/created,
    # deposited, indexed and S2 publicationDate are deliberately never used.
    before=[x for x in dates if x[3]<=cutoff]
    if before:
        field,parts,low,high,precision=min(before,key=lambda x:(x[3],x[2]))
        return dict(blank,status='crossref_'+field+'_before_cutoff',date_parts=json.dumps(parts),precision=precision,evidence_url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''),window_start=low.isoformat(),window_end=high.isoformat())
    if dates:
        field,parts,low,high,precision=min(dates,key=lambda x:(x[2],x[3]))
        status='publication_after_cutoff' if all(x[2]>cutoff for x in dates) else 'publication_date_interval_crosses_cutoff'
        return dict(blank,status=status,date_parts=json.dumps(parts),precision=precision,evidence_url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''),window_start=low.isoformat(),window_end=high.isoformat())
    return dict(blank,status='cutoff_formal_publication_evidence_missing')
def fetch(selected):
    config = cfg(); RAW.mkdir(parents=True, exist_ok=True)
    jobs=list(config['topics'])
    jobs += [dict(id=t['id']+'-supp',query=t['supplemental_query']) for t in config['topics'] if t.get('supplemental_query')]
    for topic in jobs:
        tid = topic['id']
        if selected and tid not in selected: continue
        token = None; page = 0
        while True:
            page += 1
            params = dict(query=topic['query'], fields=FIELDS, year=config['retrieval_year_range'], sort='paperId:asc')
            if token: params['token'] = token
            url = API + '?' + urllib.parse.urlencode(params)
            path = RAW / f'{tid}-p{page:03}.json'
            if path.exists():
                cached = json.loads(path.read_text())
                if cached.get('request_url') != url: raise RuntimeError('Stale cache: '+str(path))
                data = cached['response']
            else:
                for attempt in range(6):
                    try:
                        req = urllib.request.Request(url, headers={'User-Agent':'ThesisLiteratureAudit/2.0'})
                        with urllib.request.urlopen(req, timeout=50) as response: data = json.load(response)
                        break
                    except (urllib.error.URLError, TimeoutError) as exc:
                        if attempt == 5: raise
                        wait = min(5 * 2**attempt, 40)
                        print(tid, 'page', page, str(exc), 'retry', wait, flush=True); time.sleep(wait)
                path.write_text(json.dumps(dict(request_url=url, retrieved_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(), response=data), ensure_ascii=False))
                time.sleep(2)
            print(tid, 'page', page, 'records', len(data.get('data',[])), 'estimated hits', data.get('total'), flush=True)
            token = data.get('token')
            if not token: break
        (RAW / f'{tid}-meta.json').write_text(json.dumps(dict(query=topic['query'], pages=page, estimated_hits=data.get('total')), indent=2))
def topic_match(rec, tid):
    title=(rec.get('title') or '').casefold()
    abstract=(rec.get('abstract') or '').casefold()
    if tid=='T1':
        # Dynamic range, deformable registration of anatomy, and camera-only
        # localization are not recovery of a visually changing 3-D scene.
        title=re.sub(r'high dynamic range|dynamic range', '', title)
        if re.search(r'cortical|liver|brain|mri|tomograph|\bct\b|prosthes|anatom|fmri',title): return False
        explicit_3d=re.search(r'\b3d\b|3.dimensional|three.dimensional|\b4d\b|volumetric|radiance|gaussian|pointmap',title+' '+abstract)
        nonrigid_scene=re.search(r'non.rigid.{0,16}scenes?',title) and 'reconstruct' in title
        explicit_dynamic_view='dynamic view synthesis' in title
        if not (explicit_3d or nonrigid_scene or explicit_dynamic_view):return False
        if re.search(r'camera (?:re)?localiz|\bgsplatloc\b',title) and 'reconstruct' not in title:return False
        if re.search(r'\bslam\b|\bmapping\b',title) and re.search(r'(?:remov|filter|reject|eliminat).{0,90}dynamic|static (?:map|mapping|background)',abstract):
            if not re.search(r'(?:reconstruct|model|represent).{0,40}dynamic (?:object|region)',abstract):return False
        geometry=r'reconstruct|radiance|gaussian|render|view synth|surface|geometry|geometric|point.?map|3d perception|nerfies|hypernerf'
        dynamic=r'dynamic|deform|non.?rigid|\b4d\b|spacetime|space.time|topolog|\bmotion\b|\btemporal\b|time.varying|continuous 3d|nerfies|hypernerf'
        if re.search(geometry,title) and re.search(dynamic,title): return True
        # For generic method titles, require both a geometric title and an
        # explicit dynamic-scene reconstruction/rendering target in the abstract.
        target=r'dynamic (?:3d |three.dimensional )?(?:scene|object|content)|non.rigid (?:scene|object|reconstruct)|deformable (?:object|scene)|time.varying (?:scene|geometr|surface)|\b4d (?:scene|reconstruct|represent)'
        return bool(re.search(geometry,title) and re.search(target,abstract))
    if tid=='T2':
        if re.search(r'small.world|real.world models?|backdoor|malware|neuron|neuronal|brain circuit|turing pattern',title):return False
        world=r'(?<!small-)(?<!small )(?<!real-)(?<!real )\bworld[- ]models?\b|world simulator|action.conditioned.{0,35}predict'
        context=r'agent|environment|reinforcement|robot|action|planning|control|decision|dynamics|physical'
        if re.search(world,title):return bool(re.search(context,title+' '+abstract))
        if re.search(r'latent dynamics|dynamics model',title):return bool(re.search(r'robot|reinforcement|control|planning|\bagent',title))
        evolution=r'predict|dynamics|state transition|rollout|forecast|future (?:frame|video|observation|state)|imagination|imagined|environment model|benchmark|evaluat.{0,80}world.model|world.model.{0,80}evaluat'
        return bool(re.search(world,abstract) and re.search(context,abstract) and re.search(evolution,abstract))
    task=r'manipulat|grasp|dexter|\bvla\b|vision.language.action|visuomotor|hand.?over|throwing|in.hand'
    learning=r'learn|polic|imitation|diffusion|transformer|neural|reinforcement|skill|pre.?train'
    explicit=r'robotic manipulation|robot manipulation|dexterous manipulation|visuomotor polic|vision.language.action'
    if re.search(r'q.manipulation',title):return False
    if re.search(r'navigation|localization|locomotion',title) and not re.search(task,title):return False
    if re.search(r'q.manipulation|novel gripper|linkage|mechanism design',title) and not re.search(learning,title):return False
    return bool((re.search(task,title) or re.search(explicit,abstract)) and re.search(learning,title+' '+abstract) and re.search(r'robot|robotic|manipulator|visuomotor|vision.language.action|\bvla\b',title+' '+abstract))

def venue_year(rec, config):
    ext = rec.get('externalIds') or {}; key = ext.get('DBLP') or ''
    official=official_titles().get(norm(rec.get('title')))
    if official:return official['venue'],official['year'],'official_proceedings_title'
    pv=rec.get('publicationVenue') or {}
    text=' ; '.join([pv.get('name') or '',rec.get('venue') or '']).casefold()
    doi=(ext.get('DOI') or '').casefold()
    if re.search(r'10\.1109/cvprf|\bfindings\b',doi+' '+text):return '',None,'non_main_findings_track'
    if re.search(r'\bposters?\b|\bdemos?\b|\bcourses?\b|extended abstracts?|\bpanels?\b',text):return '',None,'non_research_paper_type'
    if re.search(r'10\.1109/(?:cvprw|iccvw|eccvw)',doi):return '',None,'workshop'
    if 'workshop' in text and 'applications of computer vision' not in text:return '',None,'workshop'
    parts = key.split('/')
    formal_prefixes={p for v in config['venues'] for p in v['dblp_prefixes']}
    if len(parts)==3 and parts[1]!='corr' and '/'.join(parts[:2]) not in formal_prefixes:
        return '',None,'source_outside_scope'
    # Conference DOIs authenticate their venue and year, even if the index has
    # merged a preprint or attached an inconsistent DBLP record.
    for code,name in [('CVPR','CVPR'),('ICCV','ICCV'),('WACV','WACV'),('ICRA','ICRA'),('IROS','IROS'),('3DV','3DV')]:
        m=re.search(r'10\.1109/'+code.lower()+r'\d*[._](20\d{2})[./]',doi)
        if m:return name,int(m[1]),'formal_conference_doi'
    if len(parts) == 3:
        for venue in config['venues']:
            if '/'.join(parts[:2]) in venue['dblp_prefixes']:
                m = re.search(r'(\d{2})(?:[a-z]+)?$', parts[-1])
                if m: return venue['name'], 2000+int(m[1]) if int(m[1])<70 else 1900+int(m[1]), 'formal_dblp_key'
    if any(x in text for x in ('arxiv','biorxiv','ssrn','workshop')) and 'applications of computer vision' not in text:
        return '',None,'preprint_or_workshop'
    for venue in config['venues']:
        if any(re.search(p,text) for p in venue['patterns']):
            doi=(ext.get('DOI') or '').casefold()
            if doi and not doi.startswith('10.48550/'):
                message=crossref_message(doi)
                if message:
                    year=(message.get('published-print') or message.get('published') or message.get('published-online') or {}).get('date-parts',[[None]])[0][0]
                    actual=next((formal_container_venue(s) for s in message.get('container-title',[]) if formal_container_venue(s)),'')
                    if actual and year:return actual,year,'crossref_formal_metadata'
                    return '',None,'crossref_source_outside_scope'
                return '',None,'formal_year_unresolved'
            return '',None,'formal_year_unresolved'
    return '',None,'source_outside_scope'
def save_csv(name,rows,cols):
    with (STATS/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(rows)
def analyze():
    config=cfg(); years=range(config['year_range'][0],config['year_range'][1]+1)
    included=[];excluded=[];audit={}
    for topic in config['topics']:
        tid=topic['id'];meta=json.loads((RAW/f'{tid}-meta.json').read_text())
        if meta['query']!=topic['query']: raise RuntimeError('Stale query '+tid)
        records={};pages=[RAW/f'{tid}-p{page:03}.json' for page in range(1,meta['pages']+1)]
        if topic.get('supplemental_query'):
            extra=json.loads((RAW/f'{tid}-supp-meta.json').read_text())
            if extra['query']!=topic['supplemental_query']:raise RuntimeError('Stale supplement '+tid)
            pages += [RAW/f'{tid}-supp-p{page:03}.json' for page in range(1,extra['pages']+1)]
        for path in pages:
            data=json.loads(path.read_text())['response']
            for rec in data['data']:records[rec['paperId']]=rec
        rows=[]
        for rec in records.values():
            venue,year,basis=venue_year(rec,config);ext=rec.get('externalIds') or {};doi=(ext.get('DOI') or '').lower()
            if doi.startswith('10.48550/'):doi=''
            official=official_titles().get(norm(rec['title'])) or {}
            row=dict(topic=tid,year=year,index_year=rec.get('year'),title=rec['title'],venue=venue,venue_raw=rec.get('venue') or '',doi=doi,dblp=ext.get('DBLP') or '',year_basis=basis,paper_id=rec['paperId'],s2_url='https://www.semanticscholar.org/paper/'+rec['paperId'],official_url=official.get('url',''))
            evidence=cutoff_evidence(rec,venue,year,config)
            row.update(publication_cutoff_status=evidence['status'],publication_date_parts=evidence['date_parts'],publication_date_precision=evidence['precision'],publication_evidence_url=evidence['evidence_url'],publication_window_start=evidence['window_start'],publication_window_end=evidence['window_end'])
            if not topic_match(rec,tid):
                row['reason']='topic_scope_mismatch';excluded.append(row)
            elif not venue or year not in years:
                row['reason']=basis if not venue else 'outside_formal_year_range';excluded.append(row)
            elif evidence['status'] not in ('historical_full_year','official_catalog_observed_by_cutoff') and not evidence['status'].startswith('crossref_published'):
                row['reason']=evidence['status'];excluded.append(row)
            else:rows.append(row)
        rows.sort(key=lambda r:(r['year'],r['year_basis']!='official_proceedings_title',not bool(r['doi']),r['paper_id']))
        dois=set();titles=set();chosen=[]
        for row in rows:
            title=norm(row['title'])
            if (row['doi'] and row['doi'] in dois) or title in titles:
                row['reason']='duplicate_doi_or_title';excluded.append(row);continue
            if row['doi']:dois.add(row['doi'])
            titles.add(title);chosen.append(row)
        included.extend(chosen)
        audit[tid]=dict(retrieved=len(records),included=len(chosen),excluded_by_reason=dict(Counter(r['reason'] for r in excluded if r['topic']==tid)),year_basis=dict(Counter(r['year_basis'] for r in chosen)),corrected_years=sum(r['year']!=r['index_year'] for r in chosen),partial_year_included=sum(r['year']==config['year_range'][1] for r in chosen),partial_year_evidence=dict(Counter(r['publication_cutoff_status'] for r in chosen if r['year']==config['year_range'][1])))
    cols=['topic','year','index_year','title','venue','doi','dblp','year_basis','paper_id','s2_url','official_url','publication_cutoff_status','publication_date_parts','publication_date_precision','publication_evidence_url','publication_window_start','publication_window_end']
    included.sort(key=lambda r:(r['topic'],r['year'],r['title']))
    save_csv('papers.csv',included,cols);save_csv('excluded.csv',excluded,cols+['venue_raw','reason'])
    yearly={t['id']:Counter(r['year'] for r in included if r['topic']==t['id']) for t in config['topics']}
    save_csv('yearly.csv',[dict(year=y,**{tid:c[y] for tid,c in yearly.items()}) for y in years],['year']+list(yearly))
    result={k:config[k] for k in ('source','source_url','retrieval_date','year_range')}
    result.update(partial_year=config['year_range'][1],partial_year_cutoff=config.get('partial_year_cutoff',config['retrieval_date']),annualized=False,cutoff_policy='Public official catalog observed by cutoff or authentic Crossref publication-date interval ending on or before cutoff; no S2 preprint date, created date, or missing-date imputation.')
    result['topics']=[dict(id=t['id'],name=t['name'],query=t['query'],counts={str(y):yearly[t['id']][y] for y in years},total=sum(yearly[t['id']].values())) for t in config['topics']]
    (STATS/'yearly.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));(STATS/'quality_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),ROOT/'scripts/literature_catalogs.py',STATS/'queries.json',STATS/'papers.csv',STATS/'excluded.csv',STATS/'yearly.json',STATS/'official_titles.json',STATS/'proceedings_sources.json',STATS/'relevance_review.csv',STATS/'cutoff_2026_review.csv',STATS/'README.md'] if p.exists()}
    manifest=dict(retrieval_date=config['retrieval_date'],year_range=config['year_range'],partial_year=result['partial_year'],partial_year_cutoff=result['partial_year_cutoff'],annualized=False,cutoff_applied=True,cutoff_policy=result['cutoff_policy'],script_and_data_sha256=hashes,raw_v2_pages=len(list(RAW.glob('T*-p*.json'))),crossref_records=len(list((STATS/'raw/crossref').glob('*.json'))),official_title_records=len(official_titles()),annual_counts={t['id']:t['counts'] for t in result['topics']},quality_checks=['per-topic formal DOI and normalized-title deduplication','whole-name canonical Crossref source matching','2026 records require independent formal-publication evidence by 2026-10-29','month/year date intervals are retained; cutoff-crossing intervals remain excluded','no annualization and no substitution of preprint/created dates','CSV and yearly counts independently reconcilable'])
    (STATS/'analysis_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(json.dumps(audit,ensure_ascii=False,indent=2));print((STATS/'yearly.csv').read_text())
if __name__=='__main__':
    command=sys.argv[1] if len(sys.argv)>1 else 'all'
    if command in ('fetch','all'):fetch(set(sys.argv[2:]))
    if command in ('analyze','all'):analyze()
