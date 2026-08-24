def costrow(name, budget, actual, last=False):
    d = actual - budget
    if d > 0:   col, txt, note = '#A8342A', f'+{d:,}', 'เกินงบ'
    elif d < 0: col, txt, note = '#2C5240', f'{d:,}', 'ต่ำกว่างบ'
    else:       col, txt, note = '#6E6555', '0', 'ตรงงบ'
    bb = '' if last else 'border-bottom:1px solid #EFE8DA;'
    return (f'<div style="display:grid; grid-template-columns:1fr 120px 120px 110px 120px; gap:16px; padding:14px 22px; {bb} align-items:center" class="td">'
            f'<div>{name}</div><div class="n sub" style="text-align:right">{budget:,}</div>'
            f'<div class="n" style="text-align:right; font-weight:500">{actual:,}</div>'
            f'<div class="n" style="text-align:right; color:{col}">{txt}</div>'
            f'<div style="text-align:right; color:{col}; font-size:14.5px">{note}</div></div>')

costs = (costrow('ค่าวิทยากร',12000,12000) + costrow('ค่าเดินทางวิทยากร',1500,2000)
       + costrow('ค่าที่พัก',2000,1500) + costrow('ค่าอาหารและเบรก',6000,4800)
       + costrow('ค่าเอกสารประกอบการอบรม',1200,1200) + costrow('ค่าอุปกรณ์',1000,1000)
       + costrow('ค่าสถานที่',2000,2000) + costrow('ค่าใช้จ่ายอื่น',800,500, last=True))

