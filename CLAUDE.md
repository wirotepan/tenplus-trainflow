# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **อ่านไฟล์นี้ก่อนแตะโค้ดทุกครั้ง** — ทั้งคนและ AI agent ทุกตัว. มันคือ "ตัวกันหลง context":
> กติกา, สิ่งที่ตัดสินใจไปแล้ว (decision log), และ contract กลางที่ห้ามละเมิด อยู่ที่นี่.

## 📍 มาถึงไหนแล้ว / ทำต่อตรงไหน (resume here)

อัปเดตล่าสุด: **2026-08-25 (เอกสาร + UI เสร็จ รอลูกค้ายืนยันและตอบคำถาม 🔴 — ยังไม่มีโค้ด)**

- ✅ ตั้งชื่อระบบ **TrainFlow** + สรุป concept/จุดขาย/โมดูลหลัก (ดู "What is being built")
- ✅ ได้ **ผังงาน end-to-end 16 ขั้น** จากลูกค้า (แชท 24 ส.ค.) — ถอดลงตาราง "16 ขั้นตามผังงานจริง" แล้ว
  ต้นฉบับ: [`docs/spec/flow-end-to-end.jpg`](docs/spec/flow-end-to-end.jpg)
- ✅ ตัดสินใจใช้ stack เดียวกับ `dcs-tms` (monorepo NestJS + React + Prisma/Postgres)
- ✅ ยก `.claude/` (skills `/start` `/ship` `/end` `/acceptance` `/acceptance-check` + subagents) มาจาก `dcs-tms`
- ✅ **บทเรียนจาก DCS-TMS** → [`docs/00-lessons-from-dcs-tms.md`](docs/00-lessons-from-dcs-tms.md)
  (requirement ตรงแค่ 45–50% หลังเขียนไป 7 โมดูล · cardinality ผิด = รื้อทั้งระบบ · สายข้อมูลขาดเงียบ ๆ)
- ✅ **เฟส 1 requirements** → [`docs/01-requirements.md`](docs/01-requirements.md) (SRS ย่อ + FR A–L + NFR + คำถามเปิด)
- ✅ **เฟส 2 system design** → [`docs/02-system-design.md`](docs/02-system-design.md)
  (ออกครบทั้ง 16 ขั้นในรอบเดียว: ER · **สายข้อมูลข้ามหน้าจอ §3** · state machine · BR-01..20 · API · exception · multi-tenant)
- ✅ git repo + remote `git@github.com:wirotepan/tenplus-trainflow.git`
- ✅ **UI/UX (ลูกค้าเลือกแล้ว รอบที่ 3)** — ทิศทาง **"กระดาษสถาบัน"** · design system ล็อกที่
  `apps/web/src/theme.css` · ต้นแบบ 6 หน้า `docs/design/*.dc.html` (seed ใหม่ได้ด้วย skill `design`)
  · เหตุผลเบื้องหลัง `docs/spec/ux-research-2026.md` — สองรอบแรกถูกปฏิเสธเพราะตัวอักษร 79% เล็กกว่า 13px
  และ line-height 1.5 (อักษรไทยต้องการ 1.7)
- ✅ **ต้นแบบครบ 16 หน้า** (2026-08-25) แบ่ง 4 กลุ่มบน canvas: เริ่มงาน · จัดงานและวิทยากร ·
  ผลการอบรม · การเงินและระบบ. สร้างด้วย `docs/design/_scaffold.py` ซึ่งดึง helmet + แถบเมนู
  จาก `Jobs.dc.html` (หน้าที่อนุมัติแล้ว) → **ทุกหน้าใช้ชุดเดียวกันเสมอ แก้ที่เดียว**
  · แก้หน้าไหนให้แก้ที่ `docs/design/bodies/<ชื่อ>.py` แล้วรัน `python3 _scaffold.py`
