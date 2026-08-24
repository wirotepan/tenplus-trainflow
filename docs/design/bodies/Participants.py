def mark(kind):
    if kind == 'yes':
        return ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#2C5240" stroke-width="2.4" '
                'stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>')
    if kind == 'no':
        return ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#A8342A" stroke-width="2.2" '
                'stroke-linecap="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>')
    return '<span style="color:#C7BCA6">—</span>'

def row(i, name, comp, am, pm, pre, post, result, tone, last=False):
    col = {'ok':'#2C5240','no':'#A8342A','wait':'#8A6A1E'}[tone]
    bb = '' if last else 'border-bottom:1px solid #EFE8DA;'
    return (f'<div style="display:grid; grid-template-columns:44px 1fr 108px 72px 72px 84px 84px 190px; gap:16px; '
            f'padding:15px 22px; {bb} align-items:center" class="td">'
            f'<div class="n sub">{i}</div><div style="font-weight:500">{name}</div><div class="sub">{comp}</div>'
            f'<div>{mark(am)}</div><div>{mark(pm)}</div>'
            f'<div class="n">{pre}</div><div class="n">{post}</div>'
            f'<div style="color:{col}; font-weight:500">{result}</div></div>')

rows = (row(1,'นายสมชาย โดดี','ABC','yes','yes','60%','85%','ผ่าน · ออกวุฒิบัตรแล้ว','ok')
      + row(2,'นางสาววิไล ใจดี','ABC','yes','yes','60%','70%','ผ่าน · ออกวุฒิบัตรแล้ว','ok')
      + row(3,'นายธเนตร ทองแท้','ABC','yes','no','50%','—','ไม่ผ่าน · ชั่วโมงไม่ครบเกณฑ์','no')
      + row(4,'นางสาวสุภัทร ศรีสุข','ABC','yes','yes','75%','80%','ผ่าน · ออกวุฒิบัตรแล้ว','ok')
      + row(5,'นายวัฒนา นาคดี','ABC','yes','yes','65%','55%','รอสอบซ่อม ครั้งที่ 1 จาก 2','wait')
      + row(6,'นางกมล ทิพย์วารี','ABC','no','no','—','—','ไม่มาอบรม','no', last=True))

HTML = page('ผู้เข้าอบรม', head_block(
    'TR-2026-00125', 'ผู้เข้าอบรม',
    'Safety Leadership · ABC Manufacturing · 15 มิถุนายน 2569',
    btn('นำเข้าจาก Excel') + btn('ส่งออกรายชื่อ') + btnp('เพิ่มผู้เข้าอบรม')) + f'''

    <div class="card" style="display:grid; grid-template-columns:repeat(6, minmax(0,1fr)); gap:0">
      <div style="padding:20px 22px; display:flex; flex-direction:column; gap:2px">
        <span class="lbl">ลงทะเบียนไว้</span><span class="n disp" style="font-size:30px; font-weight:600; line-height:1.2">60</span></div>
      <div style="padding:20px 22px; display:flex; flex-direction:column; gap:2px; border-left:1px solid #EFE8DA">
        <span class="lbl">เข้าอบรมรอบเช้า</span><span class="n disp" style="font-size:30px; font-weight:600; line-height:1.2">58</span></div>
      <div style="padding:20px 22px; display:flex; flex-direction:column; gap:2px; border-left:1px solid #EFE8DA">
        <span class="lbl">เข้าอบรมรอบบ่าย</span><span class="n disp" style="font-size:30px; font-weight:600; line-height:1.2">56</span></div>
      <div style="padding:20px 22px; display:flex; flex-direction:column; gap:2px; border-left:1px solid #EFE8DA">
        <span class="lbl">คะแนนก่อนอบรมเฉลี่ย</span><span class="n disp" style="font-size:30px; font-weight:600; line-height:1.2">52%</span></div>
      <div style="padding:20px 22px; display:flex; flex-direction:column; gap:2px; border-left:1px solid #EFE8DA">
        <span class="lbl">คะแนนหลังอบรมเฉลี่ย</span><span class="n disp" style="font-size:30px; font-weight:600; line-height:1.2">81%</span></div>
      <div style="padding:20px 22px; display:flex; flex-direction:column; gap:2px; border-left:1px solid #B08829">
        <span class="lbl">ผ่านเกณฑ์</span><span class="n disp" style="font-size:30px; font-weight:600; line-height:1.2; color:#2C5240">52</span>
        <span style="font-size:14px; color:#8A7F68">จาก 60 คน</span></div>
    </div>

    <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap">
      <div style="flex:1 1 280px; max-width:320px; padding:10px 14px; background:#FDFBF7; border:1px solid #E9E1D1; font-size:15px; color:#9A9182">ค้นหาชื่อหรืออีเมล</div>
      <div class="btn">ทุกผลการอบรม</div>
      <div style="margin-left:auto; font-size:14.5px; color:#8A7F68">แสดง 1–6 จาก 60 คน</div>
    </div>

    <div class="card" style="display:flex; flex-direction:column">
      <div style="display:grid; grid-template-columns:44px 1fr 108px 72px 72px 84px 84px 190px; gap:16px; padding:13px 22px; background:#F2ECDF" class="th">
        <div>ที่</div><div>ชื่อ–นามสกุล</div><div>บริษัท</div><div>เช้า</div><div>บ่าย</div><div>ก่อน</div><div>หลัง</div><div>ผลการอบรม</div>
      </div>
      {rows}
    </div>

    <div style="font-size:14.5px; color:#8A7F68; line-height:1.65">
      ช่องเช้าและบ่ายมาจากการสแกนเช็คชื่อจริง ระบบคิดชั่วโมงเข้าอบรมให้เอง
      แล้วใช้ร่วมกับคะแนนหลังอบรมตัดสินว่าผ่านหรือไม่ · แก้ไขย้อนหลังได้แต่ต้องระบุเหตุผลและระบบจะบันทึกว่าใครแก้</div>''',
    minh=940)
