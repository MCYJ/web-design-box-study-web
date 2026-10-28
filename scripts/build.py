from pathlib import Path
from html import escape
import json, shutil

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
BASE = '/web-design-box-study-web'
COPY = {
 'ko': {
  'name':'웹디자인 박스 학습', 'eyebrow':'WEB DESIGN · CSS FOUNDATIONS',
  'title':'폭 하나를 바꾸면,\n줄바꿈이 보입니다.',
  'intro':'내용·여백·테두리를 나누어 보고, content-box와 border-box의 차이를 직접 확인하세요.',
  'nav':['처음','학습 노트','지원','개인정보'], 'coming':'앱 심사 준비 중',
  'language':'앱 화면과 수록 문제는 한국어입니다. 이 웹사이트의 영어 안내는 문제 번역을 의미하지 않습니다.',
  'app':'설치 시 한 번 결제하는 오프라인 학습 앱을 준비하고 있습니다. 포함된 학습에 추가 구독이나 일일 문항 제한을 두지 않습니다. 앱 구매·업데이트·외부 링크에는 연결이 필요합니다.',
  'notice':'RushLabs의 독립 학습 자료입니다. 한국산업인력공단·Q-Net 및 시험 운영기관과 제휴하거나 공식 인증받은 서비스가 아닙니다. 공식 시험 재현·실기 대체·합격을 보장하지 않습니다.',
  'demoTitle':'같은 144px, 다른 바깥 폭',
  'demoIntro':'컨테이너 360px · 안쪽 여백 16px · 카드 width 144px · 카드 padding 16px · border 2px · gap 16px',
  'demoScope':'빈 카드 3개, 왼쪽에서 오른쪽으로 배치되는 고정폭 flex 줄바꿈 예제입니다. 작은 화면에서는 그림을 가로로 스크롤해 전체 폭을 확인하세요. 임의 HTML 실행기나 공식 실기 채점기가 아닙니다.',
  'studyTitle':'세 가지 관찰로 시작하기',
  'lessons':[
   ['01','내용 폭과 바깥 폭','content-box에서는 width에 padding과 border를 더합니다. 144 + 2 × 16 + 2 × 2 = 180px입니다. 컨테이너 안쪽 328px에 카드 두 개와 gap 16px는 들어가지 않습니다.','width는 내용의 폭일 수 있습니다. 먼저 box-sizing을 확인하세요.'],
   ['02','border-box의 안쪽 계산','border-box의 width 144px에는 padding과 border가 포함됩니다. 내용 폭은 144 − 32 − 4 = 108px입니다. 바깥 폭은 그대로 144px이므로 두 카드와 gap은 304px입니다.','같은 width 값이어도 내용 폭과 줄 수가 달라집니다.'],
   ['03','정확히 맞는 줄바꿈 경계','컨테이너 368px에서 양쪽 padding 16px를 빼면 336px입니다. border-box 카드 160px 두 개와 gap 16px는 정확히 336px입니다. width를 더 늘리면 다음 줄로 넘어갑니다.','브라우저의 축소 동작을 막은 flex: 0 0 auto 조건입니다. 일반 반응형 레이아웃 전체로 확대해서 해석하지 마세요.']
  ],
  'supportTitle':'학습을 이어갈 수 있도록',
  'supportIntro':'문의에 앱 이름, 기기와 OS, 앱 버전, 문제가 생긴 순서를 적어 주세요. 비밀번호·인증번호·개인 학습 파일은 보내지 마세요.',
  'supportSections':[
   ['오프라인 학습','설치된 앱에 포함된 문제·해설·개념·그림·복습·학습기록은 오프라인 사용을 목표로 검증 중입니다. 구매·재다운로드·업데이트와 외부 페이지는 인터넷 연결이 필요합니다.'],
   ['기록과 삭제','학습기록과 실습 A/B는 기기에 저장합니다. 앱 삭제로 기록이 사라질 수 있습니다. 기기간 자동 동기화나 계정 복구를 제공한다고 안내하지 않습니다.'],
   ['알림','학습 알림은 기기의 권한과 설정에 따릅니다. 앱의 알림 설정과 OS 설정을 함께 확인해 주세요.'],
   ['문항 제보','문항 식별자와 문제가 된 표현을 알려 주세요. 공식 문제를 복제해 보내거나 개인정보를 첨부할 필요는 없습니다.']
  ],
  'privacyTitle':'개인정보와 기기 저장',
  'privacySections':[
   ['이 웹사이트','이 사이트는 정적 안내·학습 페이지입니다. 계정, 문의 폼, 광고 또는 분석 스크립트를 운영하지 않습니다. 예제 조작값은 페이지 안에서만 사용하고 서버로 전송하지 않습니다. GitHub Pages의 제공자가 접속 처리에 필요한 네트워크 정보를 처리할 수 있습니다.'],
   ['앱의 학습 데이터','준비 중인 앱은 포함된 학습 자료와 기기 내 학습기록을 사용합니다. 학습기록·북마크·실습 A/B는 기기에 보관하며 자체 학습 서버나 계정 동기화를 사용하지 않습니다. 스토어 결제와 OS 알림 권한은 해당 플랫폼이 처리합니다.'],
   ['외부 링크와 이메일','공식 규격 문서 또는 이메일 앱으로 이동하면 해당 제공자의 정책이 적용됩니다. 이메일 문의 시 전달한 주소와 문의 내용은 답변을 위해 사용합니다.'],
   ['문의와 변경','운영자 RushLabs · june1012june@gmail.com. 이 안내는 2026년 10월 28일에 작성했습니다. 앱에 새로운 데이터 처리 기능을 추가하면 배포 전에 안내를 갱신합니다.']
  ],
 },
 'en': {
  'name':'Web Design Box Study', 'eyebrow':'WEB DESIGN · CSS FOUNDATIONS',
  'title':'Change one width.\nSee the next line.',
  'intro':'Separate content, padding and borders. Explore how content-box and border-box change a fixed-width layout.',
  'nav':['Home','Study notes','Support','Privacy'], 'coming':'App in review preparation',
  'language':'The app interface and included questions are in Korean. English website guidance does not mean the question bank is translated.',
  'app':'We are preparing a paid-download app for offline study. Included learning has no extra subscription or daily question cap. Purchases, updates and external links require a connection.',
  'notice':'Independent learning material by RushLabs. Not affiliated with or officially certified by HRD Korea, Q-Net or an exam authority. No claim to reproduce an official exam, replace practical assessment or guarantee a pass.',
  'demoTitle':'144px can mean two outer widths',
  'demoIntro':'Container 360px · container padding 16px · card width 144px · card padding 16px · border 2px · gap 16px',
  'demoScope':'Three empty fixed-width cards in a left-to-right wrapping flex row. On narrow screens, scroll the diagram horizontally to inspect its full width. This is a constrained example, not an arbitrary HTML runner or an official practical-exam assessor.',
  'studyTitle':'Start with three observations',
  'lessons':[
   ['01','Content width and outer width','With content-box, padding and border are added to width: 144 + 2 × 16 + 2 × 2 = 180px. Two cards plus a 16px gap do not fit the 328px inner container.','Check box-sizing before treating width as the outer measurement.'],
   ['02','The inside of border-box','A border-box width of 144px includes padding and borders. Content width is 144 − 32 − 4 = 108px. Two 144px outer widths and a 16px gap total 304px.','The same width value can produce a different content width and line count.'],
   ['03','The exact-fit boundary','A 368px container with 16px padding on each side leaves 336px. Two 160px border-box cards plus a 16px gap fit exactly. Increasing the card width moves the next card to a new line.','This example uses flex: 0 0 auto to prevent shrinking. Do not generalize it to every responsive layout.']
  ],
  'supportTitle':'Keep your study moving',
  'supportIntro':'Include the app name, device and OS, app version and steps that caused the issue. Do not send passwords, verification codes or private study files.',
  'supportSections':[
   ['Offline learning','Included questions, explanations, concepts, diagrams, review and study records are being verified for offline use. Purchases, redownloads, updates and external pages need an internet connection.'],
   ['Records and deletion','Study records and A/B examples are stored on the device. Removing the app may remove those records. We do not promise cross-device synchronization or account recovery.'],
   ['Notifications','Study reminders depend on device permissions and settings. Check both in-app and OS notification settings.'],
   ['Report a question','Share the question identifier and the wording you want us to review. There is no need to send copies of official exam papers or personal information.']
  ],
  'privacyTitle':'Privacy and device storage',
  'privacySections':[
   ['This website','This is a static information and study site. It has no account, inquiry form, advertising or analytics script. Example controls stay in the page and are not sent to a server. GitHub Pages may process network information needed to serve the site.'],
   ['App study data','The app in preparation uses included learning material and on-device study records. Study records, bookmarks and A/B examples stay on the device; there is no study backend or account synchronization. Store payments and OS notification permissions are handled by the platform.'],
   ['External links and email','External standards documents and email apps apply their own provider policies. An email address and inquiry sent to support are used to respond to that inquiry.'],
   ['Contact and updates','Operator: RushLabs · june1012june@gmail.com. Written on October 28, 2026. We will update this notice before distributing new data-processing features.']
  ],
 }
}

