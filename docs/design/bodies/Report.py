toc = [('1','ปก'),('2','ข้อมูลโครงการ'),('3','วัตถุประสงค์การอบรม'),('4','รายละเอียดหลักสูตร'),
       ('5','กำหนดการอบรม'),('6','ประวัติวิทยากร'),('7','รายชื่อผู้เข้าอบรม'),
       ('8','สรุปการเข้าอบรม'),('9','ผลการทดสอบก่อนและหลัง'),('10','การวิเคราะห์พัฒนาการ'),
       ('11','ผลประเมินความพึงพอใจ'),('12','รายชื่อผู้ผ่านการอบรม'),('13','ตัวอย่างวุฒิบัตร'),
       ('14','สรุปผลและข้อเสนอแนะ'),('15','ภาพกิจกรรม')]
items = ''.join(
    f'<div style="display:flex; gap:14px; padding:11px 22px; {"" if i==len(toc)-1 else "border-bottom:1px solid #EFE8DA;"} '
    f'align-items:baseline; {"background:#F2ECDF;" if n=="2" else ""}">'
    f'<span class="n" style="color:#8A7F68; width:26px; flex:0 0 auto">{n}.</span>'
    f'<span style="font-size:15.5px; {"font-weight:600" if n=="2" else ""}">{t}</span></div>'
    for i,(n,t) in enumerate(toc))

HTML = page('งานฝึกอบรม', head_block(
    'TR-2026-00125', 'รายงานผลการฝึกอบรม',
    'สร้างจากข้อมูลที่อยู่ในระบบแล้วทั้งหมด ไม่ต้องพิมพ์ซ้ำ',
    btn('เวอร์ชันก่อนหน้า') + btn('ดาวน์โหลด PDF') + btnp('ส่งให้ลูกค้า')) + f'''

    <div style="display:grid; grid-template-columns:minmax(280px,.72fr) minmax(0,1.28fr); gap:24px; align-items:start">

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('สารบัญ')}
        <div class="card" style="display:flex; flex-direction:column">{items}</div>
        <div style="font-size:14.5px; color:#8A7F68; line-height:1.65; padding:0 4px">
          ทุกหัวข้อดึงจากข้อมูลจริง ยกเว้นหัวข้อ 14 ข้อเสนอแนะ ที่ผู้ประสานงานเขียนเอง</div>
      </div>

      <div style="display:flex; flex-direction:column; gap:14px">
        <div style="display:flex; align-items:baseline; justify-content:space-between">
          {h2('ตัวอย่างหน้า')}
          <span class="n" style="font-size:14.5px; color:#8A7F68">หน้า 2 จาก 16</span>
        </div>
        <div class="card" style="padding:34px 40px; display:flex; flex-direction:column; gap:22px; background:#FFFDF8">
          <div style="display:flex; align-items:baseline; justify-content:space-between; padding-bottom:14px; border-bottom:1px solid #B08829">
            <span class="disp" style="font-size:21px; font-weight:600">ข้อมูลโครงการ</span>
            <span style="font-size:13px; letter-spacing:.14em; color:#8A7F68">SAFETY SKILL CENTER</span>
          </div>

          <div style="display:grid; grid-template-columns:auto 1fr; gap:12px 28px; font-size:15.5px">
            <span class="lbl">เลขที่งาน</span><span class="n" style="font-weight:500">TR-2026-00125</span>
            <span class="lbl">หลักสูตร</span><span style="font-weight:500">Safety Leadership</span>
            <span class="lbl">หน่วยงานผู้รับการอบรม</span><span style="font-weight:500">ABC Manufacturing Co., Ltd.</span>
            <span class="lbl">วันที่จัดอบรม</span><span style="font-weight:500">15 มิถุนายน 2569 เวลา 09:00–16:00 น.</span>
            <span class="lbl">สถานที่</span><span style="font-weight:500">ห้องประชุมชั้น 2 สำนักงานใหญ่ กรุงเทพมหานคร</span>
            <span class="lbl">วิทยากร</span><span style="font-weight:500">อ.สมชาย โดดี · จป.วิชาชีพ</span>
            <span class="lbl">ระยะเวลาอบรม</span><span style="font-weight:500">6 ชั่วโมง</span>
          </div>

          <div style="display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:0; padding-top:18px; border-top:1px solid #EFE8DA">
            <div style="display:flex; flex-direction:column; gap:2px; padding-right:20px">
              <span class="lbl">ผู้เข้าอบรม</span><span class="n disp" style="font-size:26px; font-weight:600; line-height:1.25">60</span></div>
            <div style="display:flex; flex-direction:column; gap:2px; padding:0 20px; border-left:1px solid #EFE8DA">
              <span class="lbl">เข้าอบรมเฉลี่ย</span><span class="n disp" style="font-size:26px; font-weight:600; line-height:1.25">95%</span></div>
            <div style="display:flex; flex-direction:column; gap:2px; padding:0 20px; border-left:1px solid #EFE8DA">
              <span class="lbl">ผ่านเกณฑ์</span><span class="n disp" style="font-size:26px; font-weight:600; line-height:1.25; color:#2C5240">52</span></div>
            <div style="display:flex; flex-direction:column; gap:2px; padding-left:20px; border-left:1px solid #EFE8DA">
              <span class="lbl">ความพึงพอใจ</span><span class="n disp" style="font-size:26px; font-weight:600; line-height:1.25">4.6</span></div>
          </div>

          <div style="font-size:15px; color:#6E6555; line-height:1.8; padding-top:16px; border-top:1px solid #EFE8DA">
            การฝึกอบรมครั้งนี้จัดขึ้นเพื่อเสริมสร้างความรู้ความเข้าใจด้านความปลอดภัยในการทำงาน
            ให้แก่หัวหน้างานและผู้ควบคุมงาน โดยมุ่งเน้นการชี้บ่งอันตราย การประเมินความเสี่ยง
            และการกำหนดมาตรการควบคุมที่เหมาะสมกับลักษณะงานของหน่วยงาน</div>

          <div style="display:flex; justify-content:flex-end; font-size:13.5px; color:#8A7F68; padding-top:10px">2</div>
        </div>

        <div style="display:flex; gap:10px; align-items:center">
          {btn('หน้าก่อนหน้า')}{btn('หน้าถัดไป')}
          <span style="margin-left:auto; font-size:14.5px; color:#8A7F68">
            เก็บทุกเวอร์ชันที่เคยส่งลูกค้า สร้างใหม่แล้วของเดิมยังเปิดดูได้</span>
        </div>
      </div>
    </div>''', minh=1010)
