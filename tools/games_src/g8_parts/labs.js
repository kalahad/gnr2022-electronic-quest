/* ---- LAB 1: LM324 4-level bar ---- */
const CMP_REF=[1.125,2.25,3.375,4.5]; const cmpGot={};
function cmpUpdate(user){
  const v=+$('#cmpV').value, on=CMP_REF.map(r=>v>r), n=on.filter(Boolean).length;
  $('#cmpVt').textContent=v.toFixed(2)+' V';
  $('#cmpBar').innerHTML=CMP_REF.map((r,i)=>'<div><span class="ledlamp'+(on[i]?' on':'')+'"></span><br>LED'+(i+1)+'<br>'+r+' V<br>'+(on[i]?'HIGH':'LOW')+'</div>').join('');
  const st=$('#cmpStatus'); st.className='status-line'+(n?' ok':'');
  st.innerHTML='<b>ติด '+n+' ดวง</b> — ออปแอมป์แต่ละตัวไม่มีป้อนกลับ จึงเปรียบเทียบ: V+ = '+v.toFixed(2)+' V '+(n?'มากกว่าแรงดันอ้างอิงของ LED1'+(n>1?'–LED'+n:'')+' เอาต์พุตจึงเป็น HIGH':'ยังต่ำกว่า 1.125 V ทุกเอาต์พุตเป็น LOW')+(n<4&&n>0?' · LED'+(n+1)+' ยังดับเพราะ V+ < '+CMP_REF[n]+' V':'');
  if(user){ cmpGot[n]=1; markLab('lab1','n'+n,3); }
}
/* ---- LAB 2: gain tuner + scope ---- */
const E12=[1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2];
const GN_R=[]; [1e3,1e4,1e5].forEach(d=>E12.forEach(m=>GN_R.push(Math.round(m*d)))); GN_R.push(1e6);
const GN_T=[{g:-10,t:'inv'},{g:11,t:'non'},{g:-4.7,t:'inv'},{g:2,t:'non'},{g:-2.2,t:'inv'},{g:5.7,t:'non'}];
let gnI=0; const gnOk={}; const VIN=0.5, VSAT=10.5;
function fmtR(r){ return r>=1e6?(r/1e6)+' MΩ':r>=1e3?(r/1e3)+' kΩ':r+' Ω'; }
function gnFill(){ const o=GN_R.map(r=>'<option value="'+r+'">'+fmtR(r)+'</option>').join(''); $('#gnRf').innerHTML=o; $('#gnRi').innerHTML=o; $('#gnRf').value='10000'; $('#gnRi').value='10000'; }
function gnDraw(g){
  const c=$('#gnScope'), x=c.getContext('2d'), W=c.width, H=c.height, cs=getComputedStyle(document.documentElement);
  const col=k=>cs.getPropertyValue(k).trim()||'#fff';
  x.clearRect(0,0,W,H); x.strokeStyle=col('--line'); x.lineWidth=1;
  for(let i=1;i<8;i++){x.beginPath();x.moveTo(i*W/8,0);x.lineTo(i*W/8,H);x.stroke();}
  x.beginPath();x.moveTo(0,H/2);x.lineTo(W,H/2);x.stroke();
  const sc=(H/2-6)/12, rail=v=>H/2-v*sc;
  x.setLineDash([4,4]); x.strokeStyle=col('--red'); [VSAT,-VSAT].forEach(v=>{x.beginPath();x.moveTo(0,rail(v));x.lineTo(W,rail(v));x.stroke();}); x.setLineDash([]);
  const tr=(f,k)=>{x.strokeStyle=col(k);x.lineWidth=2.2;x.beginPath();for(let i=0;i<=W;i+=3){const v=f(i/W*4*Math.PI);i?x.lineTo(i,rail(v)):x.moveTo(i,rail(v));}x.stroke();};
  tr(a=>VIN*Math.sin(a),'--gold'); tr(a=>Math.max(-VSAT,Math.min(VSAT,g*VIN*Math.sin(a))),'--ember');
}
function gnUpdate(user){
  const T=GN_T[gnI], ty=$('#gnType').value, rf=+$('#gnRf').value, ri=+$('#gnRi').value;
  const g=ty==='inv'?-rf/ri:1+rf/ri, vp=Math.abs(g*VIN), clip=vp>VSAT, err=Math.abs(g-T.g)/Math.abs(T.g);
  $('#gnTarget').innerHTML='เป้า Av = '+(T.g>0?'+':'−')+Math.abs(T.g)+'<small>โจทย์ '+(gnI+1)+'/'+GN_T.length+'</small>';
  gnDraw(g);
  $('#gnChips').innerHTML=GN_T.map((t,i)=>'<span class="'+(gnOk[i]?'got':'')+'">'+(t.g>0?'+':'−')+Math.abs(t.g)+'</span>').join('');
  const st=$('#gnStatus'), gs=(g>0?'+':'−')+(Math.round(Math.abs(g)*100)/100);
  if(clip){ st.className='status-line'; st.innerHTML='<b>ชนราง</b> — Av = '+gs+' ต้องการเอาต์พุต '+vp.toFixed(1)+' Vp เกิน ±10.5 V ยอดคลื่นถูกตัด'; if(user) markLab('lab2','clip',3); return; }
  if(err<=0.03){ st.className='status-line ok'; st.innerHTML='<b>ตรงเป้า</b> — '+(ty==='inv'?'−Rf/Ri = −'+fmtR(rf)+' / '+fmtR(ri):'1 + Rf/Ri = 1 + '+fmtR(rf)+' / '+fmtR(ri))+' = '+gs+' · เอาต์พุต '+vp.toFixed(2)+' Vp'+(ty==='inv'?' กลับเฟส':' เฟสเดิม');
    if(user&&!gnOk[gnI]){ gnOk[gnI]=1; markLab('lab2','t'+gnI,3); SFX.play(Object.keys(gnOk).length===GN_T.length?'fanfare':'correct'); $('#gnChips').innerHTML=GN_T.map((t,i)=>'<span class="'+(gnOk[i]?'got':'')+'">'+(t.g>0?'+':'−')+Math.abs(t.g)+'</span>').join(''); } return; }
  st.className='status-line'; st.innerHTML='Av ตอนนี้ = '+gs+(Math.sign(g)!==Math.sign(T.g)?' · เครื่องหมายไม่ตรง ลองเปลี่ยนชนิดวงจร':' · ยังห่างจากเป้า '+(err*100).toFixed(0)+'%');
}
/* ---- LAB 3: op-amp debug bench ---- */
const DB=[
 {m:[['สโคปขาออก','ค้างที่ +10.5 V ตลอด'],['ขา 2 (−)','ไม่เท่ากับขา 3'],['สัญญาณเข้า','0.5 Vp ปกติ'],['ไอซี','ไม่ร้อน']], a:0,
  c:['Rf หลุด วงจรไม่มีป้อนกลับ','Ri มีค่าสูงกว่าที่ออกแบบเล็กน้อย','ต้องเพิ่มสัญญาณเข้าให้มากขึ้น','ไฟเลี้ยงต่อถูกต้องแต่สูงไป'],
  e:'ไม่มีป้อนกลับ ออปแอมป์จึงกลายเป็นตัวเปรียบเทียบ เอาต์พุตชนรางทันที และกฎ V+ = V− ใช้ไม่ได้'},
 {m:[['สโคปขาออก','ยอดคลื่นแบนที่ ±10.5 V'],['สัญญาณเข้า','2 Vp'],['Av ที่ออกแบบ','−10'],['ไอซี','ไม่ร้อน']], a:1,
  c:['Rf หลุด วงจรไม่มีป้อนกลับ','สัญญาณเข้าใหญ่เกิน คลื่นชนราง','ไฟเลี้ยงต่อกลับขั้ว','ไม่ได้ต่อกราวด์ร่วม'],
  e:'2 Vp × 10 = 20 Vp เกินรางไฟ ±10.5 V ยอดคลื่นจึงถูกตัด ลดสัญญาณเข้าหรือลดอัตราขยาย'},
 {m:[['สโคปขาออก','ไม่มีสัญญาณ'],['ขา 7','−12 V'],['ขา 4','+12 V'],['ไอซี','ร้อนจัดทันทีที่เปิดไฟ']], a:2,
  c:['สัญญาณเข้าเล็กเกินไป','Ri ขาดวงจร','ไฟเลี้ยงต่อสลับขั้ว ขา 7 กับ 4','ต้องปรับ Offset Null ก่อน'],
  e:'uA741 ต้องการ +VCC ที่ขา 7 และ −VCC ที่ขา 4 สลับขั้วแล้วไอซีเสียหายทันที ต้องตรวจด้วยมัลติมิเตอร์ก่อนเปิดไฟทุกครั้ง'},
 {m:[['สโคปขาออก','คลื่นลอยขึ้นลง เส้นฐานไม่นิ่ง'],['ค่าที่อ่าน','เปลี่ยนเมื่อขยับสาย'],['สายกราวด์','Function Gen แยกจากบอร์ด'],['ไอซี','ไม่ร้อน']], a:3,
  c:['Rf หลุด วงจรไม่มีป้อนกลับ','สัญญาณเข้าใหญ่เกินไป','ไฟเลี้ยงต่อสลับขั้ว','ไม่ได้ต่อกราวด์ร่วมจุดเดียว'],
  e:'เครื่องกำเนิดสัญญาณ สโคป และแหล่งจ่ายต้องต่อกราวด์ร่วมกันบนโปรโตบอร์ดจุดเดียว มิฉะนั้นแรงดันอ้างอิงลอยและค่าที่วัดไม่นิ่ง'}
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
  else { st.className='status-line'; st.innerHTML='ยังไม่ใช่ — ดูว่าเอาต์พุตค้าง ถูกตัดยอด ไม่มีเลย หรือไม่นิ่ง แล้วไล่หาสาเหตุ'; SFX.play('wrong'); }
}
