#!/usr/bin/env python3
"""Local attribution and production-output acceptance checks (standard library only)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json,re,tomllib
SITE=Path(__file__).resolve().parents[1]
config=tomllib.loads((SITE/'hugo.toml').read_text());params=config['params']
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.nodes=[];self.head=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  if tag=='head':self.head=True
  self.nodes.append((tag,dict(attrs),self.head))
 def handle_endtag(self,tag):
  if tag=='head':self.head=False
errors=[];count=0;widgets=0;ctas=0
for file in (SITE/'public').rglob('*.html'):
 count+=1;text=file.read_text();p=Page(text);label=str(file.relative_to(SITE/'public'))
 loaders=[a for tag,a,head in p.nodes if tag=='script' and head and a.get('src','').endswith('/pa.umd.production.min.js')]
 if len(loaders)!=1 or loaders[0].get('data-gyg-partner-id')!=params['gygPartnerID']:errors.append(label+': analytics loader')
 for tag,a,head in p.nodes:
  if 'data-gyg-partner-id' in a and a['data-gyg-partner-id']!=params['gygPartnerID']:errors.append(label+': partner mismatch')
  if 'data-gyg-cmp' in a and a['data-gyg-cmp']!=params['gygCampaign']:errors.append(label+': campaign mismatch')
  if tag=='div' and a.get('data-gyg-widget')=='availability':widgets+=1
  if tag=='a' and ('data-gyg-href' in a or 'data-gyg-link' in a):
   ctas+=1;href=a.get('href','')
   if not href.startswith('https://www.getyourguide.com/') or '?' in href:errors.append(label+': missing bare product fallback')
  if tag=='a' and re.search(r'getyourguide\.com',a.get('href','')) and re.search(r'[?&](partner_id|cmp)=',a['href']):errors.append(label+': tracking must be injected at runtime')
  if tag=='img':
   src=a.get('src','')
   if not a.get('alt'):errors.append(label+': image alt missing')
   if src.startswith('/') and not (SITE/'public'/src.lstrip('/')).exists():errors.append(label+': missing image '+src)
  if tag=='link' and a.get('rel')=='canonical' and not a.get('href','').startswith(config['baseURL']):errors.append(label+': canonical domain')
 if re.search(r'livereload|localhost:1313|tokyo|shinjuku|shibuya|1Q7ZSYC|GLBKRID',text,re.I):errors.append(label+': reference/development leak')
 visible=re.sub(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>','',text,flags=re.S)
 visible=re.sub('<[^>]+>',' ',visible)
 if re.search(r'€\s*\d+[.,]\d{2}\b',visible):errors.append(label+': visible fractional price')
for expected in json.loads((SITE/'research/site-inventory.json').read_text()):
 if not (SITE/'public'/expected['path'].strip('/')/'index.html').exists():errors.append('Missing expected page '+expected['path'])
assert count>0,'No production pages found'
js=(SITE/'static/js/main.js').read_text()
if "GYG_PARTNER_ID = '"+params['gygPartnerID']+"'" not in js:errors.append('JavaScript partner mismatch')
if "GYG_CAMPAIGN   = '"+params['gygCampaign']+"'" not in js:errors.append('JavaScript campaign mismatch')
report={'html_pages':count,'availability_widgets':widgets,'static_booking_fallbacks':ctas,'partner_id':params['gygPartnerID'],'campaign':params['gygCampaign'],'errors':errors,'live_domain_checks':'N/A: local build'}
print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
