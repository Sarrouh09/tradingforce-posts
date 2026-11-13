import sys; sys.path.insert(0,'/home/claude/postgen'); sys.path.insert(0,'/home/claude/video')
from vid import build, LOGO
logo=f"<img src='{LOGO}' style='width:240px;height:240px;border-radius:50%;box-shadow:0 0 90px color-mix(in srgb,var(--blue) 60%,transparent);margin-bottom:50px'>"
card="""<div style='margin-top:50px;width:820px;padding:36px 40px;border-radius:26px;border:1px solid var(--line-2);background:linear-gradient(180deg,color-mix(in srgb,var(--panel-2) 80%,transparent),color-mix(in srgb,var(--panel) 70%,transparent));direction:ltr;text-align:left'>
<div style='display:flex;justify-content:space-between;align-items:center'><span style="font-family:'Inter Display';font-weight:800;font-size:46px">XAU/USD</span><span style='color:var(--loss);border:2px solid var(--loss);padding:8px 22px;border-radius:999px;font-weight:800;font-size:28px'>SELL</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-top:26px;font-family:'DejaVu Sans Mono';font-size:34px;font-weight:700">
<div><div style='font-size:20px;color:var(--muted);font-family:Inter'>ENTRY</div>4030</div><div><div style='font-size:20px;color:var(--muted);font-family:Inter'>STOP LOSS</div><span style='color:var(--loss)'>4055</span></div><div><div style='font-size:20px;color:var(--muted);font-family:Inter'>TAKE PROFIT</div><span style='color:var(--win)'>3980</span></div></div></div>"""
pill=lambda t,c="var(--win)":f"<div style='margin-top:22px;direction:rtl;font-size:46px;font-weight:700;padding:18px 34px;border-radius:18px;border:1px solid var(--line-2);background:color-mix(in srgb,var(--panel) 60%,transparent)'><span style='color:{c}'>✓</span> {t}</div>"
scenes=[
 (0,3.4,"<div class='ar' style='font-size:96px'>ليه بنوريك<br><span class='grad'>صفقاتنا الخسرانة؟</span></div><div class='ar2' style='margin-top:30px'>استنى للآخر 👇</div>"),
 (3.4,7.4,logo+"<div class='ar'>Trading Force</div><div class='ar2' style='margin-top:20px'>بنتداول حاجة واحدة بس:<br><span class='gold' style='font-weight:700'>الدهب XAU/USD</span></div>"),
 (7.4,12,"<div class='ar'>كل صفقة واضحة<br><span class='grad'>من أول ثانية</span></div>"+card+"<div class='ar2' style='margin-top:30px'>دخول · وقف خسارة · هدف</div>"),
 (12,16.4,"<div class='ar'>شفافية كاملة</div>"+pill("الدخول بينزل لايف قبل النتيجة")+pill("كل نتيجة بتنزل، مكسب أو خسارة")+pill("ملخص أسبوعي بأرقام حقيقية")),
 (16.4,20.6,"<div class='ar2'>يوم الإتنين ٩ نوفمبر</div><div style=\"font-family:'Inter Display';font-weight:800;font-size:220px;color:var(--win);direction:ltr;line-height:1;text-shadow:0 0 80px color-mix(in srgb,var(--win) 40%,transparent)\" id='cnt'>+0</div><div class='ar2'>نقطة في صفقتين بيع</div><div class='ar2' style='margin-top:20px;font-size:38px'>ولما نخسر، هتشوف الخسارة بنفس الشكل</div>"),
 (20.6,24.8,"<div class='ar'>أمانك أولاً 🔒</div>"+pill("عمرنا ما هنكلمك الأول","var(--gold)")+pill("الدفع من الموقع بس","var(--gold)")+pill("حساباتكم أهم من أي صفقة","var(--gold)")),
 (24.8,31,logo.replace('240px','180px')+"<div class='ar'>صفقات الدهب لايف<br><span class='grad'>على تيليجرام</span></div><div class='ar2' style='margin-top:24px'>VIP بـ <span class='gold' style='font-weight:800'>30$</span> في الشهر · اللينك في البايو</div><div class='ar2'>تابعنا 🔔 وابعتلنا <span class='gold'>«ذهب»</span></div>")]
js="const c=document.getElementById('cnt');c.textContent='+'+Math.round(266*ease((t-16.8)/2));"
print(build("brand_who_we_are_v2",scenes,31,risk="التداول فيه مخاطرة · النتايج اللي فاتت مش ضمان للي جاي",js=js))
