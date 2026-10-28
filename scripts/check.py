from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json

ROOT=Path(__file__).resolve().parent.parent
DIST=ROOT/'dist';BASE='/web-design-box-study-web'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.lang=None;self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  for key in ['href','src']:
   if key in a:self.links.append(a[key])

pages=list(DIST.rglob('*.html'));assert len(pages)==10
checked=0
for p in pages:
 source=p.read_text();page=Page();page.feed(source);assert page.lang in ['ko','en']
 assert '<meta name="viewport"' in source
 assert not any(v in source.lower() for v in ['googletagmanager','google-analytics','app-store-badge','play.google.com/store/apps','itunes.apple.com/app'])
 if p.parent!=DIST:
  assert page.h1==1 and 'RushLabs' in source and 'june1012june@gmail.com' in source
 for link in page.links:
  url=urlsplit(link)
  if url.scheme or url.netloc:continue
  assert url.path.startswith(BASE+'/'),(p,link)
  local=DIST/url.path[len(BASE)+1:]
  if url.path.endswith('/'):local=local/'index.html'
  assert local.is_file(),(p,link,local)
  checked+=1
assert not any(p.suffix in ['.p8','.mobileprovision','.ipa','.jsonl','.sqlite'] for p in DIST.rglob('*'))
assert '<text' not in (DIST/'assets/icon.svg').read_text().lower()
print(json.dumps({'status':'passed','htmlPages':10,'internalReferencesChecked':checked,'noStoreAvailabilityClaim':True,'noPrivateBankOrSigningFiles':True}))
