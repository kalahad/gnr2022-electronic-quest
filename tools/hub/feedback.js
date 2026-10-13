/* ================================================================
   GNR2022 Circuit Quest · ปุ่ม "แจ้งปัญหา / ความคิดเห็น"
   ส่งความคิดเห็นและภาพหน้าจอ (ไม่บังคับ) ไปยัง Google Sheets ผ่าน Google Apps Script
   ----------------------------------------------------------------
   ผู้สอน: วาง URL ของ Web app ที่ได้จากการ Deploy Apps Script ไว้ในบรรทัดด้านล่าง
   ================================================================ */
var GNR_FEEDBACK_URL = '';

(function(){
  'use strict';
  if(window.__gnrFb) return; window.__gnrFb = true;
  var D = document;
  var CATS = ['แสดงผลผิด / ล้นจอ', 'เนื้อหาหรือเฉลยผิด', 'โจทย์ยากเกินไป / ไม่ชัดเจน', 'ปุ่มหรือห้องทดลองใช้ไม่ได้', 'ข้อเสนอแนะ / ไอเดียใหม่', 'อื่น ๆ'];
  var img = null;

  function css(){
    var s = D.createElement('style');
    s.textContent =
      '.gfb-btn{font:600 11.5px/1 Kanit,system-ui,sans-serif;cursor:pointer;border:1px solid rgba(255,138,31,.6);background:rgba(255,138,31,.14);color:inherit;border-radius:999px;padding:4px 10px;margin-left:10px;white-space:nowrap}' +
      '.gfb-btn:hover{background:rgba(255,138,31,.28)}' +
      '.gfb-float{position:fixed;left:84px;bottom:10px;z-index:2147483000;padding:7px 12px;font-size:13px;background:rgba(10,10,25,.72);color:#f4f4ff;border-color:rgba(255,255,255,.22);backdrop-filter:blur(8px)}' +
      '.gfb-ov{position:fixed;inset:0;z-index:2147483600;display:none;align-items:center;justify-content:center;background:rgba(0,0,0,.55);padding:12px}' +
      '.gfb-ov.on{display:flex}' +
      '.gfb-box{width:min(460px,100%);max-height:calc(100dvh - 24px);overflow:auto;background:#fff;color:#14181f;border-radius:18px;padding:16px 18px;font:14px/1.5 Kanit,system-ui,sans-serif;box-shadow:0 20px 60px -20px #000}' +
      '.gfb-box h3{margin:0 0 2px;font-size:18px}.gfb-box p.s{margin:0 0 10px;color:#5b6475;font-size:12.5px}' +
      '.gfb-box label{display:block;font-size:12.5px;color:#4b4e72;margin:8px 0 3px}' +
      '.gfb-box select,.gfb-box textarea,.gfb-box input[type=text]{width:100%;box-sizing:border-box;border:1px solid #d5d9e4;border-radius:10px;padding:8px 10px;font:inherit;background:#f8f9fc;color:#14181f}' +
      '.gfb-box textarea{min-height:84px;resize:vertical}' +
      '.gfb-drop{border:1.5px dashed #c5cad8;border-radius:12px;padding:10px;text-align:center;font-size:12.5px;color:#5b6475;cursor:pointer}' +
      '.gfb-drop img{max-width:100%;max-height:140px;border-radius:8px;display:block;margin:0 auto 6px}' +
      '.gfb-row{display:flex;gap:8px;margin-top:12px}.gfb-row button{flex:1;padding:10px;border-radius:12px;border:1px solid #d5d9e4;background:#f3f4fb;font:600 14px Kanit,system-ui,sans-serif;cursor:pointer;color:#14181f}' +
      '.gfb-row .go{background:linear-gradient(100deg,#ff6a1f,#a855f7);color:#fff;border:0}.gfb-row .go:disabled{opacity:.5;cursor:default}' +
      '.gfb-msg{min-height:1.2em;font-size:12.5px;margin-top:6px}.gfb-chk{display:flex;gap:6px;align-items:center;font-size:12.5px;margin-top:8px;color:#4b4e72}';
    D.head.appendChild(s);
  }

  function session(){ try{ return JSON.parse(sessionStorage.getItem('gnr2022_student') || 'null') || {}; }catch(e){ return {}; } }
  function zoneName(){
    var m = location.pathname.match(/([^\/]+)\.html?$/); var f = m ? m[1] : 'index';
    return f === 'index' ? 'แผนที่ภารกิจ' : f;
  }
  function context(){
    var a = D.querySelector('.screen.active'), out = [];
    if(a) out.push('หน้า ' + a.id);
    var sl = D.querySelector('.screen.active .neo-slide.on .neo-slabel'); if(sl) out.push('สไลด์ ' + sl.textContent.trim());
    var qs = D.querySelectorAll('.q, .qtext, #qText, .question'), q = null;
    for(var i = 0; i < qs.length; i++){ if(qs[i].offsetParent !== null && qs[i].textContent.trim()){ q = qs[i]; } }
    if(q) out.push('โจทย์: ' + q.textContent.replace(/\s+/g, ' ').trim().slice(0, 220));
    return out.join(' | ');
  }

  function shrink(file, cb){
    var fr = new FileReader();
    fr.onload = function(){
      var im = new Image();
      im.onload = function(){
        var k = Math.min(1, 1400 / Math.max(im.width, im.height)), c = D.createElement('canvas');
        c.width = Math.round(im.width * k); c.height = Math.round(im.height * k);
        c.getContext('2d').drawImage(im, 0, 0, c.width, c.height);
        cb(c.toDataURL('image/jpeg', 0.8));
      };
      im.src = fr.result;
    };
    fr.readAsDataURL(file);
  }

  function build(){
    css();
    var ov = D.createElement('div'); ov.className = 'gfb-ov'; ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true');
    ov.innerHTML =
      '<div class="gfb-box"><h3>แจ้งปัญหา / ความคิดเห็น</h3>' +
      '<p class="s">ช่วยกันปรับปรุงเกมให้ดีขึ้น ทุกความเห็นส่งถึงอาจารย์โดยตรง</p>' +
      '<label for="gfbCat">เรื่องที่ต้องการแจ้ง</label><select id="gfbCat">' + CATS.map(function(c){ return '<option>' + c + '</option>'; }).join('') + '</select>' +
      '<label for="gfbMsg">รายละเอียด (เช่น ข้อไหน หน้าไหน เกิดอะไรขึ้น)</label><textarea id="gfbMsg" maxlength="1500"></textarea>' +
      '<label>ภาพหน้าจอ (ไม่บังคับ)</label><div class="gfb-drop" id="gfbDrop" tabindex="0">แตะเพื่อเลือกภาพ หรือกด Ctrl+V วางภาพที่แคปไว้<br><small>Windows: กด Win+Shift+S เพื่อแคปหน้าจอ</small></div>' +
      '<input type="file" id="gfbFile" accept="image/*" hidden>' +
      '<label for="gfbNick">ชื่อเล่น (ไม่บังคับ)</label><input type="text" id="gfbNick" maxlength="30">' +
      '<label class="gfb-chk"><input type="checkbox" id="gfbSid"> แนบรหัสนักศึกษา เพื่อให้อาจารย์ติดต่อกลับได้</label>' +
      '<div class="gfb-msg" id="gfbOut"></div>' +
      '<div class="gfb-row"><button type="button" id="gfbClose">ปิด</button><button type="button" class="go" id="gfbSend">ส่งความคิดเห็น</button></div></div>';
    D.body.appendChild(ov);
    var $ = function(id){ return D.getElementById(id); };
    var drop = $('gfbDrop'), file = $('gfbFile'), out = $('gfbOut');
    function setImg(f){
      if(!f || !/^image\//.test(f.type)) return;
      shrink(f, function(u){ img = u; drop.innerHTML = '<img src="' + u + '" alt="ภาพหน้าจอที่แนบ">แตะเพื่อเปลี่ยนภาพ'; });
    }
    drop.onclick = function(){ file.click(); };
    drop.onkeydown = function(e){ if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); file.click(); } };
    file.onchange = function(){ setImg(file.files[0]); };
    ov.addEventListener('paste', function(e){
      var it = (e.clipboardData || {}).items || [];
      for(var i = 0; i < it.length; i++){ if(it[i].type.indexOf('image') === 0){ setImg(it[i].getAsFile()); e.preventDefault(); break; } }
    });
    function close(){ ov.classList.remove('on'); }
    $('gfbClose').onclick = close;
    ov.onclick = function(e){ if(e.target === ov) close(); };
    D.addEventListener('keydown', function(e){ if(e.key === 'Escape' && ov.classList.contains('on')){ e.stopPropagation(); close(); } }, true);
    $('gfbSend').onclick = function(){
      var msg = $('gfbMsg').value.trim();
      if(msg.length < 5){ out.style.color = '#be123c'; out.textContent = 'กรุณาเขียนรายละเอียดอย่างน้อย 1 ประโยค'; return; }
      if(!GNR_FEEDBACK_URL){ out.style.color = '#be123c'; out.textContent = 'ระบบรับความคิดเห็นยังไม่เปิดใช้งาน กรุณาแจ้งอาจารย์ในชั้นเรียน'; return; }
      var last = 0; try{ last = +localStorage.getItem('gnr2022_fb_last') || 0; }catch(e){}
      if(Date.now() - last < 20000){ out.style.color = '#be123c'; out.textContent = 'ส่งได้อีกครั้งในอีกไม่กี่วินาที'; return; }
      var ss = session(), btn = $('gfbSend');
      var payload = {
        zone: zoneName(), category: $('gfbCat').value, message: msg,
        nick: $('gfbNick').value.trim() || ss.nick || '', sid: $('gfbSid').checked ? (ss.sid || '') : '',
        page: location.href.split('#')[0], context: context(),
        viewport: innerWidth + 'x' + innerHeight + ' @' + (window.devicePixelRatio || 1),
        ua: navigator.userAgent, theme: D.documentElement.getAttribute('data-theme') || '',
        image: img ? img.split(',')[1] : ''
      };
      btn.disabled = true; out.style.color = '#4b4e72'; out.textContent = 'กำลังส่ง...';
      fetch(GNR_FEEDBACK_URL, {method: 'POST', mode: 'no-cors', headers: {'Content-Type': 'text/plain;charset=utf-8'}, body: JSON.stringify(payload)})
        .then(function(){
          try{ localStorage.setItem('gnr2022_fb_last', String(Date.now())); }catch(e){}
          out.style.color = '#15803d'; out.textContent = 'ส่งแล้ว ขอบคุณที่ช่วยปรับปรุงเกม';
          $('gfbMsg').value = ''; img = null; drop.innerHTML = 'แตะเพื่อเลือกภาพ หรือกด Ctrl+V วางภาพที่แคปไว้';
          setTimeout(close, 1400);
        })
        .catch(function(){ out.style.color = '#be123c'; out.textContent = 'ส่งไม่สำเร็จ ตรวจสอบอินเทอร์เน็ตแล้วลองใหม่'; })
        .then(function(){ btn.disabled = false; });
    };
    return function(){ out.textContent = ''; var ss = session(); if(ss.nick && !$('gfbNick').value) $('gfbNick').value = ss.nick; ov.classList.add('on'); setTimeout(function(){ $('gfbMsg').focus(); }, 50); };
  }

  function mount(){
    var open = build();
    var b = D.createElement('button'); b.type = 'button'; b.className = 'gfb-btn'; b.textContent = 'แจ้งปัญหา / ความคิดเห็น';
    b.onclick = open;
    var host = D.querySelector('.neo-foot, footer.foot');
    if(host){ host.appendChild(b); }
    else { b.classList.add('gfb-float'); D.body.appendChild(b); }
  }
  /* รอให้แถบท้ายหน้าของเกมถูกสร้างก่อน (NEO สร้างหลังโหลด) */
  if(D.readyState === 'loading') D.addEventListener('DOMContentLoaded', function(){ setTimeout(mount, 300); });
  else setTimeout(mount, 300);
})();