HTML = page('การเงิน', head_block(
    'TR-2026-00125', 'การเงินและกำไรของงาน',
    'Safety Leadership · ABC Manufacturing · เห็นได้เฉพาะฝ่ายการเงิน ผู้บริหาร และผู้ดูแลระบบ',
    btn('เพิ่มค่าใช้จ่าย') + btnp('ปิดงาน')) + f'''

    <div style="display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:24px">
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:3px">
        <span class="lbl">รายได้สุทธิ</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">42,000</span>
        <span style="font-size:14.5px; color:#8A7F68">ราคาขาย 45,000 หักส่วนลด 3,000</span></div>
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:3px">
        <span class="lbl">ต้นทุนที่ใช้จริง</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">25,000</span>
        <span style="font-size:14.5px; color:#2C5240">ต่ำกว่างบที่ตั้งไว้ 1,500 บาท</span></div>
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:3px; border-color:#B08829">
        <span class="lbl">กำไรขั้นต้น</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2; color:#2C5240">17,000</span>
        <span style="font-size:14.5px; color:#8A7F68">อัตรากำไร 40.5%</span></div>
      <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:3px">
        <span class="lbl">ต้นทุนต่อผู้เข้าอบรม</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">417</span>
        <span style="font-size:14.5px; color:#8A7F68">คิดจากผู้เข้าอบรมจริง 60 คน</span></div>
    </div>

    <div style="display:flex; flex-direction:column; gap:14px">
      <div style="display:flex; align-items:baseline; justify-content:space-between">
        {h2('งบที่ตั้งไว้ เทียบกับที่ใช้จริง')}
        <span style="font-size:14.5px; color:#8A7F68">หมวดค่าใช้จ่ายเพิ่มหรือแก้ชื่อได้เองที่ข้อมูลหลัก</span>
      </div>
      <div class="card" style="display:flex; flex-direction:column">
        <div style="display:grid; grid-template-columns:1fr 120px 120px 110px 120px; gap:16px; padding:13px 22px; background:#F2ECDF" class="th">
          <div>หมวดค่าใช้จ่าย</div><div style="text-align:right">ตั้งงบไว้</div><div style="text-align:right">ใช้จริง</div>
          <div style="text-align:right">ส่วนต่าง</div><div style="text-align:right">สถานะ</div></div>
        {costs}
        <div style="display:grid; grid-template-columns:1fr 120px 120px 110px 120px; gap:16px; padding:16px 22px; background:#F2ECDF; align-items:center">
          <div style="font-weight:600; font-size:16px">รวมทั้งสิ้น</div>
          <div class="n sub" style="text-align:right; font-size:16px">26,500</div>
          <div class="n" style="text-align:right; font-weight:600; font-size:16px">25,000</div>
          <div class="n" style="text-align:right; color:#2C5240; font-weight:600; font-size:16px">-1,500</div>
          <div style="text-align:right; color:#2C5240; font-size:14.5px; font-weight:500">ต่ำกว่างบ</div></div>
      </div>
      <div style="font-size:14.5px; color:#8A7F68; line-height:1.65">
        ค่าเดินทางเกินงบ 500 บาท เพราะเปลี่ยนวิทยากรกลางทางและต้องเดินทางจากต่างจังหวัด
        ระบบเตือนตั้งแต่วันที่บันทึกค่าใช้จ่าย ไม่ต้องรอปิดงบสิ้นเดือน</div>
    </div>

    <div style="display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:24px; align-items:start">
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('สัดส่วนต้นทุน')}
        <div class="card" style="padding:22px 24px; display:flex; flex-direction:column; gap:14px">
          <div style="display:flex; height:14px; overflow:hidden">
            <div style="width:48%; background:#2C5240"></div><div style="width:19.2%; background:#4E7A63"></div>
            <div style="width:8%; background:#7FA48F"></div><div style="width:8%; background:#B08829"></div>
            <div style="width:6%; background:#C9A557"></div><div style="width:10.8%; background:#D8CFBD"></div>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px 20px; font-size:15px">
            <span style="display:flex; gap:9px; align-items:center"><span style="width:11px; height:11px; background:#2C5240"></span>ค่าวิทยากร <span class="n sub" style="margin-left:auto">48%</span></span>
            <span style="display:flex; gap:9px; align-items:center"><span style="width:11px; height:11px; background:#4E7A63"></span>อาหารและเบรก <span class="n sub" style="margin-left:auto">19%</span></span>
            <span style="display:flex; gap:9px; align-items:center"><span style="width:11px; height:11px; background:#7FA48F"></span>เดินทาง <span class="n sub" style="margin-left:auto">8%</span></span>
            <span style="display:flex; gap:9px; align-items:center"><span style="width:11px; height:11px; background:#B08829"></span>สถานที่ <span class="n sub" style="margin-left:auto">8%</span></span>
            <span style="display:flex; gap:9px; align-items:center"><span style="width:11px; height:11px; background:#C9A557"></span>ที่พัก <span class="n sub" style="margin-left:auto">6%</span></span>
            <span style="display:flex; gap:9px; align-items:center"><span style="width:11px; height:11px; background:#D8CFBD"></span>อื่น ๆ <span class="n sub" style="margin-left:auto">11%</span></span>
          </div>
        </div>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('ก่อนปิดงาน')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="padding:15px 22px; border-bottom:1px solid #EFE8DA; display:flex; gap:12px; align-items:center; font-size:15.5px">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#2C5240" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            บันทึกค่าใช้จ่ายครบทุกหมวดแล้ว</div>
          <div style="padding:15px 22px; border-bottom:1px solid #EFE8DA; display:flex; gap:12px; align-items:center; font-size:15.5px">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#2C5240" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            ออกวุฒิบัตรครบ 52 ใบ</div>
          <div style="padding:15px 22px; border-bottom:1px solid #EFE8DA; display:flex; gap:12px; align-items:center; font-size:15.5px; color:#8A6A1E">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#B08829" stroke-width="2.2"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2" stroke-linecap="round"></path></svg>
            ยังไม่ได้ส่งรูปเล่มรายงานให้ลูกค้า</div>
          <div style="padding:15px 22px; display:flex; gap:12px; align-items:center; font-size:15.5px; color:#8A6A1E">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#B08829" stroke-width="2.2"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2" stroke-linecap="round"></path></svg>
            ยังไม่ได้แนบสำเนาใบเสร็จค่าสถานที่</div>
        </div>
        <div style="font-size:14.5px; color:#8A7F68; line-height:1.65">
          เมื่อปิดงานแล้วระบบจะล็อกไม่ให้แก้คะแนน การเช็คชื่อ และตัวเลขการเงินย้อนหลัง
          หากจำเป็นต้องแก้ ต้องใช้สิทธิ์ผู้ดูแลระบบและระบุเหตุผล</div>
      </div>
    </div>''', minh=1120)
