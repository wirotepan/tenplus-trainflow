def yes():
    return ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2C5240" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>')
def no():
    return '<span style="color:#DDD5C4">·</span>'
def expiring():
    return ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B08829" stroke-width="2.2">'
            '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2" stroke-linecap="round"></path></svg>')

courses = ['Safety Leadership','Risk Assessment','Working at Height','Chemical Safety','5S for Workplace','Basic Safety']
trainers = [
  ('อ.สมชาย โดดี','พนักงานประจำ',[1,1,1,0,1,1],''),
  ('อ.วิภา สุขสวัสดิ์','พนักงานประจำ',[1,1,1,1,1,1],''),
  ('อ.ธนา ประเสริฐ','วิทยากรอิสระ',[1,1,0,0,1,1],''),
  ('อ.กมล รุ่งเรือง','วิทยากรอิสระ',[0,1,1,1,0,1],''),
  ('อ.สุนีย์ วัฒนา','วิทยากรอิสระ',[2,2,0,0,0,1],'ใบรับรองหมดอายุ 31 พ.ค. 2569'),
  ('อ.ณัฐพล ศรีสุข','พนักงานประจำ',[1,0,0,1,1,0],''),
]
head = ''.join(f'<div style="text-align:center">{c.replace(" ","<br>",1)}</div>' for c in courses)
rows = ''
for i,(name,kind,marks,warn) in enumerate(trainers):
    last = i == len(trainers)-1
    cells = ''.join(f'<div style="display:flex; justify-content:center">'
                    f'{yes() if m==1 else (expiring() if m==2 else no())}</div>' for m in marks)
    sub = f'<div style="font-size:14px; color:#8A6A1E">{warn}</div>' if warn else f'<div style="font-size:14px; color:#8A7F68">{kind}</div>'
    rows += (f'<div style="display:grid; grid-template-columns:210px repeat(6, minmax(0,1fr)); gap:14px; padding:14px 22px; '
             f'{"" if last else "border-bottom:1px solid #EFE8DA;"} align-items:center" class="td">'
             f'<div><div style="font-weight:500">{name}</div>{sub}</div>{cells}</div>')