- ⬜ ยังไม่มี: scaffold monorepo, contract files (`openapi.yaml`, `prisma/schema.prisma`, shared-types)
- 📋 **handoff เต็ม (สถานะ · วิธีทำต่อ · ของที่ต้องแก้ก่อนใช้): [`docs/HANDOFF.md`](docs/HANDOFF.md)** — อ่านก่อนเริ่ม
- ⏭️ **ถัดไป:** (1) ลูกค้ายืนยันต้นแบบ 16 หน้า → (2) **ตอบคำถาม 🔴 Q1–Q4** (`01-requirements.md` §7)
  → (3) เริ่ม **M0** (monorepo + contract 3 ไฟล์ + CI + `npm run check`).
  **ห้ามเริ่ม migration แรกก่อนได้คำตอบ Q1–Q4** เพราะกระทบ cardinality และฟิลด์ข้อมูลส่วนบุคคล (บทเรียน L2)

## What is being built

**TrainFlow** — ระบบบริหารงานฝึกอบรมแบบครบวงจร (**Training Business Management** ไม่ใช่แค่ LMS)
สำหรับบริษัทที่รับจัดอบรมให้ลูกค้าองค์กร.

> **Concept: "One Training, One Flow, One Platform"** — บริหารทุกกระบวนการตั้งแต่รับงานจนออกวุฒิบัตร
> และปิดโครงการ ในระบบเดียว. จุดขาย: **ลดงานซ้ำ ลด Excel ลดเอกสาร ลดการส่งข้อมูลหลายช่องทาง**
> และเชื่อม **Admin – ลูกค้า – วิทยากร – ผู้เข้าอบรม** เข้าหากัน.
>
> *"จากงานอบรมที่ต้องใช้ Excel, Google Form, LINE, แบบทดสอบ, Certificate และ Report หลายระบบ —
> รวมให้จบใน Platform เดียว"* · EN: *TrainFlow — From Booking to Certificate.*

**เส้นทางข้อมูลหลัก (end-to-end training flow)** — ทุกฟีเจอร์ต้องอธิบายได้ว่าอยู่ตรงไหนของเส้นนี้:

```
รับงาน → เสนอราคา → Job Created → จองวิทยากร ⇄ (ไม่พร้อม) → Trainer Confirm → แจ้งงาน+Location
  → ลงทะเบียนผู้เข้าอบรม → Check-in (QR เช้า/บ่าย) → Pre-test → ดำเนินการอบรม → Post-test ⇄ (Retest)
  → ตรวจเงื่อนไขผ่าน → Certificate → ประเมินความพึงพอใจ → รูปเล่มรายงาน → ปิดงาน
                                                          ↘ Finance & Dashboard (ผูกกับ Job No. ทุกงาน)
```

**16 ขั้นตามผังงานจริงของลูกค้า** — คอลัมน์ "ผลลัพธ์/เอกสาร" คือ *ปลายทางของข้อมูล* ที่ guardrail
"data spine first" บังคับให้ตอบได้ก่อนเขียนโค้ด (ฟิลด์ที่ไม่ไปโผล่คอลัมน์นี้ = ไม่เพิ่ม):

