import base64, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/home/claude/postgen'); from render import BASE_CSS, LOGO
FPS=30; DUR=16.0; OUT='/home/claude/out/video_monday_results.mp4'; FR=Path('/home/claude/video/frames'); FR.mkdir(exist_ok=True)
for f in FR.glob('*.jpg'): f.unlink()
html=f"""<!doctype html><html><head><meta charset='utf-8'><style>{BASE_CSS}
body{{width:1080px;height:1920px;font-family:Inter,'DejaVu Sans',sans-serif}}
.sc{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0;padding:0 80px}}
.brand2{{position:absolute;top:90px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px;font-family:'Inter Display';font-weight:700;font-size:34px;letter-spacing:.06em}}
.brand2 img{{width:80px;height:80px;border-radius:50%;box-shadow:0 0 50px color-mix(in srgb,var(--blue) 50%,transparent)}}
.huge{{font-family:'Inter Display';font-weight:800;font-size:260px;color:var(--win);line-height:1;text-shadow:0 0 80px color-mix(in srgb,var(--win) 40%,transparent);direction:ltr}}
.ar{{direction:rtl;font-size:64px;font-weight:700;line-height:1.5}}.ar2{{direction:rtl;font-size:44px;color:var(--muted);line-height:1.6}}
.tag{{display:inline-block;padding:14px 34px;border-radius:999px;font-size:40px;font-weight:700;background:color-mix(in srgb,var(--loss) 16%,transparent);color:var(--loss);border:2px solid var(--loss);direction:rtl}}
.price{{font-family:'DejaVu Sans Mono';font-size:120px;font-weight:700;direction:ltr;margin:30px 0}}
.row{{display:flex;gap:40px;justify-content:center;font-family:'DejaVu Sans Mono';font-size:40px;color:var(--muted);direction:ltr}}
.pip{{font-family:'Inter Display';font-weight:800;font-size:150px;color:var(--win);direction:ltr}}
.risk{{position:absolute;bottom:80px;left:0;right:0;text-align:center;font-size:28px;color:var(--muted);direction:rtl}}
</style></head><body>
<div class='brand2'><img src='{LOGO}'>TRADING FORCE</div>
<div class='sc' id='s1'><div class='ar'>في يوم واحد على الدهب</div><div class='huge' id='h1'>+0</div><div class='ar2'>نقطة · يوم الإتنين ٩ نوفمبر</div></div>
<div class='sc' id='s2'><span class='tag'>الصفقة الأولى · بيع</span><div class='price' id='p2'>4130.000</div><div class='row'><span>ENTRY 4130.000 · 4129.355 · 4120.955</span></div><div class='row' style='margin-top:14px'><span>EXIT 4119.835</span></div><div class='pip' id='q2'>+0</div><div class='ar2'>نقطة · اتقفلت ٤:٣٦ العصر</div></div>
<div class='sc' id='s3'><span class='tag'>الصفقة التانية · بيع</span><div class='price' id='p3'>4124.405</div><div class='row'><span>ENTRY 4124.405 → EXIT 4118.615</span></div><div class='pip' id='q3'>+0</div><div class='ar2'>نقطة · اتقفلت ٦:٢٥ المسا</div></div>
<div class='sc' id='s4'><div class='ar'>كل صفقة بتنزل<br><span class='grad'>حتى الخسارة</span></div><div class='ar2' style='margin-top:40px'>تابعنا عشان تشوف الصفقة الجاية 👀</div><div class='ar2' style='color:var(--gold)'>ابعتلنا «ذهب» على إنستجرام</div></div>
<div class='risk'>التداول فيه مخاطرة · النتايج اللي فاتت مش ضمان للي جاي</div>
<script>
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
function vis(id,a,b,t){{const e=document.getElementById(id);let o=0;if(t>=a&&t<b){{o=Math.min(1,(t-a)/0.35,(b-t)/0.35)}}e.style.opacity=o;e.style.transform=`translateY(${{(1-o)*40}}px)`}}
window.R=function(t){{
 vis('s1',0,3.6,t);vis('s2',3.6,8.4,t);vis('s3',8.4,12.4,t);vis('s4',12.4,16.5,t);
 document.getElementById('h1').textContent='+'+Math.round(266*ease((t-0.3)/2));
 let k=ease((t-4.0)/3);document.getElementById('p2').textContent=(4130-10.165*k).toFixed(3);document.getElementById('q2').textContent='+'+Math.round(208*k);
 let m=ease((t-8.8)/2.6);document.getElementById('p3').textContent=(4124.405-5.79*m).toFixed(3);document.getElementById('q3').textContent='+'+Math.round(58*m);
}}
</script></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920}); pg.set_content(html); pg.wait_for_timeout(300)
    for i in range(int(FPS*DUR)):
        pg.evaluate(f"R({i/FPS})"); pg.screenshot(path=str(FR/f'{i:04d}.jpg'),type='jpeg',quality=90)
    b.close()
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',str(FR/'%04d.jpg'),'-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',OUT],check=True)
print(OUT)
