---
name: ship
description: >
  Commit all current work, merge it into main, and push to GitHub — in one step.
  Use when the user says "ship", "ship it", "commit and push", "เอาเข้า main",
  "commit + push", "push ขึ้น main", "ลง main ให้หน่อย". Optional argument = commit subject.
---

# /ship — commit → merge main → push (อัตโนมัติ)

ผู้ใช้ไม่ถนัด terminal — **รันทุกคำสั่งให้เอง** อย่าให้ผู้ใช้พิมพ์ shell. ทำตามลำดับนี้:

## 1. Preflight
- `git branch --show-current` และ `git status --short`.
- ถ้าไม่มีการเปลี่ยนแปลง (working tree สะอาด) → บอก "ไม่มีอะไรให้ commit" แล้วหยุด.
- รัน `npm run check` (typecheck + prisma validate + unit). **ถ้าแดง → หยุด** แสดง error ที่แท้จริง อย่า commit.
  - ถ้าแตะ service/DB layer มาก แนะนำผู้ใช้ว่าควรรัน `npm run check:all` (ต้องมี docker postgres) — แต่ไม่บังคับ.

## 2. ตัวกันเผลอ push ข้อมูลจริง (สำคัญ — ห้ามข้าม)
- หา **ไฟล์ untracked ที่ไม่ใช่ source code**: นามสกุล `.jpg .jpeg .png .webp .gif .pdf .xlsx .xls .csv .zip`
  หรืออยู่ในโฟลเดอร์ที่ชื่อสื่อว่าเป็นข้อมูล/ตัวอย่าง (เช่น `ตัวอย่าง*`, `sample*`, `data/`, `เก็บ`).
- ไฟล์พวกนี้ **อาจเป็นข้อมูลลูกค้าจริง** (เลขผู้เสียภาษี/ชื่อ/ยอดเงิน) — push = เผยแพร่ขึ้น GitHub.
  → **อย่า stage อัตโนมัติ**. ถ้ามี ให้ถามผู้ใช้ด้วย AskUserQuestion (default = ไม่เอาขึ้น) ว่าจะรวมไหม.
- stage เฉพาะที่ตอบตกลง; ที่เหลือ (โค้ด `.ts/.tsx`, เอกสาร `.md`, config, migration, ฟอนต์) stage ได้ปกติ.
- คำสั่ง: `git add -A` แล้ว `git reset -q -- "<โฟลเดอร์/ไฟล์ข้อมูลที่กันไว้>"` (path ไทยต้องใส่ quote).
- ยืนยันด้วย `git diff --cached --name-only` ว่าไม่มีไฟล์ข้อมูลจริงติดไป.

## 3. Branch
- ถ้าอยู่บน `main`/`master`: สร้าง feature branch ก่อน — `git checkout -b feature/<slug>`
  โดย `<slug>` = คำสรุปสั้น ๆ ของงาน (kebab-case ภาษาอังกฤษ เช่น `feature/invoice-pdf`).
- ถ้าอยู่บน branch อื่นอยู่แล้ว: ใช้ branch นั้น ไม่ต้องสร้างใหม่.

## 4. Commit
- อ่าน `git diff --cached --stat` เพื่อสรุปว่าทำอะไร แล้วเขียน **Conventional Commit**:
  - prefix: `feat/fix/docs/refactor/test/chore` ให้ตรงเนื้องาน (มี module tag ได้ เช่น `feat(M5):`).
  - subject ภาษาไทยได้ (ตามกติกา repo: คำอธิบายไทย); ถ้าผู้ใช้ส่ง argument มา ใช้เป็น subject.
  - body = bullet สรุปการเปลี่ยนแปลงหลัก.
  - **ปิดท้ายทุก commit ด้วยบรรทัดนี้เป๊ะ ๆ:**
    `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
- commit ด้วย heredoc: `git commit -q -F - <<'EOF' ... EOF`.

## 5. Merge เข้า main
- `git checkout -q main`
- `git merge --no-ff <feature-branch> -m "merge: <คำสรุปงาน>"` (merge commit ตามแพตเทิร์นของ repo นี้).
- ถ้า merge conflict → **หยุด** รายงาน conflict ให้ผู้ใช้ตัดสิน อย่าแก้มั่ว.

## 6. Push
- `git push origin main`
- `git push -u origin <feature-branch>`
- ถ้า push โดน reject (remote นำหน้า) → **หยุด** รายงาน แนะนำให้ `git pull --rebase` ก่อน อย่า `--force`.

## 7. รายงานผล
สรุปให้ผู้ใช้: hash ของ feat commit + merge commit, branch, ไฟล์ที่ push, และ **ไฟล์ข้อมูลที่กันไว้ไม่ push** (ถ้ามี).

> remote ของ repo นี้: `origin` = GitHub (SSH). default branch = `main`.
