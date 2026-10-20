/* ---- LAB 1: pin hunt ---- */
const PQ=[{p:8,q:'ขาไฟเลี้ยง VCC'},{p:1,q:'ขากราวด์'},{p:3,q:'ขาเอาต์พุต'},{p:4,q:'ขารีเซ็ต (ดึงต่ำแล้วหยุดทันที)'},
  {p:5,q:'ขาที่ต่อ C 10 nF ลงกราวด์กันสัญญาณรบกวน'},{p:6,q:'ขาที่ตรวจว่าแรงดัน C ถึง 2/3 VCC'},{p:7,q:'ขาที่คายประจุ C ลงกราวด์'},{p:2,q:'ขาที่ถูกดึงต่ำกว่า 1/3 VCC เพื่อเริ่มนับ'}];
const PNAME={1:'GND',2:'TRIG',3:'OUT',4:'RESET',5:'CONT',6:'THRES',7:'DISCH',8:'VCC'};
let pqOrder=[], pqI=0; const pqOk={};
function pqBuild(){
  let h='<rect x="120" y="18" width="100" height="154" rx="10" fill="rgba(0,0,0,.35)" stroke="currentColor" stroke-width="2" style="color:var(--ember)"/><path d="M155 18 a15 15 0 0 0 30 0" fill="none" stroke="var(--ember)" stroke-width="2"/><text x="170" y="100" text-anchor="middle" style="font-size:20px">555</text>';
  for(let i=0;i<4;i++){ const y=36+i*36;
    h+='<g class="pin" data-pin="'+(i+1)+'"><rect x="64" y="'+(y-10)+'" width="56" height="22" rx="5"/><text x="92" y="'+(y+5)+'" text-anchor="middle">'+(i+1)+'</text></g>';
    h+='<g class="pin" data-pin="'+(8-i)+'"><rect x="220" y="'+(y-10)+'" width="56" height="22" rx="5"/><text x="248" y="'+(y+5)+'" text-anchor="middle">'+(8-i)+'</text></g>'; }
  $('#pqChip').innerHTML=h;
}
function pqAskNext(){ if(!pqOrder.length||pqI>=pqOrder.length){ pqOrder=PQ.slice().sort(()=>Math.random()-.5); pqI=0; }
  $('#pqAsk').innerHTML=pqOrder[pqI].q+'<small>ถูกแล้ว '+Object.keys(pqOk).length+' / 8</small>';
  document.querySelectorAll('#pqChip .pin').forEach(g=>g.classList.remove('ok','bad')); }
