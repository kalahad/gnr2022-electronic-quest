/* ---- LAB 1: region meter ---- */
let rmRB=22000; const rmGot={};
function fmtI(a){ return a>=1e-3?(a*1000).toFixed(2)+' mA':(a*1e6).toFixed(1)+' µA'; }
function rmUpdate(user){
  const vin=+$('#rmV').value, beta=100, IB=Math.max(0,(vin-0.7)/rmRB), ICs=(5-0.2)/1000, IC=Math.min(beta*IB,ICs), VCE=IB>0?Math.max(0.2,5-IC*1000):5;
  const k=IB<=0?'cut':(beta*IB<ICs?'act':'sat');
  $('#rmVt').textContent=vin.toFixed(1)+' V';
  $('#rmIB').textContent=fmtI(IB); $('#rmIC').textContent=fmtI(IC); $('#rmVCE').textContent=VCE.toFixed(2)+' V';
  const lamp=$('#rmLed'), lv=IC/ICs; lamp.classList.toggle('on',lv>0.02); lamp.style.setProperty('--lv',lv.toFixed(2));
  document.querySelectorAll('[data-rmrb]').forEach(b=>b.classList.toggle('primary',+b.dataset.rmrb===rmRB));
  const st=$('#rmStatus');
  if(k==='cut'){st.className='status-line';st.innerHTML='<b>คัตออฟ</b> — Vin '+vin.toFixed(1)+' V ยังไม่ถึง 0.7 V ไม่มี IB · VCE ≈ VCC = 5 V';}
  else if(k==='act'){st.className='status-line ok';st.innerHTML='<b>แอกทีฟ</b> — IC = β × IB = '+fmtI(IC)+' ยังน้อยกว่าค่าสูงสุดของวงจร '+fmtI(ICs)+' · VCE = 5 − IC × 1 kΩ = '+VCE.toFixed(2)+' V';}
  else {st.className='status-line ok';st.innerHTML='<b>อิ่มตัว</b> — β × IB = '+fmtI(beta*IB)+' เกินที่วงจรยอมให้ IC ถูกจำกัดที่ (5 − 0.2) / 1 kΩ = 4.80 mA · VCE ≈ 0.2 V';}
  if(user){ rmGot[k]=1; document.querySelectorAll('#rmChips [data-rg]').forEach(s=>s.classList.toggle('got',!!rmGot[s.dataset.rg])); markLab('lab1',k,3);
    if(rmGot.cut&&rmGot.act&&rmGot.sat&&!rmGot.done){rmGot.done=1; st.innerHTML+=' · <b>พบครบ 3 ย่านแล้ว</b>'; SFX.play('fanfare');} }
}
/* ---- LAB 2: relay driver ---- */
let rlRB=0, rlD=true, rlOn=false, rlDead=false;
function rlUpdate(user, ev){
  const st=$('#rlStatus'), lamp=$('#rlLed');
  document.querySelectorAll('[data-rlrb]').forEach(b=>b.classList.toggle('primary',+b.dataset.rlrb===rlRB));
  if(!rlRB){st.className='status-line';st.textContent='เลือก RB ก่อน';return;}
  if(ev==='off' && !rlD && !rlDead){ rlDead=true; SFX.play('wrong'); if(user) markLab('lab2','spike',3); }
  const beta=100, ICs=(5-0.2)/70, IB=rlOn?(3.3-0.7)/rlRB:0, IC=rlDead?0:Math.min(beta*IB,ICs), VCE=rlDead?5:(rlOn?(beta*IB>=ICs?0.2:5-IC*70):5), P=VCE*IC;
  $('#rlIB').textContent=fmtI(IB); $('#rlIC').textContent=fmtI(IC); $('#rlVCE').textContent=VCE.toFixed(2)+' V'; $('#rlP').textContent=(P*1000).toFixed(0)+' mW';
  lamp.classList.remove('on','hot'); let key=null;
  if(rlDead){ lamp.classList.add('hot'); st.className='status-line'; st.innerHTML='<b>ทรานซิสเตอร์เสียแล้ว</b> — ไม่มีไดโอด แรงดันพุ่งจากขดลวดขณะตัดไฟเกิน VCEO 40 V ของ 2N3904 ใส่ไดโอดกันกลับ แล้วกดเลือก RB ใหม่เพื่อเปลี่ยนตัวใหม่'; return; }
  if(!rlOn){
    if(ev==='off'){ st.className='status-line ok'; st.innerHTML='<b>ตัดไฟอย่างปลอดภัย</b> — ไดโอดพากระแสในขดลวดวนกลับ VCE ถูกจำกัดราว 5.7 V'+(rlRB===1200?' · <b>ภารกิจสำเร็จ</b>':''); if(rlRB===1200){key='safe';SFX.play('fanfare');} }
    else { st.className='status-line'; st.innerHTML='GPIO LOW: ทรานซิสเตอร์คัตออฟ รีเลย์ปล่อย'; }
    if(user&&key) markLab('lab2',key,3); return; }
  if(IB>0.01){ lamp.classList.add('on'); st.className='status-line'; st.innerHTML='<b>รีเลย์ติด แต่ขา GPIO ต้องจ่าย '+fmtI(IB)+'</b> เกินระดับที่ควรดึงจากขา GPIO (ออกแบบไม่ควรเกินราว 10 mA) RB ต่ำเกินไป'; key='gpio'; }
  else if(beta*IB>=ICs){ lamp.classList.add('on'); lamp.style.setProperty('--lv','1'); st.className='status-line ok'; st.innerHTML='<b>อิ่มตัว รีเลย์ติดแน่น</b> — β × IB = '+fmtI(beta*IB)+' เผื่อ '+(beta*IB/ICs).toFixed(1)+' เท่าของ 68.6 mA · ทรานซิสเตอร์ร้อนเพียง '+(P*1000).toFixed(0)+' mW ต่อไปลองสั่ง LOW'; key='sat'; }
  else if(IC>0.5*ICs){ lamp.classList.add('hot'); st.className='status-line'; st.innerHTML='<b>แอกทีฟ รีเลย์สั่น ทรานซิสเตอร์ร้อน '+(P*1000).toFixed(0)+' mW</b> — IC ได้แค่ '+fmtI(IC)+' ไม่ถึง 68.6 mA ให้ลด RB'; key='weak'; }
  else { st.className='status-line'; st.innerHTML='<b>IB น้อยเกินไป รีเลย์ไม่ติด</b> — IC = β × IB = '+fmtI(IC)+' เท่านั้น'; key='weak'; }
  if(user&&key) markLab('lab2',key,3);
}
/* ---- LAB 3: debug bench ---- */
const DB=[
 {m:[['GPIO','3.3 V (HIGH)'],['VBE','0.00 V'],['VCE','5.00 V'],['รีเลย์','ไม่ติด']], a:0,
  c:['RB ขาด หรือขาเบสต่อไม่ถึง','ทรานซิสเตอร์อิ่มตัวตามปกติ','ไดโอดกันกลับขาดวงจร','ขดลวดรีเลย์ลัดวงจรภายใน'],
  e:'VBE = 0 V ทั้งที่ GPIO เป็น HIGH แปลว่าไม่มีกระแสเข้าเบส ให้ตรวจ RB และสายเส้นเบสก่อน'},
 {m:[['GPIO','3.3 V (HIGH)'],['VBE','0.70 V'],['VCE','2.10 V'],['รีเลย์','สั่น ทรานซิสเตอร์ร้อน']], a:1,
  c:['IB มากเกินไป ควรเพิ่ม RB','IB น้อยเกินไป ควรลด RB','ไดโอดกันกลับต่อกลับทิศ','ทรานซิสเตอร์เป็นชนิด PNP'],
  e:'VBE ปกติแต่ VCE ค้างกลาง ๆ คือย่านแอกทีฟ กระแสเบสไม่พอให้อิ่มตัว ให้ลด RB (เผื่อ overdrive 2–5 เท่า)'},
 {m:[['GPIO','3.3 V (HIGH)'],['VBE','0.70 V'],['VCE','5.00 V'],['รีเลย์','ไม่ติด']], a:2,
  c:['RB ขาด ไม่มีกระแสเข้าเบส','IB น้อยไปจนอยู่ย่านแอกทีฟ','C–E ไม่นำ: ต่อขาสลับหรือตัวเสีย','วงจรทำงานปกติทุกอย่าง'],
  e:'รอยต่อ B–E นำแล้ว (0.7 V) แต่ C–E ไม่นำเลย มักเกิดจากต่อขาสลับ (เช่น จำขา BC547 สลับกับ 2N3904) หรือทรานซิสเตอร์เสียแบบเปิด'},
 {m:[['ประวัติ','ใช้ได้ 2 วันแล้วเสีย'],['VBE','0.70 V'],['VCE','0.00 V ตลอด'],['ไดโอดคร่อมขดลวด','ไม่มี']], a:3,
  c:['RB มีค่าสูงเกินไป','แหล่งจ่าย 5 V ต่ำเกินไป','GPIO ให้ 3.3 V แทน 5 V','ไม่มีไดโอด แรงดันพุ่งจนเสีย'],
  e:'ทุกครั้งที่ตัดไฟ ขดลวดสร้างแรงดันพุ่งหลายสิบโวลต์ ถ้าไม่มีไดโอดกันกลับ C–E จะพังลัดวงจรในที่สุด (VCE ค้าง 0 V)'}
];
let dbI=0; const dbOk={};
function dbCountTxt(){ $('#dbCount').textContent='เคส '+(dbI+1)+' / '+DB.length+' · วินิจฉัยถูกแล้ว '+Object.keys(dbOk).length+' เคส'; }
function dbRender(){
  const c=DB[dbI];
  $('#dbMeas').innerHTML=c.m.map(x=>'<div><b>'+x[0]+'</b>'+x[1]+'</div>').join('');
  $('#dbPicks').innerHTML=c.c.map((t,i)=>'<button class="pick" data-db="'+i+'">'+t+'</button>').join('');
  dbCountTxt(); const st=$('#dbStatus'); st.className='status-line'; st.textContent='เลือกคำวินิจฉัย';
}
function dbPick(i){
  const c=DB[dbI], st=$('#dbStatus');
  document.querySelectorAll('#dbPicks .pick').forEach((b,j)=>{b.classList.remove('ok','bad'); if(j===i) b.classList.add(i===c.a?'ok':'bad');});
  if(i===c.a){ st.className='status-line ok'; st.innerHTML='<b>ถูกต้อง</b> — '+c.e; dbOk[dbI]=1; markLab('lab3','c'+dbI,3); SFX.play(Object.keys(dbOk).length===DB.length?'fanfare':'correct'); dbCountTxt(); }
  else { st.className='status-line'; st.innerHTML='ยังไม่ใช่ — ดูค่า VBE ก่อน แล้วดู VCE ว่าบอกย่านใด'; SFX.play('wrong'); }
}