| # | ขั้นตอน | สาระสำคัญ | ผลลัพธ์ / เอกสาร |
|---|---|---|---|
| 0 | **Master Data** | หลักสูตร (~10) · ทะเบียนวิทยากร (~30) · **Matrix วิทยากร×หลักสูตรที่สอนได้** | — |
| 1 | สร้างงาน / รับความต้องการ | **Public** (สร้างตารางอบรม เปิดรับสมัคร) หรือ **In-house** (รับ requirement: หลักสูตร/วัน/จำนวน/สถานที่) | ใบคำขอจัดอบรม |
| 2 | เสนอราคา | จัดทำใบเสนอราคาส่งลูกค้า → รอลูกค้ายืนยัน | Quotation |
| 3 | **ยืนยันจัดงาน (Job Created)** | ลูกค้ายืนยัน → สร้าง **Job No.** + รายละเอียดเบื้องต้น | Job No., รายละเอียดงาน |
| 4 | จองวิทยากร | ค้นหาจาก **Matrix** + เช็ค **Calendar** → จอง. **ไม่พร้อม → วนกลับหาคนใหม่** | ใบจองวิทยากร (Tentative), Calendar ล็อกวัน |
| 5 | วิทยากรยืนยันงาน | trainer ตรวจรายละเอียด → กด Confirm | Trainer Confirmation, ล็อกงานสมบูรณ์ |
| 6 | แจ้งรายละเอียด + Location | วัน/เวลา/สถานที่/แผนที่ · ผู้ประสานงาน+เบอร์ · เอกสาร/อุปกรณ์ | ใบมอบหมายงานวิทยากร |
| 7 | ลงทะเบียนผู้เข้าอบรม | นำเข้ารายชื่อ หรือ ลงทะเบียนออนไลน์ + ส่งข้อมูลให้ผู้เข้าอบรม | รายชื่อผู้เข้าอบรม |
| 8 | **Check-in (QR)** | สแกน QR **รอบเช้า + รอบบ่าย** บันทึกเวลาเข้า | Attendance เช้า–บ่าย, ชั่วโมงเข้าอบรม |
| 9 | Pre-test | ผู้เข้าอบรมทำแบบทดสอบก่อนเรียน ระบบตรวจอัตโนมัติ | คะแนน Pre-test |
| 10 | ดำเนินการอบรม | บันทึกเวลาเริ่ม–สิ้นสุด, ชั่วโมงจริง + **upload รูปกิจกรรม/เอกสารบรรยาย** | ชั่วโมงอบรมจริง, ไฟล์ประกอบ |
| 11 | Post-test | ตรวจอัตโนมัติ. **ไม่ผ่าน → Retest (สอบใหม่) วนกลับ** | คะแนน Post-test, ผลผ่านเกณฑ์ |
| 12 | **ตรวจเงื่อนไขการผ่าน** | Attendance ครบเกณฑ์ **และ** Post-test ผ่านเกณฑ์ → `TRAINING COMPLETED` | สถานะผ่านการอบรม |
| 13 | **ออกวุฒิบัตรรายบุคคล** | generate อัตโนมัติ + เลขที่วุฒิบัตร + **QR Code** + ผู้เข้าอบรมดาวน์โหลดเอง | วุฒิบัตร (PDF), เลขที่วุฒิบัตร |
| 14 | ประเมินความพึงพอใจ | ผู้เข้าอบรมประเมิน: เนื้อหา · วิทยากร · การจัดอบรม · สถานที่ | ผลประเมิน, คะแนนความพึงพอใจ |
| 15 | **รูปเล่มรายงานผลการอบรม** | ข้อมูลโครงการ · หลักสูตร · รายชื่อ · Attendance · Pre/Post · วิเคราะห์ผล · ภาพกิจกรรม · ข้อเสนอแนะ | รายงานผลการอบรม (PDF) |
| 16 | ปิดงาน | ตรวจเอกสารครบ → ปิดงาน → **สรุปค่าใช้จ่าย/รายได้** | สถานะ `Closed`, สรุปงาน |
| ⤷ | **Dashboard & Report** | ภาพรวม · รายได้/จำนวนงาน/จำนวนผู้เข้าอบรม · ผลประเมิน/**ประสิทธิภาพวิทยากร** | — |

**จุดที่เป็น loop (ห้ามทำเป็นเส้นตรง):** ขั้น 4 วิทยากรไม่พร้อม → หาใหม่ · ขั้น 11 ไม่ผ่าน → Retest.
**Master data ที่ต้องมีตั้งแต่ M1:** หลักสูตร (รายละเอียด · **ระยะเวลา 3/6/12/21 ชม. ตามกฎหมาย** ·
ชุด Pre/Post test · เกณฑ์ผ่าน · เทมเพลตวุฒิบัตร) · วิทยากร (คุณวุฒิ/ประสบการณ์ · **ค่าใช้จ่าย/rate** · สถานะ) ·
**Matrix วิทยากร×หลักสูตร** · ลูกค้า/บริษัท · สถานที่ (Location) · แบบฟอร์ม/เอกสาร · **หมวดค่าใช้จ่าย** · ผู้ใช้งาน.

**3 อย่างที่ทำให้ต่างจาก LMS ทั่วไป — ห้ามลดทอน (นี่คือเหตุผลที่ระบบนี้มีอยู่):**

1. **Trainer Booking Engine** — ระบบรู้ว่า *ใครสอนหลักสูตรอะไรได้ + วันไหนว่าง*.
   เลือกหลักสูตร + วันที่ → แสดงเฉพาะ trainer ที่ **Qualified และ Available** → กด **Tentative → Confirm**.
   ต้องกันจองซ้ำ (double-booking) ที่ระดับข้อมูล ไม่ใช่แค่เตือนบนจอ.
2. **Certificate Automation** — ไม่ใช่แอดมินนั่งทำทีละคน. ระบบตรวจ **Attendance + Post-test + เงื่อนไขหลักสูตร**
   → PASS → generate วุฒิบัตร → **Certificate No.** → **QR verify** อัตโนมัติ.
3. **One-click Training Report** ⭐ (killer feature) — จบงานแล้วกดปุ่มเดียวได้ **รูปเล่ม PDF** ส่งลูกค้าทันที
   จากข้อมูลที่มีอยู่แล้ว (รายชื่อ, attendance, คะแนน pre/post, evaluation, ภาพกิจกรรม, certificate).

**โมดูล/ความสามารถที่ต้องมี:** Smart Training Calendar (Public / In-house / Trainer schedule ในปฏิทินเดียว) ·
Trainer Job Notification (วัน เวลา ลูกค้า contact location) · QR Attendance (เช้า–บ่าย) · Pre/Post Test
ตรวจอัตโนมัติ · Certificate Verification · Training Analytics (attendance, pre/post, pass rate, evaluation) ·
Auto Training Report · Cloud-based ใช้ได้ทั้งมือถือ/คอม · **Scalable** เริ่มจากบริษัทเดียว → SaaS หลายบริษัท.

### Finance & Profitability (ทำให้เป็น Training *Business* Management)

ผูกการเงินกับ **Training Job No.** ทุกงาน (เช่น `TR-2026-00125`) — ผู้บริหารต้องเห็นว่า *งานไหนทำเงิน
งานไหนต้นทุนสูง กำไรอยู่ตรงไหน* ไม่ใช่แค่ "เดือนนี้จัดกี่งาน". โครงสร้างต่อ 1 งานอบรม:

| รายการ | ตัวอย่าง (บาท) |
|---|---:|
| ราคาขายหลักสูตร | 45,000 |
| ส่วนลด | -3,000 |
| **รายได้สุทธิ (Revenue)** | **42,000** |
| ค่าวิทยากร | 12,000 |
| ค่าเดินทางวิทยากร | 2,000 |
| ค่าที่พัก | 1,500 |
| ค่าอาหาร/เบรก | 4,800 |
| ค่าเอกสาร | 1,200 |
| ค่าอุปกรณ์ | 1,000 |
| ค่าสถานที่ | 2,000 |
| ค่าใช้จ่ายอื่น | 500 |
| **ต้นทุนรวม** | **25,000** |
| **กำไรขั้นต้น** | **17,000** |
| **Gross Margin** | **40.5%** |

หมวดค่าใช้จ่ายต้องเป็น **master ที่แก้ผ่านหน้าจอได้** (เพิ่มหมวดใหม่ได้โดยไม่แก้โค้ด) — ห้าม hard-code 9 หมวดนี้.

## Source-of-truth contract files (ห้ามแก้แบบไม่ sync)

ระบบใหญ่ทำให้ agent หลง context ได้ง่าย — ป้องกันด้วยการเก็บ contract ไว้ใน **ไฟล์ ไม่ใช่ความจำ agent**.
สามไฟล์นี้ต้องตรงกันเสมอ; แก้ที่หนึ่งต้องแก้ให้ครบทั้งสาม:

| ไฟล์ | เป็น source of truth ของ |
|---|---|
| `openapi.yaml` | สัญญา API — endpoint, request/response, enum |
| `prisma/schema.prisma` | โครง DB — model, field, enum, relation |
| `packages/shared-types/src/index.ts` | type/enum ที่ backend+frontend ใช้ร่วม (compiler บังคับ) |

ถ้าเพิ่ม field/endpoint/enum ใหม่: **อัปเดตทั้งสามไฟล์ + `docs/02-system-design.md` ก่อน** แล้วค่อยเขียน implementation.

## Commands

> ยังไม่ scaffold — ชุดคำสั่งเป้าหมาย (ยกมาจาก `dcs-tms` ซึ่งใช้ stack เดียวกัน). ตอน scaffold M1
> ต้องทำให้ `npm run check` ใช้ได้จริงเป็นอย่างแรก เพราะเป็นด่านกันหลงของทุก skill.

```bash
npm ci                    # ติดตั้ง (มี workspaces: packages/*, apps/*)
npm run check             # ด่านรวม: typecheck + prisma validate + unit test  ← รันก่อน commit เสมอ
npm run test:db:setup     # เตรียมฐานทดสอบ (ต้องมี docker compose postgres รันอยู่)
npm run test:int          # integration test (ยิง Postgres จริง) — ไฟล์ *.int.test.ts
npm run test:int:cov      # + coverage gate 100% statement ของ service ที่ทำเสร็จแล้ว
npm run check:all         # check + integration test + coverage gate
npm run typecheck         # tsc ข้าม package (จับ contract หลุดข้ามฝั่ง)
npm run prisma:validate   # ตรวจ schema DB
npm test                  # unit test (vitest); รันไฟล์เดียว: npx vitest run path/to/file.test.ts
docker compose up --build # รันทั้งระบบ (web + api + postgres)
```

CI (`.github/workflows/ci.yml`) ต้องรัน `typecheck + prisma:validate + test` ทุก PR — ถ้าโค้ดไม่ตรง contract จะแดง merge ไม่ได้.

## Guardrails — หลักการที่ห้ามละเมิด

1. **Config-driven** — เกณฑ์ผ่าน (attendance %, คะแนน post-test), สูตรคิดเงิน/ต้นทุน, ราคา, หมวดค่าใช้จ่าย,
   สถานะ/สี, เทมเพลตวุฒิบัตร ต้องแก้ผ่านหน้าจอ (ตาราง `Setting`/master) **ห้าม hard-code**.
   คีย์ config รวมที่ `SETTING_KEYS` ใน shared-types.
2. **Multi-tenant ตั้งแต่วันแรก** — ออกแบบให้เป็น SaaS ได้ตั้งแต่ M1 (ทุก query กรอง tenant, เข้า id
   ข้าม tenant ต้องได้ **404 ไม่ใช่ 403**). ย้อนมาใส่ทีหลัง = รื้อทั้งระบบ.
3. **ระบบเสนอ–คนยืนยัน (human-in-the-loop)** — ระบบแนะนำ คนกดยืนยัน (booking engine เสนอ trainer ที่ qualified+available
   → แอดมินกด Confirm). ยกเว้นที่ตั้งใจให้อัตโนมัติจริง ๆ คือ certificate ตามเงื่อนไข config.
4. **MVP first** — ทำตามลำดับ M1→M8; ส่วนขยาย (SaaS onboarding, payment gateway, e-signature, LINE bot)
   = เฟสหลัง อย่าเผลอทำก่อน.
5. **Mobile-first ฝั่ง trainer/learner** — สแกน QR เช็คชื่อ, ทำข้อสอบ, ดูตารางงาน ต้องใช้บนมือถือลื่นจริง
   (viewport ~414×900). ฝั่งแอดมินเป็นเดสก์ท็อป.
6. **ทุกโมดูลส่งมอบได้จริง** — รันได้ + migration + seed + unit test (โดยเฉพาะสูตรคิดเงิน/เกณฑ์ผ่าน)
   + วิธีรัน; จบโมดูลแล้ว **หยุดรอรีวิว**.
7. คำอธิบายเป็นไทย, โค้ด/ชื่อตัวแปร/คอมเมนต์เทคนิคเป็นอังกฤษ.
8. **สายข้อมูลเส้นเดียวมาก่อนหน้าจอ (data spine first)** — ก่อนเขียนฟีเจอร์ ต้องตอบให้ได้ว่า *ข้อมูลเกิดที่จอไหน
   → เก็บคอลัมน์ไหน → ไหลไปโผล่ที่เอกสาร/รายงานใด*. ตอบไม่ได้ = ยังไม่เริ่มเขียน.
   **ฟิลด์ใหม่ที่ไม่มีปลายทาง = ไม่เพิ่ม** — ปลายทางสุดท้ายของเกือบทุกฟิลด์ในระบบนี้คือ
   **Training Report (PDF)** และ **Finance ต่อ Job**.
9. **ส่งงานเป็นแนวตั้ง (vertical slice) ไม่ใช่รายหน้าจอ** — 1 รอบส่งมอบ = ข้อมูลวิ่งครบเส้นจากต้นทางถึงเอกสารปลายทาง
   + มี integration test ที่เดินครบเส้นนั้นจริง (ไม่ใช่เทสต์เฉพาะ service เดียว).
10. **ทุกฟีเจอร์ต้องมี: เทสต์ครอบ 100% + เอกสาร** — unit/integration รักษา **100% statement**
    (เพิ่มไฟล์ service/controller ใหม่ → เพิ่มชื่อใน `thresholds` ของ `vitest.int.config.ts`)
    และอัปเดต **เอกสารตรวจรับ `docs/acceptance/`** (`npm run docs:acceptance`).
11. **ยึดเอกสารจริงของลูกค้าเป็นสเปก** — ใบเสนอราคา/ใบลงชื่อเข้าอบรม/แบบประเมิน/วุฒิบัตร/รูปเล่มรายงาน
    ที่ใช้อยู่จริง คือ acceptance ของงานนั้น. ขอตัวอย่างจริงมาก่อนออกแบบหน้าจอ.
12. **อ่านเอกสารประชุมให้ครบทุกไฟล์** (ไฟล์สรุป + โน้ตดิบ + Excel + รูปถ่าย/แชท) ก่อนวางแผน —
    ของสำคัญมักอยู่ในโน้ตดิบ ไม่ใช่ไฟล์สรุป.
13. **ไม่มีคนขอ = ไม่ทำ** — ทุกฟีเจอร์ต้องชี้ได้ว่าอยู่บรรทัดไหนของ requirement. ห้ามใส่ "ความฉลาด"
    (สูตรอัตโนมัติ/auto-suggest) ที่ยังไม่มีคนขอ — **ทำช่องกรอกตามจริงก่อนเสมอ** (บทเรียน L5:
    dcs-tms ต้องถอดโหมด Offer + สูตรต้นทุนอัตโนมัติทิ้ง หลังทำเสร็จแล้ว).
14. **แยก "ค่าแผน" กับ "ค่าจริง" คนละคอลัมน์เสมอ** และระบุว่าเอกสารปลายทางอ่านตัวไหน — ห้ามเขียนทับ
    (บทเรียน L4: ทะเบียนรถบนใบวางบิลของ dcs-tms ผิดเงียบ ๆ). ดู `02-system-design.md` §2.4.
15. **ข้อมูลไม่พอ → BLOCKED + เหตุผล ห้ามคืน 0 หรือ fallback เงียบ ๆ** (บทเรียน L9). ตัวเลขที่โผล่หลายหน้า
    ต้องมาจาก helper ตัวเดียวกัน + มีเทสต์เทียบสองหน้าให้เท่ากัน (บทเรียน L8).
16. **ไม่มีคำตอบของคำถามธง 🔴 → ไม่เริ่ม migration แรก** (บทเรียน L1/L2).

## Decision log (สิ่งที่ตัดสินไปแล้ว — อย่ารื้อโดยไม่ถาม)

- **2026-08-24 · Stack:** ใช้ชุดเดียวกับ `dcs-tms` — monorepo (npm workspaces) · NestJS + React ·
  Prisma + Postgres · vitest · Docker Compose. เหตุผล: ทีมเดียวกัน reuse pattern/CI/skills/subagent ได้ทันที
  ไม่ต้องเรียนของใหม่. อ้างอิงของจริงที่รันแล้ว: `/data/WORKSPACE/dcs-tms`.
- **2026-08-24 · Multi-tenant:** ทำตั้งแต่ M1 เพราะเป้าหมายคือขยายเป็น SaaS ให้บริษัทฝึกอบรมอื่นใช้.
- **2026-08-24 · Finance ผูกกับ Job:** รายได้/ต้นทุน/กำไรผูกกับ **Training Job No.** เป็นแกน
  (ไม่ผูกกับหลักสูตรหรือรอบ) — เพื่อให้ตอบได้ว่างานไหนกำไร.
- **2026-08-25 · Design system (LOCKED): "กระดาษสถาบัน"** — ลูกค้าเลือกจาก 3 ทิศทาง หลังปฏิเสธ 2 รอบแรก.
  พื้นกระดาษ `#F7F3EC` · หมึก `#242019` · แบรนด์/ปุ่ม `#2C5240` · เส้นทอง `#B08829` · มุม 3px · ไม่มีเงา.
  **ฟอนต์: IBM Plex Sans Thai (ไม่มีหัว) สำหรับ UI · Trirong เฉพาะหัวเรื่อง/เอกสาร** — เลิกใช้ Sarabun
  เพราะเป็นฟอนต์เอกสารราชการ หนักตาเมื่อย่อเล็ก. SSOT = `apps/web/src/theme.css`.
  **กติกาที่ห้ามละเมิด: ตัวเนื้อหา 16px · line-height 1.7 · เล็กสุด 13px** (อักษรไทยมีวรรณยุกต์บน-ล่าง
  ต้องการระยะมากกว่าละติน 10–15%) · สีบอกสถานะเท่านั้น ห้ามเอา `--accent` ไปแทนสีสถานะ ·
  แบ่งกลุ่มด้วยที่ว่างและเส้นบางก่อน ใช้กล่องเฉพาะที่ต้องแยกจริง · `--gold` ใช้เฉพาะของที่เป็นทางการ.
  หลักฐาน/เหตุผล: `docs/spec/ux-research-2026.md`
- **2026-08-25 · กระบวนการออกแบบ:** ห้ามทำครบทุกหน้าแล้วค่อยให้ลูกค้าดู — สองรอบแรกทำแบบนั้นแล้วถูกปฏิเสธทั้งยวง.
  ต้อง **เสนอ 2–4 ทิศทางบนหน้าจอเดียวกันให้เลือกก่อน** แล้วค่อยขยาย (ใช้ skill `design` ทำ canvas).
- **2026-08-24 · Certificate:** เลข certificate + **QR verify เป็น public endpoint ไม่ต้อง login**
  (คนนอก/ลูกค้าต้องตรวจสอบวุฒิบัตรได้) — แต่ต้องเปิดเผยเฉพาะข้อมูลที่จำเป็น.

## MVP backlog (ทำทีละโมดูล หยุดรีวิว)

> ลำดับนี้ยึด "สายข้อมูลเส้นเดียว" — แต่ละ M คือช่วงหนึ่งของ flow ไม่ใช่กองหน้าจอ. ปรับได้ตอนเฟส requirements.

- **M0** ⬜ ฐานราก anti-drift — git repo + monorepo scaffold + contract 3 ไฟล์ + CI + `npm run check`
- **M1** ⬜ *(ขั้น 0)* Master data + RBAC + tenant — `Tenant`, `User`, `Role`, `Customer`, `Trainer`,
  `Course`, **`TrainerCourse` (Matrix)**, `Venue`, `CostCategory`, `Setting`, `AuditLog`
- **M2** ⬜ *(ขั้น 1–3)* Training Job — Public/In-house → ใบคำขอ → Quotation → ลูกค้ายืนยัน →
  **Job No.** (`TR-YYYY-#####`)
- **M3** ⬜ *(ขั้น 4–6)* **Trainer Booking Engine** + Smart Calendar — qualified (Matrix) × available,
  Tentative → Confirm, กันจองซ้ำ, loop "ไม่พร้อม → หาใหม่", ใบมอบหมายงาน + Location ให้วิทยากร
- **M4** ⬜ *(ขั้น 7–8, 10)* Delivery — ลงทะเบียนผู้เข้าอบรม (นำเข้า/ออนไลน์) + **QR Check-in เช้า–บ่าย**
  + บันทึกเวลาจริง + upload รูปกิจกรรม/เอกสาร
- **M5** ⬜ *(ขั้น 9, 11, 14)* Assessment — Pre/Post test ตรวจอัตโนมัติ + **Retest loop** + แบบประเมินความพึงพอใจ
- **M6** ⬜ *(ขั้น 12–13)* **Certificate Automation** — ตรวจเงื่อนไข (attendance + post-test) → `TRAINING COMPLETED`
  → generate + Certificate No. + **QR verification** (public, ไม่ต้อง login) + ผู้เข้าอบรมดาวน์โหลดเอง
- **M7** ⬜ *(ขั้น 16)* **Finance & Profitability** — revenue/cost ต่อ Job → กำไรขั้นต้น + margin,
  หมวดค่าใช้จ่ายเป็น master, ปิดงาน (`Closed`)
- **M8** ⬜ *(ขั้น 15 + Dashboard)* **One-click Training Report (PDF)** + Analytics
  (attendance · pre/post · pass rate · evaluation · **ประสิทธิภาพวิทยากร**)
- **เฟสหลัง** SaaS onboarding หลายบริษัท, LINE/Email notification, e-signature, payment gateway, e-learning ออนไลน์

## Repo layout (เป้าหมาย)

```
openapi.yaml              # contract: API
prisma/schema.prisma      # contract: DB
packages/shared-types/    # contract: shared TS types (SSOT ของ enum)
apps/api/                 # NestJS backend
apps/web/                 # React (admin) + trainer/learner mobile web
docs/00-lessons-from-dcs-tms.md  # บทเรียนที่ห้ามทำซ้ำ (อ่านก่อนตัดสินใจโครงสร้าง)
docs/01-requirements.md   # เฟส 1 SRS + คำถามเปิด
docs/02-system-design.md  # เฟส 2 — contract ของ design (แก้ที่นี่ก่อนเขียนโค้ด)
docs/spec/                # ภาพ/ไฟล์ที่เป็นสเปกของระบบ (ผังงาน 16 ขั้น)
docs/                     # research, prompts, UI prototype
docs/acceptance/          # เอกสารตรวจรับรายหน้าจอ (1 ไฟล์ / 1 หน้า)
docs/agents/              # config ที่ engineering skills อ่าน (tracker, labels, domain)
.github/workflows/ci.yml  # anti-drift gate
```

## Agent skills

Skill/subagent ยกมาจาก `dcs-tms` (ปรับชื่อโปรเจกต์แล้ว) — บางตัวอ้าง path ที่ยังไม่มีในโครงการนี้
(`docs/HANDOFF.md`, `scripts/gen-acceptance.ts`, `scripts/bot/`) ให้สร้างตอนถึงโมดูลที่เกี่ยวข้อง.

| คำสั่ง | ทำอะไร |
|---|---|
| `/start` | เปิด session — อ่าน resume note + handoff + git แล้วบอกว่าอยู่ตรงไหน ทำต่อตรงไหน |
| `/ship` | commit → merge `main` → push (มีด่านกันเผลอ push ข้อมูลจริงของลูกค้า) |
| `/end` | ปิด session — อัปเดต resume note ในไฟล์นี้ + `docs/HANDOFF.md` |
| `/acceptance [หน้า]` | เขียน/อัปเดตเอกสารตรวจรับรายหน้าจอใน `docs/acceptance/` |
| `/acceptance-check` | ตรวจ drift ระหว่างเอกสารตรวจรับกับโค้ดจริง |

Subagents: `.claude/agents/acceptance-writer.md` (เขียนเอกสารตรวจรับหลายหน้าพร้อมกัน) ·
`.claude/agents/e2e-tester.md` (QA เล่นหน้าจอจริงตามสายข้อมูล headless Chrome).

**เอกสารตรวจรับ (dev-acceptance)** — `docs/acceptance/`: 1 ไฟล์ต่อ 1 หน้าจอ: หน้านี้ทำอะไร · ใครเข้าได้ ·
**ช่องบนจอ ↔ field API ↔ คอลัมน์ DB** · ค่าที่คำนวณตอนอ่าน · กฎธุรกิจ (ชี้ `file → symbol()`) ·
checklist ตรวจรับที่ผู้ใช้ติ๊กเอง. บล็อก `<!-- gen:*:start/end -->` เครื่องสร้าง **ห้ามแก้มือ**; นอกบล็อก = ของคน.

**Issue tracker / triage labels / domain docs** — ดู `docs/agents/*.md` (ยกมาจาก dcs-tms;
**ต้องแก้ให้ชี้ project ของ TrainFlow ก่อนใช้** — ตอนนี้ยังชี้ project `CCM` ของ TMS อยู่).
