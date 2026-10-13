/**
 * GNR2022 Circuit Quest — ตัวรับความคิดเห็นจากปุ่ม "แจ้งปัญหา / ความคิดเห็น"
 * ชื่อไฟล์: GNR2022 เกมบทเรียน · ความคิดเห็นเพื่อพัฒนาเวอร์ชันถัดไป (ฟังก์ชัน setup ตั้งชื่อให้อัตโนมัติ)
 * วิธีใช้: เปิด Google Sheets แผ่นใหม่ → ส่วนขยาย → Apps Script → วางโค้ดนี้ทั้งหมด
 *         → เลือกฟังก์ชัน setup แล้วกด Run (อนุญาตสิทธิ์) → Deploy → New deployment → Web app
 *         (Execute as: Me · Who has access: Anyone) → คัดลอก URL ไปใส่ใน feedback.js
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
