/**
 * GNR2022 Circuit Quest — ตัวรับความคิดเห็นจากปุ่ม "แจ้งปัญหา / ความคิดเห็น"
 * ชื่อไฟล์: GNR2022 เกมบทเรียน · ความคิดเห็นเพื่อพัฒนาเวอร์ชันถัดไป (ฟังก์ชัน setup ตั้งชื่อให้อัตโนมัติ)
 * วิธีใช้: เปิด Google Sheets แผ่นใหม่ → ส่วนขยาย → Apps Script → วางโค้ดนี้ทั้งหมด
 *         → เลือกฟังก์ชัน setup แล้วกด Run (อนุญาตสิทธิ์) → Deploy → New deployment → Web app
 *         (Execute as: Me · Who has access: Anyone) → คัดลอก URL ไปใส่ใน feedback.js
 * รุ่น 2 (20 ต.ค. 2569): เพิ่มกระดานคะแนนรวมห้อง แผ่น "คะแนนรวมห้อง" (doPost type=score, doGet action=board)
 *   อัปเดตโค้ดแล้ว: Deploy → Manage deployments → แก้ไข (ดินสอ) → Version: New version → Deploy  (URL เดิมใช้ต่อได้)
 * ภาพหน้าจอเก็บใน Google Drive ของผู้สอน โฟลเดอร์ "GNR2022 เกมบทเรียน · ภาพหน้าจอจากความคิดเห็น" (ไม่เปิดสาธารณะ)
 */
const BOOK_NAME = 'GNR2022 เกมบทเรียน · ความคิดเห็นเพื่อพัฒนาเวอร์ชันถัดไป';
const SHEET_NAME = 'ความคิดเห็น';
const FOLDER_NAME = 'GNR2022 เกมบทเรียน · ภาพหน้าจอจากความคิดเห็น';
const HEADERS = ['เวลา', 'โซน/หน้า', 'ประเภท', 'รายละเอียด', 'ภาพหน้าจอ', 'ชื่อเล่น', 'รหัสนักศึกษา',
                 'ตำแหน่งในเกม', 'ขนาดจอ', 'โหมดสี', 'ลิงก์หน้า', 'อุปกรณ์', 'สถานะ', 'หมายเหตุผู้สอน'];

function setup() {
  SpreadsheetApp.getActiveSpreadsheet().rename(BOOK_NAME);
  const sh = sheet_();
  sh.setFrozenRows(1);
  sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold').setBackground('#fde7d7');
  const rule = SpreadsheetApp.newDataValidation().requireValueInList(['ใหม่', 'กำลังแก้', 'แก้แล้ว', 'ไม่แก้'], true).build();
  sh.getRange(2, 13, 1000, 1).setDataValidation(rule);
  sh.setColumnWidth(4, 360); sh.setColumnWidth(8, 300);
  folder_();
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    const d = JSON.parse(e.postData.contents || '{}');
    if (d.type === 'score') return score_(d);          // กระดานคะแนนรวมห้อง
    let link = '';
    if (d.image && d.image.length < 7000000) {
      const blob = Utilities.newBlob(Utilities.base64Decode(d.image), 'image/jpeg',
        Utilities.formatDate(new Date(), 'Asia/Bangkok', 'yyyyMMdd_HHmmss') + '_' + clean_(d.zone).slice(0, 30) + '.jpg');
      link = folder_().createFile(blob).getUrl();
    }
    sheet_().appendRow([new Date(), clean_(d.zone), clean_(d.category), clean_(d.message).slice(0, 2000), link,
      clean_(d.nick), clean_(d.sid), clean_(d.context).slice(0, 500), clean_(d.viewport), clean_(d.theme),
      clean_(d.page), clean_(d.ua).slice(0, 200), 'ใหม่', '']);
    return ContentService.createTextOutput('ok');
  } catch (err) {
    return ContentService.createTextOutput('error: ' + err);
  } finally {
    lock.releaseLock();
  }
}

