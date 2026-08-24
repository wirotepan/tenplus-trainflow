def step(n, label, state):
    if state == 'done':
        mark = ('<div style="width:30px; height:30px; border-radius:20px; background:#2C5240; color:#F7F3EC; display:flex; align-items:center; justify-content:center">'
                '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>')
        col = '#242019'
    elif state == 'now':
        mark = f'<div class="n" style="width:30px; height:30px; border-radius:20px; background:#B08829; color:#FDFBF7; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:600">{n}</div>'
        col = '#8A6A1E'
    else:
        mark = f'<div class="n" style="width:30px; height:30px; border-radius:20px; border:1px solid #D8CFBD; color:#A2967F; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:600">{n}</div>'
        col = '#A2967F'
    w = '600' if state != 'todo' else '400'
    return (f'<div style="flex:1 1 0; display:flex; flex-direction:column; align-items:center; gap:7px">{mark}'
            f'<div style="font-size:14px; font-weight:{w}; color:{col}; text-align:center">{label}</div></div>')

def line(done):
    return f'<div style="flex:0 0 auto; width:44px; height:1px; background:{"#2C5240" if done else "#E0D6C2"}"></div>'

steps = [('ลูกค้า','done'),('หลักสูตร','done'),('ประเภทงาน','now'),('วัน/เวลา','todo'),
         ('ผู้เข้าอบรม','todo'),('วิทยากร','todo'),('การเงิน','todo'),('ตรวจสอบ','todo')]
bar = ''
for i,(lab,st) in enumerate(steps):
    if i: bar += line(steps[i-1][1] == 'done')
    bar += step(i+1, lab, st)

HTML = page('งานฝึกอบรม', head_block(
    'ขั้นที่ 3 จาก 8', 'สร้างงานฝึกอบรม', 'เลือกประเภทงานและรูปแบบการรับผู้เข้าอบรม',
    btn('บันทึกร่าง')) + f'''

    <div class="card" style="display:flex; align-items:flex-start; padding:22px 26px">{bar}</div>

    <div style="display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.75fr); gap:24px; align-items:start">

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('ประเภทงานอบรม')}

        <div class="card" style="padding:22px 24px; border-color:#2C5240; display:flex; gap:16px; align-items:flex-start">
          <span style="width:19px; height:19px; border-radius:19px; border:5px solid #2C5240; background:#FDFBF7; flex:0 0 auto; margin-top:4px"></span>
          <div style="display:flex; flex-direction:column; gap:6px">
            <div style="font-size:17px; font-weight:600">In-house — จัดให้ลูกค้าเฉพาะราย</div>
            <div style="font-size:15px; color:#6E6555; line-height:1.65">ลูกค้าระบุหลักสูตร วันที่ จำนวนคน และสถานที่เอง
              ระบบจะออกใบเสนอราคาให้ก่อน แล้วจึงสร้างเลขที่งานเมื่อลูกค้ายืนยัน</div>
          </div>
        </div>

        <div class="card" style="padding:22px 24px; display:flex; gap:16px; align-items:flex-start">
          <span style="width:19px; height:19px; border-radius:19px; border:1px solid #D8CFBD; background:#FDFBF7; flex:0 0 auto; margin-top:4px"></span>
          <div style="display:flex; flex-direction:column; gap:6px">
            <div style="font-size:17px; font-weight:600; color:#6E6555">Public — เปิดรอบสาธารณะ</div>
            <div style="font-size:15px; color:#6E6555; line-height:1.65">บริษัทกำหนดวันเอง แล้วเปิดรับสมัครรายบุคคลผ่านลิงก์
              ผู้สมัครมาจากหลายบริษัทได้ ระบบออกใบเสนอราคาเป็นรายคน</div>
          </div>
        </div>

        <div style="display:flex; flex-direction:column; gap:14px; margin-top:8px">
          {h2('รายละเอียดเพิ่มเติม')}
          <div class="card" style="padding:22px 24px; display:grid; grid-template-columns:1fr 1fr; gap:18px 22px">
            <div style="display:flex; flex-direction:column; gap:7px">
              <span style="font-size:14px; color:#6E6555; font-weight:500">สถานที่จัดอบรม</span>
              <div style="padding:11px 14px; background:#F7F3EC; border:1px solid #E9E1D1; font-size:15.5px">ห้องประชุมชั้น 2 · ABC Manufacturing</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:7px">
              <span style="font-size:14px; color:#6E6555; font-weight:500">จำนวนผู้เข้าอบรมที่คาดไว้</span>
              <div class="n" style="padding:11px 14px; background:#F7F3EC; border:1px solid #E9E1D1; font-size:15.5px">60 คน</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:7px; grid-column:1 / -1">
              <span style="font-size:14px; color:#6E6555; font-weight:500">ข้อกำหนดพิเศษจากลูกค้า</span>
              <div style="padding:11px 14px; background:#F7F3EC; border:1px solid #E9E1D1; font-size:15.5px; color:#9A9182; line-height:1.7">
                เช่น ต้องการวิทยากรที่มีประสบการณ์โรงงานพลาสติก หรือขอเอกสารเป็นภาษาอังกฤษ</div>
            </div>
          </div>
        </div>
      </div>

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('สรุปที่เลือกไว้')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; display:flex; flex-direction:column; gap:2px">
            <span class="lbl">ลูกค้า</span>
            <span style="font-size:15.5px; font-weight:500">ABC Manufacturing Co., Ltd.</span>
            <span style="font-size:14px; color:#8A7F68">คุณสมศรี โดดี · 02-123-4567</span>
          </div>
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; display:flex; flex-direction:column; gap:2px">
            <span class="lbl">หลักสูตร</span>
            <span style="font-size:15.5px; font-weight:500">Safety Leadership</span>
            <span style="font-size:14px; color:#8A7F68">6 ชั่วโมง · ราคามาตรฐาน 45,000 บาท</span>
          </div>
          <div style="padding:16px 22px; display:flex; flex-direction:column; gap:2px">
            <span class="lbl">ประเภทงาน</span>
            <span style="font-size:15.5px; font-weight:500">In-house</span>
          </div>
        </div>
        <div style="font-size:14.5px; color:#8A7F68; line-height:1.65; padding:0 4px">
          เลขที่งานจะออกให้เมื่อลูกค้ายืนยันใบเสนอราคาแล้วเท่านั้น ระหว่างนี้ยังเป็นร่าง แก้ไขได้ทุกขั้น</div>
      </div>
    </div>

    <div style="display:flex; gap:10px; justify-content:flex-end; padding-top:8px; border-top:1px solid #E9E1D1">
      {btn('ย้อนกลับ')}{btnp('ถัดไป — เลือกวันและเวลา')}
    </div>''', minh=950)
