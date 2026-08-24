def ev(text, sub, tone):
    c = {'ok':('#E4EBE5','#244636','#2C5240'),'hold':('#F6EEDA','#8A6A1E','#B08829'),
         'off':('#F6E7E4','#8A2B22','#A8342A'),'pub':('#F2ECDF','#6E6555','#8A7F68')}[tone]
    return (f'<div style="margin-top:5px; padding:5px 7px; background:{c[0]}; color:{c[1]}; '
            f'border-left:3px solid {c[2]}; font-size:13px; line-height:1.45">'
            f'<div style="font-weight:600">{text}</div><div style="color:#6E6555">{sub}</div></div>')

def day(n, content='', dim=False):
    col = '#A2967F' if dim else '#242019'
    return (f'<div style="border-right:1px solid #EFE8DA; border-bottom:1px solid #EFE8DA; padding:8px; min-height:104px">'
            f'<div class="n" style="font-size:13.5px; color:{col}; font-weight:{"400" if dim else "500"}">{n}</div>{content}</div>')

hdr = ''.join(f'<div style="padding:11px; text-align:center; font-size:13px; color:#8A7F68; font-weight:500; '
              f'border-right:1px solid #EFE8DA; border-bottom:1px solid #E9E1D1">{d}</div>'
              for d in ['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์'])

week1 = (day(7, dim=True) + day(8) + day(9)
       + day(10, ev('Safety Leadership','อ.สมชาย · จองชั่วคราว','hold'))
       + day(11, ev('Basic Safety','อ.นภา · ยืนยันแล้ว','ok')) + day(12) + day(13, dim=True))
week2 = (day(14, dim=True)
       + day(15, ev('Safety Leadership','อ.สมชาย · กำลังอบรม','ok'))
       + day(16, ev('40,000 Awareness','อ.นภา · ยืนยันแล้ว','ok') + ev('อ.กมล ลาพักร้อน','ไม่รับงาน','off'))
       + day(17, ev('Risk Assessment','ยังไม่มีวิทยากร','off'))
       + day(18, ev('Working at Height','อ.วิภา · ยืนยันแล้ว','ok'))
       + day(19) + day(20, ev('Basic Safety','รอบสาธารณะ · รับสมัคร','pub'), dim=True))
week3 = (day(21, dim=True) + day(22, ev('Chemical Safety','อ.ธนา · ยืนยันแล้ว','ok'))
       + day(23, ev('5S for Workplace','อ.กมล · ยืนยันแล้ว','ok'))
       + day(24) + day(25) + day(26) + day(27, dim=True))

legend = ''.join(
    f'<span style="display:flex; gap:8px; align-items:center; font-size:14.5px; color:#6E6555">'
    f'<span style="width:11px; height:11px; background:{bg}; border-left:3px solid {ln}"></span>{t}</span>'
    for t,bg,ln in [('ยืนยันแล้ว','#E4EBE5','#2C5240'),('จองชั่วคราว','#F6EEDA','#B08829'),
                    ('ยังไม่มีวิทยากร / วิทยากรลา','#F6E7E4','#A8342A'),('รอบสาธารณะ','#F2ECDF','#8A7F68')])

HTML = page('ปฏิทินวิทยากร', head_block(
    'มิถุนายน 2569', 'ปฏิทินวิทยากร',
    'เห็นงาน In-house รอบสาธารณะ และวันที่วิทยากรไม่ว่าง ในปฏิทินเดียว',
    btn('เดือน') + btn('สัปดาห์') + btn('รายวิทยากร') + btnp('เพิ่มงาน')) + f'''

    <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap">
      <div class="btn">ทุกวิทยากร</div>
      <div class="btn">ทุกหลักสูตร</div>
      <div style="margin-left:auto; display:flex; gap:22px; flex-wrap:wrap">{legend}</div>
    </div>

    <div class="card" style="display:flex; flex-direction:column">
      <div style="display:grid; grid-template-columns:repeat(7, minmax(0,1fr))">{hdr}</div>
      <div style="display:grid; grid-template-columns:repeat(7, minmax(0,1fr))">{week1}{week2}{week3}</div>
    </div>

    <div style="display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:24px; align-items:start">
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('วิทยากรที่ว่างสัปดาห์นี้')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="display:grid; grid-template-columns:1fr 120px 130px; gap:16px; padding:13px 22px; background:#F2ECDF" class="th">
            <div>วิทยากร</div><div>ว่าง</div><div style="text-align:right">หลักสูตรที่สอนได้</div></div>
          <div style="display:grid; grid-template-columns:1fr 120px 130px; gap:16px; padding:14px 22px; border-bottom:1px solid #EFE8DA" class="td">
            <div style="font-weight:500">อ.วิภา สุขสวัสดิ์</div><div class="n sub">4 วัน</div><div class="n" style="text-align:right">6 หลักสูตร</div></div>
          <div style="display:grid; grid-template-columns:1fr 120px 130px; gap:16px; padding:14px 22px; border-bottom:1px solid #EFE8DA" class="td">
            <div style="font-weight:500">อ.ธนา ประเสริฐ</div><div class="n sub">3 วัน</div><div class="n" style="text-align:right">4 หลักสูตร</div></div>
          <div style="display:grid; grid-template-columns:1fr 120px 130px; gap:16px; padding:14px 22px" class="td">
            <div style="font-weight:500">อ.ณัฐพล ศรีสุข</div><div class="n sub">5 วัน</div><div class="n" style="text-align:right">3 หลักสูตร</div></div>
        </div>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px">
        {h2('ต้องจัดการก่อนถึงวัน')}
        <div class="card" style="display:flex; flex-direction:column">
          <div style="padding:16px 22px; border-bottom:1px solid #EFE8DA; border-left:3px solid #A8342A; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">17 มิ.ย. — Risk Assessment ยังไม่มีวิทยากร</div>
            <div style="font-size:14.5px; color:#6E6555">เหลืออีก 2 วัน · มีคนที่สอนได้และว่าง 3 คน</div></div>
          <div style="padding:16px 22px; border-left:3px solid #B08829; display:flex; flex-direction:column; gap:2px">
            <div style="font-size:15.5px; font-weight:600">10 มิ.ย. — อ.สมชาย ยังไม่ตอบรับงาน</div>
            <div style="font-size:14.5px; color:#6E6555">จองชั่วคราวไว้ ระบบจะปลดวันคืนอัตโนมัติในอีก 12 ชั่วโมง</div></div>
        </div>
      </div>
    </div>''', minh=1080)
