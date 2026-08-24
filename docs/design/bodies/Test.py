def qrow(n, text, correct, wrong, last=False):
    bb = '' if last else 'border-bottom:1px solid #EFE8DA;'
    pct = round(correct*100/(correct+wrong))
    tone = '#2C5240' if pct >= 70 else ('#8A6A1E' if pct >= 50 else '#A8342A')
    return (f'<div style="display:grid; grid-template-columns:52px 1fr 130px 96px; gap:16px; padding:15px 22px; {bb} align-items:center" class="td">'
            f'<div class="n sub">{n}</div><div>{text}</div>'
            f'<div style="display:flex; align-items:center; gap:10px">'
            f'<div style="flex:1 1 auto; height:6px; background:#EFE8DA"><div style="width:{pct}%; height:100%; background:{tone}"></div></div></div>'
            f'<div class="n" style="text-align:right; color:{tone}; font-weight:500">{pct}%</div></div>')

qs = (qrow(1,'ข้อใดคือความหมายของ P-D-C-A',55,5)
    + qrow(2,'ผู้ควบคุมงานมีหน้าที่ใดตามกฎหมายความปลอดภัย',48,12)
    + qrow(3,'อุปกรณ์คุ้มครองความปลอดภัยส่วนบุคคลข้อใดใช้กับงานที่สูง',52,8)
    + qrow(4,'ลำดับขั้นการควบคุมอันตรายข้อใดควรทำก่อน',31,29)
    + qrow(5,'การชี้บ่งอันตรายควรทำเมื่อใด',44,16, last=True))

HTML = page('งานฝึกอบรม', head_block(
    'TR-2026-00125', 'แบบทดสอบก่อนและหลังอบรม',
    'Safety Leadership · ชุดข้อสอบ 20 ข้อ · ระบบตรวจให้อัตโนมัติทันทีที่ส่ง',
    btn('ธนาคารข้อสอบ') + btnp('เปิดให้ทำแบบทดสอบหลังอบรม')) + f'''

    <div style="display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr) minmax(0,1fr); gap:24px">
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:12px">
        <span class="lbl">ก่อนอบรม (Pre-test)</span>
        <div style="display:flex; align-items:baseline; gap:10px">
          <span class="n disp" style="font-size:34px; font-weight:600; line-height:1.2">52%</span>
          <span style="font-size:15px; color:#6E6555">คะแนนเฉลี่ย</span></div>
        <div style="font-size:14.5px; color:#8A7F68">ทำครบ 60 จาก 60 คน</div>
      </div>
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:12px">
        <span class="lbl">หลังอบรม (Post-test)</span>
        <div style="display:flex; align-items:baseline; gap:10px">
          <span class="n disp" style="font-size:34px; font-weight:600; line-height:1.2; color:#2C5240">81%</span>
          <span style="font-size:15px; color:#6E6555">คะแนนเฉลี่ย</span></div>
        <div style="font-size:14.5px; color:#8A7F68">ทำครบ 58 จาก 60 คน · เกณฑ์ผ่าน 60%</div>
      </div>
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:12px; border-color:#B08829">
        <span class="lbl">พัฒนาการ</span>
        <div style="display:flex; align-items:baseline; gap:10px">
          <span class="n disp" style="font-size:34px; font-weight:600; line-height:1.2; color:#2C5240">+29</span>
          <span style="font-size:15px; color:#6E6555">จุด</span></div>
        <div style="font-size:14.5px; color:#8A7F68">ตัวเลขนี้ไปอยู่ในรูปเล่มรายงานหัวข้อวิเคราะห์ผล</div>
      </div>
    </div>

    <div style="display:grid; grid-template-columns:minmax(0,1.25fr) minmax(0,.8fr); gap:24px; align-items:start">

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('ข้อที่ผู้เรียนตอบถูกน้อย')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="display:grid; grid-template-columns:52px 1fr 130px 96px; gap:16px; padding:13px 22px; background:#F2ECDF" class="th">
            <div>ข้อ</div><div>คำถาม (หลังอบรม)</div><div>สัดส่วนตอบถูก</div><div style="text-align:right">ร้อยละ</div></div>
          {qs}
        </div>
        <div style="font-size:14.5px; color:#8A7F68; line-height:1.65">
          ข้อ 4 ตอบถูกเพียง 52% — ใช้เป็นข้อเสนอแนะให้วิทยากรเน้นเนื้อหาส่วนนี้ในรุ่นถัดไป
          ระบบจะดึงข้อสังเกตนี้ไปขึ้นในรูปเล่มรายงานให้อัตโนมัติ</div>
      </div>

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('การสอบซ่อม')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; display:flex; justify-content:space-between; align-items:baseline">
            <span style="font-size:15.5px">ผ่านตั้งแต่ครั้งแรก</span><span class="n" style="font-size:19px; font-weight:600; color:#2C5240">52</span></div>
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; display:flex; justify-content:space-between; align-items:baseline">
            <span style="font-size:15.5px">กำลังรอสอบซ่อม</span><span class="n" style="font-size:19px; font-weight:600; color:#8A6A1E">4</span></div>
          <div style="padding:16px 22px; display:flex; justify-content:space-between; align-items:baseline">
            <span style="font-size:15.5px">ยังไม่ได้ทำแบบทดสอบ</span><span class="n" style="font-size:19px; font-weight:600; color:#8A7F68">2</span></div>
        </div>

        <div class="card" style="padding:20px 22px; display:flex; flex-direction:column; gap:12px">
          <span class="lbl">กติกาที่ตั้งไว้สำหรับหลักสูตรนี้</span>
          <div style="display:flex; justify-content:space-between; font-size:15.5px"><span class="sub">คะแนนผ่านขั้นต่ำ</span><span class="n" style="font-weight:500">60%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:15.5px"><span class="sub">สอบซ่อมได้ไม่เกิน</span><span class="n" style="font-weight:500">2 ครั้ง</span></div>
          <div style="display:flex; justify-content:space-between; font-size:15.5px"><span class="sub">เวลาทำข้อสอบ</span><span class="n" style="font-weight:500">30 นาที</span></div>
          <div style="display:flex; justify-content:space-between; font-size:15.5px"><span class="sub">สลับลำดับข้อและตัวเลือก</span><span style="font-weight:500">เปิดใช้งาน</span></div>
          <div style="font-size:14px; color:#8A7F68; line-height:1.65; padding-top:10px; border-top:1px solid #EFE8DA">
            ระบบใช้คะแนนครั้งที่ดีที่สุดตัดสินผ่าน แต่เก็บผลทุกครั้งไว้ในรายงาน</div>
        </div>
      </div>
    </div>''', minh=980)