CSS = '''
:root{color-scheme:light;--ink:#241e39;--paper:#fbf9ff;--purple:#6438ad;--line:#e2daed;--soft:#eee8f7;--gold:#a66b14}*{box-sizing:border-box}body{margin:0;color:var(--ink);background:var(--paper);font-family:system-ui,-apple-system,sans-serif;line-height:1.75;word-break:keep-all;overflow-wrap:anywhere}a{color:var(--purple);text-underline-offset:4px}a:focus-visible,button:focus-visible{outline:3px solid var(--gold);outline-offset:4px}button{font:inherit;cursor:pointer}header,main,footer{max-width:1160px;margin:auto;padding:24px 32px}header{display:flex;gap:24px;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line)}.brand{display:flex;align-items:center;gap:10px;font-weight:750;text-decoration:none;color:var(--ink)}.brand img{width:36px;height:36px;border-radius:10px}nav{display:flex;flex-wrap:wrap;gap:16px;font-size:.9rem}nav a[aria-current=page]{font-weight:750}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(2.6rem,6.3vw,5rem);line-height:1.13;letter-spacing:-.045em;white-space:pre-line;max-width:840px;margin-bottom:24px}h2{font-size:clamp(1.65rem,3.3vw,2.5rem);line-height:1.3;letter-spacing:-.025em}h3{line-height:1.4}.hero{padding:64px 0 40px;display:grid;grid-template-columns:1fr 240px;gap:40px;align-items:center}.hero img{width:100%;border-radius:25%;filter:drop-shadow(0 18px 28px #402c5d20)}.eyebrow{color:var(--purple);font-size:.76rem;letter-spacing:.15em;font-weight:750;margin-bottom:22px}.lead{font-size:1.17rem;max-width:720px;color:#574e68}.badge{display:inline-block;padding:5px 12px;border:1px solid #c4b4dd;border-radius:24px;color:var(--purple);font-size:.84rem;font-weight:700}.note{font-size:.9rem;color:#61586d}.section{padding:42px 0;border-top:1px solid var(--line)}.two{display:grid;grid-template-columns:1fr 1fr;gap:24px}.panel{padding:28px;background:white;border:1px solid var(--line);border-radius:20px;min-width:0}.panel p:last-child{margin-bottom:0}.pillbox{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0}.pillbox button{padding:10px 14px;border:1px solid #c8b8df;border-radius:10px;background:white;color:var(--purple);min-height:44px}.pillbox button[aria-pressed=true]{background:var(--purple);color:white}.canvas-viewport{width:100%;overflow:auto;padding:14px 0}.canvas{width:360px;max-width:none;padding:16px;display:flex;flex-flow:row wrap;gap:16px;background:#f3edf9;outline:1px dashed #b5a3cc;outline-offset:-1px;border-radius:12px;box-sizing:border-box}.example-card{width:144px;padding:16px;border:2px solid #b47c21;min-width:0;margin:0;flex:0 0 auto;height:60px;box-sizing:content-box;background:#e4d8f3}.example-card::after{content:'';display:block;width:100%;height:100%;background:#7a50ad;border-radius:3px}.canvas.border .example-card{box-sizing:border-box;height:96px}.canvas.exact{width:368px}.canvas.exact .example-card{width:160px}#result{font-weight:700;margin-top:16px}pre{font: .83rem/1.6 ui-monospace,monospace;background:#281f3b;color:#f4edff;padding:20px;border-radius:12px;overflow:auto;white-space:pre-wrap;overflow-wrap:anywhere}.lesson{display:grid;grid-template-columns:64px 1fr;gap:20px}.number{font-size:2rem;color:var(--purple);font-weight:800}.hint{padding:14px 18px;border-left:3px solid var(--gold);background:#fbf6e9;font-size:.92rem}article{max-width:850px;padding:48px 0}article h1{font-size:clamp(2.2rem,5vw,3.7rem)}article section{margin-top:32px}footer{font-size:.8rem;color:#6d627b;border-top:1px solid var(--line);padding-top:32px;padding-bottom:40px}.footer-row{display:flex;gap:24px;justify-content:space-between;flex-wrap:wrap}.footer-note{max-width:820px;margin:20px 0 0}.textlink{font-weight:700} @media(max-width:700px){header,main,footer{padding-left:20px;padding-right:20px}header{align-items:flex-start;flex-direction:column;gap:12px}nav{gap:12px}.hero{grid-template-columns:1fr;padding-top:40px;gap:20px}.hero img{width:120px;grid-row:1}.two{grid-template-columns:1fr}.panel{padding:20px}.section{padding:30px 0}.lesson{grid-template-columns:42px 1fr;gap:12px}h1{font-size:2rem}.canvas{max-width:none}.canvas-viewport{padding-bottom:16px}}
'''
JS = '''
const canvas=document.querySelector('.canvas');
if(canvas){
 const locale=document.documentElement.lang;
 const names=locale==='ko'?['바깥 폭','내용 폭','열 / 행']:['Outer width','Content width','columns / rows'];
 function select(mode){
  document.querySelectorAll('[data-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===mode)));
  canvas.className='canvas'+(mode==='content'?'':' border')+(mode==='exact'?' exact':'');
  const width=mode==='exact'?160:144, viewport=mode==='exact'?368:360;
  const border=mode!=='content', outer=border?width:width+36, content=border?width-36:width;
  const cols=Math.max(1,Math.min(3,Math.floor((viewport-32+16)/(outer+16)))),rows=Math.ceil(3/cols);
  document.querySelector('#result').textContent=`${names[0]} ${outer}px · ${names[1]} ${content}px · ${cols} / ${rows} ${names[2]}`;
  document.querySelector('#css').textContent=`.container {\n  display: flex;\n  flex-flow: row wrap;\n  width: ${viewport}px;\n  box-sizing: border-box;\n  padding: 16px;\n  gap: 16px;\n}\n.card {\n  box-sizing: ${border?'border-box':'content-box'};\n  flex: 0 0 auto;\n  min-width: 0;\n  margin: 0;\n  width: ${width}px;\n  padding: 16px;\n  border: 2px solid;\n}`;
 }
 document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>select(b.dataset.mode)));
 select('content');
}
'''

