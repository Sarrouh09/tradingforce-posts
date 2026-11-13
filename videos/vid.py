"""Generic vertical video builder: scenes = list of (start, end, html). Optional JS for per-frame updates."""
import subprocess, sys, shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/home/claude/postgen'); from render import BASE_CSS, LOGO
CSS="""body{width:1080px;height:1920px;font-family:Inter,'DejaVu Sans',sans-serif}
.sc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0;padding:0 80px}
.brand2{position:absolute;top:90px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px;font-family:'Inter Display';font-weight:700;font-size:34px;letter-spacing:.06em}
.brand2 img{width:80px;height:80px;border-radius:50%;box-shadow:0 0 50px color-mix(in srgb,var(--blue) 50%,transparent)}
.ar{direction:rtl;font-size:72px;font-weight:700;line-height:1.45}.ar2{direction:rtl;font-size:46px;color:var(--muted);line-height:1.6}
.num{width:190px;height:190px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Inter Display';font-weight:800;font-size:110px;margin-bottom:50px;
 background:linear-gradient(135deg,var(--blue-3),var(--cyan));box-shadow:0 0 70px color-mix(in srgb,var(--blue) 55%,transparent)}
.numr{background:linear-gradient(135deg,#b91c1c,var(--loss));box-shadow:0 0 70px color-mix(in srgb,var(--loss) 45%,transparent)}
.btnm{margin-top:50px;background:linear-gradient(90deg,var(--blue-3),var(--blue));padding:28px 48px;border-radius:20px;font-weight:700;font-size:44px;direction:ltr}
.url{margin-top:44px;font-family:'DejaVu Sans Mono';font-size:44px;color:var(--blue-2);padding:24px 36px;border:2px solid var(--line-2);border-radius:18px;direction:ltr}
.gold{color:var(--gold)}.risk{position:absolute;bottom:80px;left:0;right:0;text-align:center;font-size:28px;color:var(--muted);direction:rtl}
.time{font-family:'Inter Display';font-weight:800;font-size:150px;direction:ltr;line-height:1}
"""
def build(name, scenes, dur, risk="التداول فيه مخاطرة · محتوى تعليمي مش نصيحة مالية", js="", fps=30):
    fr=Path(f'/home/claude/video/f_{name}'); shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
    sh="".join(f"<div class='sc' id='s{i}'>{h}</div>" for i,(_,_,h) in enumerate(scenes))
    ts=",".join(f"[{a},{b}]" for a,b,_ in scenes)
    html=f"""<!doctype html><html><head><meta charset='utf-8'><style>{BASE_CSS}{CSS}</style></head><body>
<div class='brand2'><img src='{LOGO}'>TRADING FORCE</div>{sh}<div class='risk'>{risk}</div>
<script>const T=[{ts}];const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
window.R=function(t){{T.forEach(([a,b],i)=>{{const e=document.getElementById('s'+i);let o=0;if(t>=a&&t<b)o=Math.min(1,a==0?1:(t-a)/0.25,(b-t)/0.25);e.style.opacity=o;e.style.transform=`translateY(${{(1-o)*40}}px) scale(${{0.97+0.03*o}})`}});{js}}}</script></body></html>"""
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920}); pg.set_content(html); pg.wait_for_timeout(300)
        for i in range(int(fps*dur)):
            pg.evaluate(f"R({i/fps})"); pg.screenshot(path=str(fr/f'{i:04d}.jpg'),type='jpeg',quality=90)
        b.close()
    out=f'/home/claude/out/video_{name}.mp4'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',str(fr/'%04d.jpg'),'-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',out],check=True)
    shutil.rmtree(fr); return out
