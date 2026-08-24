"""ประกอบ artboard จากแหล่งเดียว — helmet + sidebar ยกมาจากหน้าที่ลูกค้าอนุมัติแล้ว
ใช้: python3 _scaffold.py  (อ่าน bodies/*.html แล้วเขียน <ชื่อ>.dc.html)"""
import io, os, re, sys

REF = 'Jobs.dc.html'          # หน้าอ้างอิงที่อนุมัติแล้ว
src = io.open(REF, encoding='utf-8').read()
HEAD = src[:src.index('</helmet>') + len('</helmet>')]

ICONS = {
 'ภาพรวม':'<rect x="3" y="3" width="7" height="9" rx="1.2"/><rect x="14" y="3" width="7" height="5" rx="1.2"/><rect x="14" y="12" width="7" height="9" rx="1.2"/><rect x="3" y="16" width="7" height="5" rx="1.2"/>',
 'งานฝึกอบรม':'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/>',
 'ปฏิทินวิทยากร':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18"/><path d="M8 3v4"/><path d="M16 3v4"/>',
 'ผู้เข้าอบรม':'<path d="M16 20v-1.5a3.5 3.5 0 0 0-3.5-3.5h-5A3.5 3.5 0 0 0 4 18.5V20"/><circle cx="10" cy="8" r="3.2"/><path d="M20 20v-1.4a3.5 3.5 0 0 0-2.6-3.4"/><path d="M15.4 5.2a3.2 3.2 0 0 1 0 5.6"/>',
 'วุฒิบัตร':'<circle cx="12" cy="9" r="5.2"/><path d="M8.6 13.4 7 21l5-2.4L17 21l-1.6-7.6"/>',
 'การเงิน':'<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 11.9h.02"/><path d="M18 11.9h.02"/>',
 'ข้อมูลหลัก':'<ellipse cx="12" cy="6" rx="7.5" ry="3"/><path d="M4.5 6v6c0 1.66 3.36 3 7.5 3s7.5-1.34 7.5-3V6"/><path d="M4.5 12v6c0 1.66 3.36 3 7.5 3s7.5-1.34 7.5-3v-6"/>',
}
def icon(name, size=19):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" style="flex:0 0 auto">'
            f'{ICONS[name]}</svg>')

def sidebar(active):
    rows = '\n'.join(
        f'    <div class="{"snav-on" if n==active else "snav"}">{icon(n)}<span>{n}</span></div>'
        for n in ICONS)
    return ('  <div class="side">\n'
            '    <div style="display:flex; flex-direction:column; gap:2px; padding:0 8px 24px">\n'
            '      <div class="disp" style="font-size:20px; font-weight:600; letter-spacing:.01em">TrainFlow</div>\n'
            '      <div style="font-size:13px; color:#9DB3A5; line-height:1.5; letter-spacing:.04em">SAFETY SKILL CENTER</div>\n'
            '    </div>\n' + rows + '\n  </div>')

def page(active, body, minh=880):
    return (HEAD + f'\n\n<div style="display:grid; grid-template-columns:212px 1fr; '
            f'min-height:{minh}px; background:#F7F3EC">\n' + sidebar(active) +
            '\n  <div style="padding:34px 46px 46px; display:flex; flex-direction:column; gap:28px">\n'
            + body + '\n  </div>\n</div>\n</x-dc>\n</body>\n</html>\n')

def bare(body):
    """หน้าที่ไม่มีแถบเมนู (เช่น หน้าเข้าสู่ระบบ)"""
    return HEAD + '\n\n' + body + '\n</x-dc>\n</body>\n</html>\n'

def head_block(eyebrow, title, sub, actions=''):
    e = f'<div class="n" style="font-size:13px; letter-spacing:.14em; color:#8A7F68">{eyebrow}</div>' if eyebrow else ''
    s = f'<div style="font-size:15px; color:#6E6555">{sub}</div>' if sub else ''
    return (f'''    <div class="rule" style="display:flex; align-items:flex-end; justify-content:space-between; gap:24px">
      <div style="display:flex; flex-direction:column; gap:2px">
        {e}
        <div class="disp" style="font-size:29px; font-weight:600; line-height:1.35">{title}</div>
        {s}
      </div>
      <div style="display:flex; gap:10px; align-items:center">{actions}</div>
    </div>''')

def h2(t):  return f'<div class="disp" style="font-size:19px; font-weight:600">{t}</div>'
def btn(t): return f'<div class="btn">{t}</div>'
def btnp(t):return f'<div class="btn-p">{t}</div>'

if __name__ == '__main__':
    n = 0
    for f in sorted(os.listdir('bodies')):
        if not f.endswith('.py'): continue
        ns = {'page':page,'bare':bare,'head_block':head_block,'h2':h2,'btn':btn,'btnp':btnp,'icon':icon}
        exec(io.open(f'bodies/{f}', encoding='utf-8').read(), ns)
        out = f[:-3] + '.dc.html'
        io.open(out, 'w', encoding='utf-8').write(ns['HTML'])
        s = ns['HTML']
        assert s.count('<div') == s.count('</div>'), f'{out}: div ไม่สมดุล'
        assert s.count('<svg') == s.count('</svg>'), f'{out}: svg ไม่สมดุล'
        print(f'  {out:<24} {len(s):>6} bytes')
        n += 1
    print(f'สร้าง {n} หน้า')
