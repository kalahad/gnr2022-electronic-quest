# GNR2022 · Circuit Quest

แผนที่ภารกิจของวิชา **GNR2022 อิเล็กทรอนิกส์พื้นฐาน** คณะวิศวกรรมศาสตร์ มหาวิทยาลัยรามคำแหง ภาคเรียนที่ 1/2569
รวมเกมบทเรียน ห้องทดลองจำลอง และ Final Boss ไว้ในลิงก์เดียว เล่นบนเบราว์เซอร์มือถือได้ทันที

**เข้าเล่น:** https://kalahad.github.io/gnr-electronic/

## แผนที่โซน

| โซน | ชื่อ | เนื้อหา | ไฟล์ | สถานะ |
|---|---|---|---|---|
| S1 · Z1 | RESISTOR CITY | ตัวต้านทานแถบสี | `play/s1-z1-resistor-city.html` | พร้อมเล่น |
| S1 · Z2 | LUMEN STATION | ตัวต้านทานปรับค่า · LDR · วงจรแบ่งแรงดันและ ADC | `play/s1-z2-lumen-station.html` | พร้อมเล่น |
| S1 · Z3 | DEEP CRYSTAL | แถบพลังงาน · การเจือสาร · รอยต่อ PN | `play/s1-z3-deep-crystal.html` | พร้อมเล่น |
| S1 · Z4 | DIODE FORGE | ไดโอด · LED · 7-segment · ซีเนอร์ | `play/s1-z4-diode-forge.html` | พร้อมเล่น |
| S1 · Z5 | STORM HARBOR | วงจรเรียงกระแส · ตัวกรอง · ซีเนอร์ | `play/s1-z5-storm-harbor.html` | พร้อมเล่น |
| S1 · Z6 | NIGHT MELODY (บอส S1) | LDR · ทรานซิสเตอร์สวิตช์ · ระบบเพลงยามค่ำ (ข้อสอบกลางภาคข้อ 72) | `play/s1-z6-night-melody.html` | พร้อมเล่น |
| S2 · Z7–Z10 | BJT ARENA · OP-AMP TOWER · 555 CLOCKWORK · MOSFET × IoT GATE | เนื้อหาหลังสอบกลางภาค | `play/s2-…` | กำลังสร้าง |
| FINAL | FINAL BOSS | จำลองสอบปลายภาค | `boss/final-boss.html` | พร้อมเล่น |

ห้องทดลองจำลอง (Side Quest) อยู่ในโฟลเดอร์ `lab/`: 7-segment (DIGIT FORGE), รูป 3-40 SUN CHIME, 3-44 DUSK GUARD, 3-47 BEAM SENTRY, 3-50 PULSE EYE, LM339 TRIP POINT และ BAR RANGER

ชื่อไฟล์เดิมในโฟลเดอร์หลัก (เช่น `Lab_3_4_sun_chime_light_alarm_3_40.html`) เป็นหน้าส่งต่ออัตโนมัติ ลิงก์และ QR code ที่เคยแจกจึงยังใช้ได้

## ระบบผู้เล่น

- ลงทะเบียนด้วยรหัสนักศึกษา 10 หลัก + ชื่อเล่น (ไม่มีรายชื่อนักศึกษาอยู่ในเว็บ) · ผู้สอนใช้รหัสลับแทนรหัสนักศึกษาได้
- ผลเก็บในเบราว์เซอร์ของผู้เล่น คีย์ `gnr2022_*` ไม่มี backend
- แรงก์ตามดาวรวม: Resistor → Capacitor → Diode → Transistor → Op-Amp → MCU → Circuit Legend
- Posttest 5 ดาวขึ้นไป ได้การ์ดอุปกรณ์และรหัสแสตมป์ ผู้สอนตรวจรหัสได้ที่ปุ่ม "ผู้สอน" บนหน้าแผนที่
- สตรีครายวัน มีโล่กันขาด 1 วันต่อสัปดาห์

## สร้างใหม่หลังแก้เนื้อหา (สำหรับผู้ดูแล)

```bash
tools/build_all.sh                              # สร้างทุกโซนจาก tools/games_src/gN_*.py
python3 tools/qa_headless.py game6_night_melody.html   # ต้องได้ ALL OK
python3 tools/make_answer_key.py <ไฟล์นอก repo>          # เฉลยผู้สอน ห้ามเผยแพร่
python3 tools/dist.py <ไฟล์ gnr-electronic เดิม> <เกมฉบับเดิม> <ปลายทาง>
```

ทุกหน้าย่อให้พอดีจอเดียวอัตโนมัติ (ตรวจด้วย `tools/fit_check.py`) · โซน 2, 3, 5 ดึงเนื้อหา คลังข้อสอบ และห้องทดลองจากเกมฉบับเดิมใน `tools/legacy_src/` ผ่าน `legacy_port.py` (แก้เนื้อหาที่ไฟล์ต้นฉบับนั้น) · ตัวเลือกแรกของแต่ละข้อในคอนฟิกคือคำตอบที่ถูก เอนจินสลับตัวเลือกให้เอง หน้าแผนที่อยู่ที่ `tools/hub/index.html`

## เครดิต

ผศ.ดร.กุลวลัญช์ วรุณสิน · คณะวิศวกรรมศาสตร์ มหาวิทยาลัยรามคำแหง
เอนจิน: CPE2422 IoT Maker Quest v1.00 + NEO ARCADE (สืบทอดจาก GNR1007 Learning Game Series UI v7.0)