/* กันสูตรแปลกปลอมในเซลล์ (ข้อความที่ขึ้นต้นด้วย = + - @) */
function clean_(v) {
  const s = String(v == null ? '' : v);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) { sh = ss.insertSheet(SHEET_NAME); sh.appendRow(HEADERS); }
  if (sh.getLastRow() === 0) sh.appendRow(HEADERS);
  return sh;
}
function folder_() {
  const it = DriveApp.getFoldersByName(FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(FOLDER_NAME);
}

/* ================= กระดานคะแนนรวมห้อง (รุ่น 2) =================
   เก็บ 1 แถวต่อรหัสนักศึกษา ทุกช่องเก็บค่าสูงสุดที่เคยส่ง (ส่งซ้ำได้ ค่าไม่ลดลง)
   หน้าเว็บแสดงรหัสแบบปิดกลาง เช่น 69••••1234 ไม่ส่งชื่อหรือชื่อเล่น */
const BOARD_SHEET = 'คะแนนรวมห้อง';
const ZK = ['z1','z2','z3','z4','z5','z6','z7','z8','z9','z10'], RK = ['r4','r5','r6'];
const BOARD_HEAD = ['รหัสนักศึกษา', 'ดาวรวม', 'การ์ด (≥5 ดาว)', 'กู้โซนผ่าน'].concat(ZK, RK, ['อัปเดตล่าสุด', 'ส่งแล้ว (ครั้ง)']);

function board_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(BOARD_SHEET);
  if (!sh) {
    sh = ss.insertSheet(BOARD_SHEET); sh.appendRow(BOARD_HEAD); sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, BOARD_HEAD.length).setFontWeight('bold').setBackground('#d7f0fd');
    sh.getRange('A:A').setNumberFormat('@');
  }
  return sh;
}
function int_(v, lo, hi) { v = Math.round(Number(v) || 0); return Math.max(lo, Math.min(hi, v)); }

function score_(d) {
  const sid = String(d.sid || '');
  if (!/^[5-7]\d{9}$/.test(sid)) return ContentService.createTextOutput('bad sid');
  const sh = board_(), last = sh.getLastRow();
  const ids = last > 1 ? sh.getRange(2, 1, last - 1, 1).getValues().map(function (r) { return String(r[0]); }) : [];
  let row = ids.indexOf(sid) + 2, old = null;
  if (row < 2) { row = last + 1; } else { old = sh.getRange(row, 1, 1, BOARD_HEAD.length).getValues()[0]; }
  const st = d.stars || {}, rs = d.rescue || {};
  const z = ZK.map(function (k, i) { return Math.max(int_(st[k], 0, 6), old ? int_(old[4 + i], 0, 6) : 0); });
  const r = RK.map(function (k, i) { return Math.max(int_(rs[k], 0, 12), old ? int_(old[4 + ZK.length + i], 0, 12) : 0); });
  const total = z.reduce(function (a, b) { return a + b; }, 0);
  const cards = z.filter(function (x) { return x >= 5; }).length;
  const saved = r.filter(function (x) { return x >= 10; }).length;
  const n = old ? int_(old[BOARD_HEAD.length - 1], 0, 1e6) + 1 : 1;
  sh.getRange(row, 1, 1, BOARD_HEAD.length).setValues([[sid, total, cards, saved].concat(z, r, [new Date(), n])]);
  return ContentService.createTextOutput('ok');
}

function fnv5_(s) {
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; }
  const A = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; let o = '';
  for (let j = 0; j < 5; j++) { o += A[h % A.length]; h = Math.floor(h / A.length); }
  return o;
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.action !== 'board') return ContentService.createTextOutput('GNR2022 Circuit Quest');
  const sh = board_(), last = sh.getLastRow();
  const rows = last > 1 ? sh.getRange(2, 1, last - 1, 4).getValues() : [];
  const list = rows.filter(function (r) { return /^[5-7]\d{9}$/.test(String(r[0])); }).map(function (r) {
    const sid = String(r[0]);
    return { id: sid.slice(0, 2) + '••••' + sid.slice(-4), h: fnv5_(sid), stars: Number(r[1]) || 0, cards: Number(r[2]) || 0, rescue: Number(r[3]) || 0 };
  }).sort(function (a, b) { return b.stars - a.stars || b.cards - a.cards || b.rescue - a.rescue; });
  return ContentService.createTextOutput(JSON.stringify({ n: list.length, at: new Date().toISOString(), list: list }))
    .setMimeType(ContentService.MimeType.JSON);
}