function pqPick(n){
  const t=pqOrder[pqI], st=$('#pqStatus'), g=document.querySelector('#pqChip .pin[data-pin="'+n+'"]');
  if(n===t.p){ g.classList.add('ok'); pqOk[n]=1; markLab('lab1','p'+n,3); st.className='status-line ok'; st.innerHTML='<b>ถูกต้อง</b> — ขา '+n+' คือ '+PNAME[n]; SFX.play(Object.keys(pqOk).length===8?'fanfare':'correct');
    pqI++; setTimeout(pqAskNext,900); }
  else { g.classList.add('bad'); st.className='status-line'; st.innerHTML='ขา '+n+' คือ '+PNAME[n]+' ยังไม่ใช่ ลองใหม่'; SFX.play('wrong'); }
}
/* ---- LAB 2: monostable timer ---- */
const MN_C=[1,4.7,10,22,47,100], MN_G=[5,1,11]; let mnI=0, mnRun=null; const mnOk={};
function mnT(){ return 1.1*(+$('#mnR').value)*1e3*(+$('#mnC').value)*1e-6; }
function mnShow(){
  const t=mnT(), g=MN_G[mnI]; $('#mnRt').textContent=$('#mnR').value+' kΩ';
  $('#mnGoal').innerHTML='ภารกิจ: '+g+' วินาที<small>'+(mnI+1)+'/'+MN_G.length+'</small>'; $('#mnT').innerHTML='t = '+t.toFixed(2)+'<small>s</small>';
  $('#mnChips').innerHTML=MN_G.map((x,i)=>'<span class="'+(mnOk[i]?'got':'')+'">'+x+' s</span>').join('');
  const st=$('#mnStatus'); st.className='status-line'; st.innerHTML='t = 1.1 × '+$('#mnR').value+' kΩ × '+$('#mnC').value+' µF = <b>'+t.toFixed(2)+' s</b>'+(Math.abs(t-g)/g<=0.05?' · ตรงภารกิจแล้ว กด TRIG เพื่อยืนยัน':' · เป้า '+g+' s');
}
function mnTrig(){
  if(mnRun) return; const t=mnT(), g=MN_G[mnI], ok=Math.abs(t-g)/g<=0.05, k=t>20?t/20:1, dur=t/k*1000, t0=performance.now(), st=$('#mnStatus'), led=$('#mnLed');
  led.classList.add('on'); SFX.play('select');
  st.className='status-line'; st.innerHTML='ขา 2 ต่ำกว่า 1/3 VCC → OUT = HIGH · C ชาร์จผ่าน R'+(k>1?' (เร่งเวลา ×'+k.toFixed(1)+')':'');
  mnRun=setInterval(()=>{ const x=Math.min(1,(performance.now()-t0)/dur), vc=1-Math.exp(-x*1.0986);
    $('#mnCap').style.width=(vc*100)+'%'; $('#mnT').innerHTML='เหลือ '+Math.max(0,t*(1-x)).toFixed(1)+'<small>s</small>';
    if(x>=1){ clearInterval(mnRun); mnRun=null; led.classList.remove('on'); setTimeout(()=>{$('#mnCap').style.width='0';},400);
      if(ok){ st.className='status-line ok'; st.innerHTML='<b>ภารกิจสำเร็จ</b> — C ถึง 2/3 VCC ที่ t = 1.1RC = '+t.toFixed(2)+' s → OUT = LOW ขา 7 คายประจุ C';
        if(!mnOk[mnI]){ mnOk[mnI]=1; markLab('lab2','g'+mnI,3); SFX.play(Object.keys(mnOk).length===MN_G.length?'fanfare':'correct'); } }
      else { st.className='status-line'; st.innerHTML='C ถึง 2/3 VCC แล้ว ไฟดับที่ '+t.toFixed(2)+' s แต่ภารกิจต้องการ '+g+' s ปรับ R หรือ C แล้วลองใหม่'; markLab('lab2','try',1); }
      $('#mnChips').innerHTML=MN_G.map((x,i)=>'<span class="'+(mnOk[i]?'got':'')+'">'+x+' s</span>').join(''); }
  },50);
}
/* ---- LAB 3: BPM astable ---- */
const BP_RA=[1,4.7,10], BP_C=[1,4.7,10], BP_G=[60,120,150]; let bpI=0, bpTimer=null, bpSound=false; const bpOk={};
function bpCalc(){ const ra=+$('#bpRA').value*1e3, rb=+$('#bpRB').value*1e3, c=+$('#bpC').value*1e-6;
  return {f:1.44/((ra+2*rb)*c), tH:0.693*(ra+rb)*c, tL:0.693*rb*c, d:(ra+rb)/(ra+2*rb)}; }
function bpBlink(){ clearTimeout(bpTimer); const r=bpCalc(), led=$('#bpLed');
  if(r.f>15){ led.classList.add('on'); led.style.opacity='.6'; return; } led.style.opacity='1';
  const on=()=>{ led.classList.add('on'); if(bpSound) SFX.play('select'); bpTimer=setTimeout(off,r.tH*1000); }, off=()=>{ led.classList.remove('on'); bpTimer=setTimeout(on,r.tL*1000); }; on(); }
function bpUpdate(user){
  const r=bpCalc(), bpm=r.f*60, g=BP_G[bpI], err=Math.abs(bpm-g)/g;
  $('#bpRBt').textContent=$('#bpRB').value+' kΩ'; $('#bpGoal').innerHTML='เป้า '+g+' BPM<small>เพลง '+(bpI+1)+'/'+BP_G.length+'</small>';
  $('#bpF').textContent=r.f.toFixed(2)+' Hz'; $('#bpB').textContent=bpm.toFixed(1); $('#bpD').textContent=(r.d*100).toFixed(1)+'%';
  $('#bpHL').textContent=(r.tH*1000).toFixed(0)+' / '+(r.tL*1000).toFixed(0)+' ms';
  const st=$('#bpStatus');
  if(err<=0.03){ st.className='status-line ok'; st.innerHTML='<b>ตรงจังหวะ</b> — f = 1.44 / ((RA + 2RB) × C) = '+r.f.toFixed(2)+' Hz = '+bpm.toFixed(1)+' BPM';
    if(user&&!bpOk[bpI]){ bpOk[bpI]=1; markLab('lab3','b'+bpI,3); SFX.play(Object.keys(bpOk).length===BP_G.length?'fanfare':'correct'); } }
  else { st.className='status-line'; st.innerHTML=(bpm>g?'เร็วไป':'ช้าไป')+' '+(err*100).toFixed(0)+'% — '+(bpm>g?'เพิ่ม RB หรือ C':'ลด RB หรือ C')+(r.f>15?' (ตอนนี้กะพริบเร็วเกินตาเห็น)':''); }
  $('#bpChips').innerHTML=BP_G.map((x,i)=>'<span class="'+(bpOk[i]?'got':'')+'">'+x+' BPM</span>').join('');
  bpBlink();
}
