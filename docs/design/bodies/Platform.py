def trow(name, plan, users, jobs, storage, renew, status, tone, last=False):
    c = {'ok':'#2C5240','warn':'#8A6A1E','bad':'#A8342A'}[tone]
    bb = '' if last else 'border-bottom:1px solid #EFE8DA;'
    return (f'<div style="display:grid; grid-template-columns:1fr 130px 96px 90px 96px 118px 168px; gap:16px; '
            f'padding:15px 22px; {bb} align-items:center" class="td">'
            f'<div style="font-weight:500">{name}</div><div class="sub">{plan}</div>'
            f'<div class="n" style="text-align:right">{users}</div><div class="n" style="text-align:right">{jobs}</div>'
            f'<div class="n sub" style="text-align:right">{storage}</div><div class="n sub" style="text-align:right">{renew}</div>'
            f'<div style="color:{c}">{status}</div></div>')

rows = (trow('Safety Skill Center','Professional','12 / 15','40','6.2 GB','1 ก.ค. 69','ใช้งานปกติ','ok')
      + trow('TPS Training','Enterprise','38 / ไม่จำกัด','96','41 GB','15 ส.ค. 69','ใช้งานปกติ','ok')
      + trow('ไทยเซฟตี้ อคาเดมี','Starter','3 / 3','18','1.1 GB','22 มิ.ย. 69','โควตาผู้ใช้เต็ม','warn')
      + trow('Delta Learning','Professional','7 / 15','31','3.8 GB','3 ก.ค. 69','ใช้งานปกติ','ok')
      + trow('EPS Academy','ทดลองใช้','2 / 3','4','0.3 GB','28 มิ.ย. 69','ทดลองใช้ เหลือ 13 วัน','warn')
      + trow('Northern Safety','Starter','1 / 3','0','0.0 GB','10 มิ.ย. 69','เลยกำหนดชำระ 5 วัน','bad', last=True))

HTML = page('ข้อมูลหลัก', head_block(
    'สำหรับผู้ให้บริการระบบ', 'คอนโซลผู้ให้บริการ',
    'ดูแลทุกบริษัทที่เช่าใช้ TrainFlow · หน้านี้ผู้ใช้ของบริษัทลูกค้าเข้าไม่ได้',
    btn('รายงานรายได้') + btnp('เปิดบริษัทใหม่')) + f'''

    <div class="card" style="display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:0">
      <div style="padding:22px 24px; display:flex; flex-direction:column; gap:3px">
        <span class="lbl">บริษัทที่ใช้งาน</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">14</span>
        <span style="font-size:14.5px; color:#8A7F68">จ่ายจริง 11 · ทดลองใช้ 3</span></div>
      <div style="padding:22px 24px; display:flex; flex-direction:column; gap:3px; border-left:1px solid #EFE8DA">
        <span class="lbl">รายได้ต่อเดือน</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">78,300</span>
        <span style="font-size:14.5px; color:#2C5240">เพิ่มขึ้น 6,900 จากเดือนก่อน</span></div>
      <div style="padding:22px 24px; display:flex; flex-direction:column; gap:3px; border-left:1px solid #EFE8DA">
        <span class="lbl">งานอบรมทั้งระบบ</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">412</span>
        <span style="font-size:14.5px; color:#8A7F68">เดือนมิถุนายน</span></div>
      <div style="padding:22px 24px; display:flex; flex-direction:column; gap:3px; border-left:1px solid #EFE8DA">
        <span class="lbl">ผู้เข้าอบรมสะสม</span>
        <span class="n disp" style="font-size:32px; font-weight:600; line-height:1.2">28,940</span>
        <span style="font-size:14.5px; color:#8A7F68">ทุกบริษัทรวมกัน</span></div>
    </div>

    <div style="display:flex; flex-direction:column; gap:14px">
      <div style="display:flex; align-items:baseline; justify-content:space-between">
        {h2('บริษัทที่เช่าใช้ระบบ')}
        <span style="font-size:14.5px; color:#8A7F68">เรียงตามวันต่ออายุที่ใกล้ที่สุด</span>
      </div>
      <div class="card" style="display:flex; flex-direction:column">
        <div style="display:grid; grid-template-columns:1fr 130px 96px 90px 96px 118px 168px; gap:16px; padding:13px 22px; background:#F2ECDF" class="th">
          <div>บริษัท</div><div>แพ็กเกจ</div><div style="text-align:right">ผู้ใช้</div><div style="text-align:right">งาน</div>
          <div style="text-align:right">พื้นที่</div><div style="text-align:right">ต่ออายุ</div><div>สถานะ</div></div>
        {rows}
      </div>
    </div>

    <div style="display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:24px; align-items:start">
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('ต้องติดตาม')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; border-left:3px solid #A8342A; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">Northern Safety เลยกำหนดชำระ 5 วัน</div>
            <div style="font-size:14.5px; color:#6E6555">ยังไม่มีการใช้งานในรอบนี้เลย · ระบบจะระงับบัญชีอัตโนมัติในอีก 10 วัน</div></div>
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; border-left:3px solid #B08829; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">EPS Academy ทดลองใช้เหลือ 13 วัน</div>
            <div style="font-size:14.5px; color:#6E6555">สร้างงานไปแล้ว 4 งาน · เหมาะจะเสนอแพ็กเกจ Starter</div></div>
          <div style="padding:16px 22px; border-left:3px solid #B08829; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">ไทยเซฟตี้ อคาเดมี ใช้ผู้ใช้เต็มโควตา</div>
            <div style="font-size:14.5px; color:#6E6555">3 จาก 3 คน · เสนออัปเกรดเป็น Professional ได้</div></div>
        </div>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('การแยกข้อมูลระหว่างบริษัท')}
        <div class="card" style="padding:24px 26px; display:flex; flex-direction:column; gap:14px; font-size:15.5px; line-height:1.75; color:#6E6555">
          <div>ข้อมูลของแต่ละบริษัทถูกแยกที่ระดับฐานข้อมูล ผู้ใช้ของบริษัทหนึ่งเปิดข้อมูลของอีกบริษัทไม่ได้
            แม้จะรู้เลขที่งานก็ตาม ระบบจะตอบว่าไม่พบข้อมูล ไม่ใช่บอกว่าไม่มีสิทธิ์</div>
          <div style="padding-top:14px; border-top:1px solid #EFE8DA">
            ผู้ดูแลของผู้ให้บริการเข้าดูข้อมูลภายในของบริษัทลูกค้าไม่ได้เช่นกัน
            เห็นได้เพียงจำนวนการใช้งานและสถานะการชำระเงินตามตารางด้านบน</div>
        </div>
      </div>
    </div>''', minh=1080)
