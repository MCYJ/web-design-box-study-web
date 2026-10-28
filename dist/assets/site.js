
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
  document.querySelector('#css').textContent=`.container {
  display: flex;
  flex-flow: row wrap;
  width: ${viewport}px;
  box-sizing: border-box;
  padding: 16px;
  gap: 16px;
}
.card {
  box-sizing: ${border?'border-box':'content-box'};
  flex: 0 0 auto;
  min-width: 0;
  margin: 0;
  width: ${width}px;
  padding: 16px;
  border: 2px solid;
}`;
 }
 document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>select(b.dataset.mode)));
 select('content');
}
