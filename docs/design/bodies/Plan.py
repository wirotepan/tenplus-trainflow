def quota(label, used, cap, pct, tone='ok', note=''):
    c = {'ok':'#2C5240','warn':'#B08829','bad':'#A8342A'}[tone]
    n = f'<div style="font-size:14px; color:#8A7F68; line-height:1.6">{note}</div>' if note else ''
    return (f'<div style="display:flex; flex-direction:column; gap:8px">'
            f'<div style="display:flex; justify-content:space-between; align-items:baseline">'
            f'<span style="font-size:15.5px">{label}</span>'
            f'<span class="n" style="font-size:16px; font-weight:600">{used} <span style="color:#8A7F68; font-weight:400">/ {cap}</span></span></div>'
            f'<div style="height:7px; background:#EFE8DA"><div style="width:{pct}%; height:100%; background:{c}"></div></div>{n}</div>')

HTML = page('ข้อมูลหลัก', head_block(
    'บัญชีบริษัท', 'แพ็กเกจและการใช้งาน',
    'Safety Skill Center · แพ็กเกจ Professional · รอบถัดไป 1 กรกฎาคม 2569',
    btn('ประวัติการชำระเงิน') + btnp('เปลี่ยนแพ็กเกจ')) + f'''

    <div style="display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:24px; align-items:stretch">

      <div class="card" style="padding:26px 26px 24px; display:flex; flex-direction:column; gap:14px">
        <div style="display:flex; flex-direction:column; gap:2px">
          <span style="font-size:13px; letter-spacing:.14em; color:#8A7F68">STARTER</span>
          <span class="n disp" style="font-size:30px; font-weight:600; line-height:1.25">2,900<span style="font-size:16px; font-weight:400; color:#8A7F68"> บาท/เดือน</span></span>
        </div>
        <div style="height:1px; background:#EFE8DA"></div>
        <div style="display:flex; flex-direction:column; gap:9px; font-size:15px; color:#6E6555; line-height:1.6">
          <div>งานอบรม 20 งานต่อเดือน</div><div>ผู้ใช้ระบบ 3 คน</div>
          <div>วุฒิบัตรพร้อมรหัสตรวจสอบ</div>
          <div style="color:#A2967F">ไม่รวมรูปเล่มรายงานอัตโนมัติ</div>
          <div style="color:#A2967F">ไม่รวมการปรับแบรนด์ของบริษัท</div>
        </div>
        <div class="btn" style="text-align:center; margin-top:auto">ลดเป็นแพ็กเกจนี้</div>
      </div>

      <div class="card" style="padding:26px 26px 24px; display:flex; flex-direction:column; gap:14px; border-color:#B08829">
        <div style="display:flex; flex-direction:column; gap:2px">
          <div style="display:flex; align-items:center; justify-content:space-between">
            <span style="font-size:13px; letter-spacing:.14em; color:#B08829">PROFESSIONAL</span>
            <span style="font-size:14px; color:#2C5240; font-weight:600">ใช้อยู่</span></div>
          <span class="n disp" style="font-size:30px; font-weight:600; line-height:1.25">6,900<span style="font-size:16px; font-weight:400; color:#8A7F68"> บาท/เดือน</span></span>
        </div>
        <div style="height:1px; background:#B08829"></div>
        <div style="display:flex; flex-direction:column; gap:9px; font-size:15px; color:#6E6555; line-height:1.6">
          <div>งานอบรม 100 งานต่อเดือน</div><div>ผู้ใช้ระบบ 15 คน</div>
          <div>รูปเล่มรายงานอัตโนมัติ</div><div>ปรับโลโก้และสีแบรนด์ของบริษัท</div>
          <div>รายงานต้นทุนและกำไรรายงาน</div>
        </div>
        <div class="btn" style="text-align:center; margin-top:auto; color:#A2967F">แพ็กเกจปัจจุบัน</div>
      </div>

      <div class="card" style="padding:26px 26px 24px; display:flex; flex-direction:column; gap:14px">
        <div style="display:flex; flex-direction:column; gap:2px">
          <span style="font-size:13px; letter-spacing:.14em; color:#8A7F68">ENTERPRISE</span>
          <span class="disp" style="font-size:30px; font-weight:600; line-height:1.25">ตามการใช้งาน</span>
        </div>
        <div style="height:1px; background:#EFE8DA"></div>
        <div style="display:flex; flex-direction:column; gap:9px; font-size:15px; color:#6E6555; line-height:1.6">
          <div>งานอบรมและผู้ใช้ไม่จำกัด</div><div>ใช้โดเมนของบริษัทเองและเข้าระบบด้วยบัญชีองค์กร</div>
          <div>เชื่อมข้อมูลกับระบบบัญชีหรือ HR</div><div>ผู้ดูแลเฉพาะรายและข้อตกลงระดับบริการ</div>
        </div>
        <div class="btn-p" style="text-align:center; margin-top:auto">ติดต่อฝ่ายขาย</div>
      </div>
    </div>

    <div style="display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:24px; align-items:start">

      <div style="display:flex; flex-direction:column; gap:14px">
        <div style="display:flex; align-items:baseline; justify-content:space-between">
          {h2('การใช้งานรอบนี้')}
          <span style="font-size:14.5px; color:#8A7F68">1–30 มิถุนายน 2569 · เหลืออีก 15 วัน</span>
        </div>
        <div class="card" style="padding:24px 26px; display:flex; flex-direction:column; gap:20px">
          {quota('งานฝึกอบรม','40','100 งาน',40)}
          {quota('ผู้ใช้ระบบ','12','15 คน',80,'warn','ใกล้เต็มโควตา — ระบบจะเตือนก่อนที่จะเพิ่มคนไม่ได้')}
          {quota('พื้นที่เก็บไฟล์ รูปกิจกรรมและเอกสาร','6.2','20 GB',31)}
          {quota('วุฒิบัตรที่ออกในรอบนี้','2,280','ไม่จำกัด',100)}
        </div>
      </div>

      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('แบรนด์ของบริษัท')}
        <div class="card" style="padding:24px 26px; display:flex; flex-direction:column; gap:18px">
          <div style="display:flex; gap:16px; align-items:center">
            <div class="disp" style="width:54px; height:54px; background:#2C5240; color:#E9E3D6; display:flex; align-items:center; justify-content:center; font-size:19px; font-weight:600; flex:0 0 auto">SS</div>
            <div style="display:flex; flex-direction:column; gap:2px">
              <span style="font-size:16px; font-weight:600">Safety Skill Center Co., Ltd.</span>
              <span style="font-size:14.5px; color:#8A7F68">ชื่อที่พิมพ์บนวุฒิบัตรและรูปเล่มรายงาน</span></div>
          </div>
          <div style="display:flex; flex-direction:column; gap:9px">
            <span class="lbl">สีหลักของแบรนด์</span>
            <div style="display:flex; gap:10px">
              <span style="width:34px; height:34px; background:#2C5240; box-shadow:0 0 0 1px #FDFBF7, 0 0 0 3px #B08829"></span>
              <span style="width:34px; height:34px; background:#1F4E79"></span>
              <span style="width:34px; height:34px; background:#7B2D3B"></span>
              <span style="width:34px; height:34px; background:#4A4A42"></span>
              <span style="width:34px; height:34px; background:#B08829"></span>
            </div>
          </div>
          <div style="display:flex; flex-direction:column; gap:7px">
            <span class="lbl">รูปแบบเลขที่วุฒิบัตร</span>
            <div class="n" style="padding:11px 14px; background:#F7F3EC; border:1px solid #E9E1D1; font-size:15.5px">SSC-{{ปี}}-{{เลขงาน}}-{{ลำดับ}}</div>
            <span style="font-size:14px; color:#8A7F68">ตัวอย่างที่ออกจริง SSC-2569-00125-0001</span>
          </div>
          <div style="font-size:14.5px; color:#8A7F68; line-height:1.65; padding-top:14px; border-top:1px solid #EFE8DA">
            แต่ละบริษัทที่ใช้ระบบเห็นแบรนด์ของตัวเอง ทั้งบนหน้าจอ วุฒิบัตร และรูปเล่มรายงาน
            ข้อมูลของแต่ละบริษัทแยกขาดจากกัน เข้าดูข้ามกันไม่ได้</div>
        </div>
      </div>
    </div>''', minh=1080)
