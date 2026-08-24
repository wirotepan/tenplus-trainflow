---
name: start
description: >
  Orient a fresh session — read the resume note + handoff docs + git state and report
  where the project is and what to do next. Use at the start of a session, or when the user
  says "start", "เริ่มงาน", "ทำต่อ", "อยู่ตรงไหนแล้ว", "resume", "ต่อจากเดิม", "brief me".
---

# /start — เปิด session แล้วรู้ว่าทำอะไรต่อ

เป้าหมาย: อ่านสถานะล่าสุดจากเอกสารกลาง (ที่ `/end` เขียนไว้) + git แล้ว **บอกผู้ใช้ว่าอยู่ตรงไหน /
ทำต่อตรงไหน** ก่อนเริ่มงานจริง. ผู้ใช้ไม่ถนัด terminal — **รันคำสั่งให้เอง**.

## 1. อ่าน context (ตามลำดับ)
- `CLAUDE.md` — โดยเฉพาะส่วน **"📍 มาถึงไหนแล้ว / ทำต่อตรงไหน"** (resume + `⏭️ ถัดไป`),
  **Decision log**, และ **Guardrails** (กติกาที่ห้ามละเมิด).
- `docs/HANDOFF.md` — TL;DR สถานะ, วิธีรัน, บัญชีทดสอบ, กติกา, งานที่ค้าง.
- ถ้ามี `CONTEXT.md` หรือ `docs/adr/` ที่ repo root → อ่านด้วย.
- อย่าเดา — เปิดไฟล์จริงอ่าน. ถ้า resume note อ้างชื่อไฟล์/flag ให้เช็คว่ายังมีอยู่จริงก่อนแนะนำ.

## 2. เช็ค git state
- `git branch --show-current`, `git log --oneline -8`, `git status --short`.
- ถ้ามีงานค้าง (uncommitted / อยู่ feature branch ที่ยังไม่ merge) → ชี้ให้ผู้ใช้เห็น + โยงกับ HANDOFF
  ว่าค้างตรงไหน. เตือนว่ามี `/ship` ไว้ commit+push และ `/end` ไว้เขียน handoff.

## 3. (ถ้าเกี่ยวข้อง) เช็คว่าระบบรันได้
- ดูว่ามีบริการรันอยู่ไหม (เช่น `docker compose ps`) — เฉพาะเมื่อผู้ใช้จะเดโม/ทดสอบ. อย่ารัน build หนัก
  โดยไม่จำเป็น. บอกวิธีรันจาก HANDOFF (`docker compose up --build`, `npm run check`) แทน.

## 4. สรุปให้ผู้ใช้ (สั้น กระชับ)
รายงาน 4 อย่าง:
1. **ตอนนี้อยู่ตรงไหน** — โมดูล/ฟีเจอร์ล่าสุดที่เสร็จ + สถานะ (merged/ค้าง).
2. **ทำต่อตรงไหน** — งานถัดไปจากบรรทัด `⏭️ ถัดไป` + follow-up ที่ค้าง.
3. **กติกาสำคัญที่ต้องระวัง** สำหรับงานถัดไป (เช่น contracts sync, config-driven, tenant isolation).
4. **git**: branch ปัจจุบัน + มีของค้างไหม.

จบด้วยคำถามว่า **"จะเริ่มงานถัดไป (…) หรืออยากทำอย่างอื่น?"** แล้วรอผู้ใช้ยืนยันก่อนลงมือ
(ตาม guardrail SDLC: ทำทีละโมดูล หยุดรอรีวิว — อย่าเผลอเริ่มเฟสถัดไปโดยไม่ถาม).