def h(v):return escape(v,quote=True)
def shell(locale, key, title, body):
 c=COPY[locale]; keys=['index','study','support','privacy'];nav=''.join(f'<a href="{BASE}/{locale}/{"" if k=="index" else k+"/"}"'+(' aria-current="page"' if k==key else '')+f'>{h(label)}</a>' for k,label in zip(keys,c['nav']))
 other='en' if locale=='ko' else 'ko';lang='English' if locale=='ko' else '한국어';rel='' if key=='index' else key+'/'
 return f'''<!doctype html><html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{h(title)} · {h(c['name'])}</title><meta name="description" content="{h(c['intro'])}"><link rel="icon" href="{BASE}/assets/icon.svg" type="image/svg+xml"><link rel="stylesheet" href="{BASE}/assets/site.css"><link rel="canonical" href="https://mcyj.github.io{BASE}/{locale}/{rel}"><link rel="alternate" hreflang="{other}" href="https://mcyj.github.io{BASE}/{other}/{rel}"><script src="{BASE}/assets/site.js" defer></script></head><body><header><a class="brand" href="{BASE}/{locale}/"><img src="{BASE}/assets/icon.svg" alt="">{h(c['name'])}</a><nav aria-label="{'주요 메뉴' if locale=='ko' else 'Main navigation'}">{nav}<a href="{BASE}/{other}/{rel}" lang="{other}">{lang}</a></nav></header><main>{body}</main><footer><div class="footer-row"><span>RushLabs · 2026</span><a href="mailto:june1012june@gmail.com">june1012june@gmail.com</a></div><p class="footer-note">{h(c['language'])}</p><p class="footer-note">{h(c['notice'])}</p></footer></body></html>'''