HTML = page('ข้อมูลหลัก', head_block(
    'ข้อมูลหลัก', 'หลักสูตรและทะเบียนวิทยากร',
    'ตารางนี้คือหัวใจของการจองวิทยากร — ระบบจะเสนอเฉพาะคนที่ติ๊กไว้ว่าสอนหลักสูตรนั้นได้',
    btn('เพิ่มหลักสูตร') + btnp('เพิ่มวิทยากร')) + f'''

    <div style="display:flex; gap:10px; flex-wrap:wrap">
      <div class="btn" style="background:#2C5240; color:#F7F3EC; border-color:#2C5240">หลักสูตร · วิทยากร</div>
      <div class="btn">ลูกค้า</div><div class="btn">สถานที่</div><div class="btn">หมวดค่าใช้จ่าย</div>
      <div class="btn">ชุดข้อสอบ</div><div class="btn">แบบประเมิน</div><div class="btn">ผู้ใช้และสิทธิ์</div>
    </div>

    <div style="display:flex; flex-direction:column; gap:14px">
      {h2('ใครสอนหลักสูตรใดได้')}
      <div class="card" style="display:flex; flex-direction:column">
        <div style="display:grid; grid-template-columns:210px repeat(6, minmax(0,1fr)); gap:14px; padding:14px 22px; background:#F2ECDF" class="th">
          <div>วิทยากร</div>{head}
        </div>
        {rows}
      </div>
      <div style="display:flex; gap:26px; flex-wrap:wrap; font-size:14.5px; color:#6E6555">
        <span style="display:flex; gap:9px; align-items:center">{yes()}สอนได้</span>
        <span style="display:flex; gap:9px; align-items:center">{expiring()}คุณสมบัติหมดอายุ ต้องต่ออายุก่อนจึงจะเลือกได้</span>
        <span style="display:flex; gap:9px; align-items:center">{no()}ยังไม่ได้กำหนด</span>
      </div>
    </div>

    <div style="display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:24px; align-items:start">
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('รายละเอียดหลักสูตร')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="display:grid; grid-template-columns:1fr 96px 110px 120px; gap:16px; padding:13px 22px; background:#F2ECDF" class="th">
            <div>หลักสูตร</div><div style="text-align:right">ชั่วโมง</div><div style="text-align:right">เกณฑ์ผ่าน</div><div style="text-align:right">ราคามาตรฐาน</div></div>
          <div style="display:grid; grid-template-columns:1fr 96px 110px 120px; gap:16px; padding:14px 22px; border-bottom:1px solid #EFE8DA" class="td">
            <div style="font-weight:500">Safety Leadership</div><div class="n" style="text-align:right">6</div><div class="n sub" style="text-align:right">80% / 60%</div><div class="n" style="text-align:right">45,000</div></div>
          <div style="display:grid; grid-template-columns:1fr 96px 110px 120px; gap:16px; padding:14px 22px; border-bottom:1px solid #EFE8DA" class="td">
            <div style="font-weight:500">Risk Assessment</div><div class="n" style="text-align:right">12</div><div class="n sub" style="text-align:right">80% / 60%</div><div class="n" style="text-align:right">65,000</div></div>
          <div style="display:grid; grid-template-columns:1fr 96px 110px 120px; gap:16px; padding:14px 22px; border-bottom:1px solid #EFE8DA" class="td">
            <div style="font-weight:500">Working at Height</div><div class="n" style="text-align:right">6</div><div class="n sub" style="text-align:right">100% / 70%</div><div class="n" style="text-align:right">66,500</div></div>
          <div style="display:grid; grid-template-columns:1fr 96px 110px 120px; gap:16px; padding:14px 22px" class="td">
            <div style="font-weight:500">เจ้าหน้าที่ความปลอดภัยระดับหัวหน้างาน</div><div class="n" style="text-align:right">12</div><div class="n sub" style="text-align:right">100% / 60%</div><div class="n" style="text-align:right">58,000</div></div>
        </div>
        <div style="font-size:14.5px; color:#8A7F68; line-height:1.65">
          เกณฑ์ผ่านอ่านว่า ชั่วโมงเข้าอบรมขั้นต่ำ / คะแนนหลังอบรมขั้นต่ำ
          หลักสูตรตามกฎหมายบางตัวต้องเข้าครบ 100% จึงตั้งค่าแยกรายหลักสูตรได้</div>
      </div>

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('เอกสารวิทยากรที่ใกล้หมดอายุ')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; border-left:3px solid #A8342A; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">อ.สุนีย์ วัฒนา — ใบรับรองวิทยากร</div>
            <div style="font-size:14.5px; color:#6E6555">หมดอายุแล้วเมื่อ 31 พฤษภาคม 2569 · ถูกตัดออกจากการจองอัตโนมัติ</div></div>
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; border-left:3px solid #B08829; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">อ.กมล รุ่งเรือง — วุฒิบัตร จป.วิชาชีพ</div>
            <div style="font-size:14.5px; color:#6E6555">หมดอายุ 12 กรกฎาคม 2569 · เหลืออีก 27 วัน</div></div>
          <div style="padding:16px 22px; border-left:3px solid #B08829; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">อ.ธนา ประเสริฐ — ประกันอุบัติเหตุ</div>
            <div style="font-size:14.5px; color:#6E6555">หมดอายุ 30 กรกฎาคม 2569 · เหลืออีก 45 วัน</div></div>
        </div>
        <div style="font-size:14.5px; color:#8A7F68; line-height:1.65">
          ระบบเตือนล่วงหน้าตามจำนวนวันที่ตั้งไว้ และตัดคนที่เอกสารหมดอายุออกจากรายชื่อที่เลือกได้ทันที
          เพื่อไม่ให้เผลอส่งวิทยากรที่คุณสมบัติไม่ครบไปหน้างาน</div>
      </div>
    </div>''', minh=1120)
