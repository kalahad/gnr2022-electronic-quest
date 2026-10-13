#!/bin/sh
# สร้างทุกโซนที่มีคอนฟิก แล้วติดตั้งชั้น UI และ NEO
set -e
cd "$(dirname "$0")/.."
python3 tools/cpe_build.py g1_resistor_city g2_lumen_station g3_deep_crystal g4_diode_forge g5_storm_harbor g6_night_melody
python3 tools/cpe_core/apply_core.py . > /dev/null
python3 tools/neo/apply_neo.py .