def sections(rows):return ''.join(f'<section><h2>{h(a)}</h2><p>{h(b)}</p></section>' for a,b in rows)

def build():
 DIST.mkdir(exist_ok=True);(DIST/'assets').mkdir(exist_ok=True)
 shutil.copy2(ROOT/'assets/icon.svg',DIST/'assets/icon.svg');(DIST/'assets/site.css').write_text(CSS);(DIST/'assets/site.js').write_text(JS)
 for locale,c in COPY.items():
  labels=['content-box','border-box','정확히 맞추기' if locale=='ko' else 'Exact fit'];buttons=''.join(f'<button type="button" data-mode="{k}" aria-pressed="{str(k=="content").lower()}">{h(label)}</button>' for k,label in zip(['content','border','exact'],labels))
  home=f'''<section class="hero"><div><p class="eyebrow">{c['eyebrow']}</p><h1>{h(c['title'])}</h1><p class="lead">{h(c['intro'])}</p><span class="badge">{h(c['coming'])}</span></div><img src="{BASE}/assets/icon.svg" alt="{'브라우저와 커서 그림' if locale=='ko' else 'Browser and cursor illustration'}"></section><section class="section two"><div><h2>{h(c['demoTitle'])}</h2><p>{h(c['demoIntro'])}</p><div class="pillbox" role="group" aria-label="box-sizing">{buttons}</div><p id="result" role="status" aria-live="polite"></p><p class="note">{h(c['demoScope'])}</p></div><div class="panel"><div class="canvas-viewport"><div class="canvas" aria-hidden="true"><div class="example-card"></div><div class="example-card"></div><div class="example-card"></div></div></div><pre id="css"></pre></div></section><section class="section two"><div><h2>{h(c['studyTitle'])}</h2><p>{h(c['lessons'][0][2])}</p><a class="textlink" href="{BASE}/{locale}/study/">{h(c['nav'][1])} →</a></div><div class="panel"><h3>{h(c['coming'])}</h3><p>{h(c['app'])}</p><p class="note">{h(c['language'])}</p></div></section>'''
  lessons=''.join(f'<section class="section lesson"><span class="number">{n}</span><div><h2>{h(title)}</h2><p>{h(body)}</p><p class="hint">{h(hint)}</p></div></section>' for n,title,body,hint in c['lessons'])
  sources='<section><h2>'+('규격 문서' if locale=='ko' else 'Standards references')+'</h2><p><a href="https://www.w3.org/TR/css-sizing-3/#box-sizing">CSS Sizing · box-sizing</a><br><a href="https://www.w3.org/TR/css-flexbox-1/#line-break">CSS Flexbox · line breaking</a><br><a href="https://www.w3.org/TR/css-align-3/#gaps">CSS Box Alignment · gaps</a></p></section>'
  bodies={'index':home,'study':f'<article><p class="eyebrow">CSS NOTES</p><h1>{h(c["studyTitle"])}</h1>{lessons}{sources}</article>','support':f'<article><h1>{h(c["supportTitle"])}</h1><p class="lead">{h(c["supportIntro"])}</p><a class="textlink" href="mailto:june1012june@gmail.com">june1012june@gmail.com</a>{sections(c["supportSections"])}</article>','privacy':f'<article><h1>{h(c["privacyTitle"])}</h1>{sections(c["privacySections"])}</article>'}
  for key,body in bodies.items():
   out=DIST/locale/('' if key=='index' else key);out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text(shell(locale,key,c['nav'][['index','study','support','privacy'].index(key)],body))
 (DIST/'index.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>웹디자인 박스 학습</title></head><body><p><a href="'+BASE+'/ko/">한국어</a> · <a href="'+BASE+'/en/">English</a></p></body></html>')
 (DIST/'404.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>페이지를 찾을 수 없습니다</title></head><body><h1>페이지를 찾을 수 없습니다 / Page not found</h1><a href="'+BASE+'/ko/">한국어</a> · <a href="'+BASE+'/en/">English</a></body></html>')
 (DIST/'.nojekyll').write_text('')
 print(json.dumps({'pages':len(list(DIST.rglob('*.html'))),'locales':['ko','en'],'appDownloadClaimed':False,'approvedQuestionBankPublished':False}))

if __name__=='__main__':build()
