from render import render, BRAND
css="""body{font-family:Inter,'DejaVu Sans',sans-serif}
.gift{display:inline-block;padding:14px 32px;border-radius:999px;font-size:32px;font-weight:800;color:#0b1430;background:linear-gradient(90deg,var(--gold),#ffe08a);box-shadow:0 0 40px color-mix(in srgb,var(--gold) 45%,transparent);letter-spacing:.04em}
.h{direction:rtl;font-size:76px;font-weight:800;line-height:1.3;margin-top:26px}
.card{padding:40px 44px;margin-top:34px}.top{display:flex;justify-content:space-between;align-items:center}
.pair{font-family:'Inter Display';font-weight:800;font-size:52px}
.sell{background:color-mix(in srgb,var(--loss) 16%,transparent);color:var(--loss);border:2px solid var(--loss);padding:10px 26px;border-radius:999px;font-weight:800;font-size:30px}
.zone{margin-top:28px;font-size:26px;color:var(--muted);letter-spacing:.12em}
.zv{font-family:'DejaVu Sans Mono';font-size:76px;font-weight:700;margin-top:6px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;margin-top:30px}
.k{padding:22px 24px;border-radius:18px;border:1px solid var(--line-2);background:color-mix(in srgb,var(--bg) 50%,transparent)}
.k .l{font-size:22px;color:var(--muted);letter-spacing:.1em}.k .v{font-family:'DejaVu Sans Mono';font-size:38px;font-weight:700;margin-top:8px}
.note{direction:rtl;text-align:right;font-size:30px;color:var(--muted);line-height:1.6;margin-top:28px}
.ft2{margin-top:auto;padding-top:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;font-size:24px;color:var(--muted)}.ft2 b{color:var(--gold);font-size:30px}"""
def body(story):
    return f"""{BRAND}
<div style='margin-top:{230 if story else 44}px;text-align:center'><span class='gift'>FREE VIP SIGNAL · 12 NOV · 13:58</span>
<div class='h'>صفقة مجانية<br><span class='grad'>من قناة الـ VIP</span> 🎁</div></div>
<div class='card'><div class='top'><span class='pair'>XAU/USD</span><span class='sell'>SELL LIMIT</span></div>
<div class='zone'>SELL ZONE</div><div class='zv'>4025 – 4035</div>
<div class='g3'><div class='k'><div class='l'>STOP LOSS</div><div class='v' style='color:var(--loss)'>4055</div></div>
<div class='k'><div class='l'>TAKE PROFIT</div><div class='v' style='color:var(--win)'>3980</div></div>
<div class='k'><div class='l'>RISK : REWARD</div><div class='v' style='color:var(--blue-2)'>1 : 2</div></div></div>
<div class='note'>أمر معلّق: الصفقة بتتفعّل بس لو السعر طلع لمنطقة البيع.<br>تابعنا والنتيجة هتنزل هنا، مكسب أو خسارة.</div></div>
<div class='ft2' style='margin-top:{80 if story else 30}px'><span>Trading involves risk · not financial advice</span><b dir='rtl'>ابعتلنا «ذهب» للـ VIP</b></div>"""
render(body(False),"/home/claude/out/free_signal_2026-11-12.png",css)
render(body(True),"/home/claude/out/free_signal_2026-11-12_story.png",css,h=1920)
from PIL import Image
Image.open("/home/claude/out/free_signal_2026-11-12.png").convert("RGB").save("/home/claude/out/free_signal_2026-11-12.jpg",quality=92)
