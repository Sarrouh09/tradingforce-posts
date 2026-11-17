from vid import build
big="font-family:'Inter Display';font-weight:800;direction:ltr;line-height:1"
chip=lambda a,i: f"<div id='ch{i}' style='display:flex;justify-content:space-between;align-items:center;padding:26px 40px;margin:16px 0;border-radius:24px;background:#0E2253;border:2px solid #28498F;direction:rtl;opacity:0'><span style='font-size:48px;font-weight:700'>🛡️ خطة مخاطرة</span><span style=\"{big};font-size:64px;color:var(--gold)\">{a}</span></div>"
S=[(0,3,"<div class='ar' style='font-size:90px'>تقدر تبدأ<br>بـ <bdi dir='ltr' class='gold'>$100</bdi> بس؟ 🤔</div>"),
 (3,6,f"<div style='font-size:150px'>✅</div><div class='ar' style='font-size:96px'>أيوه، تقدر</div>"),
 (6,9.5,f"<div class='ar2'>بس إحنا بننصح بـ</div><div style=\"{big};font-size:230px;color:var(--gold)\">$300</div><div class='ar2'>عشان تبدأ براحة 💡</div>"),
 (9.5,14,"<div class='ar' style='font-size:68px;margin-bottom:30px'>ولكل حساب خطة<br><span class='grad'>حسب حجمه</span> 📏</div><div style='width:860px'>"+chip("$100",0)+chip("$300",1)+chip("$1000",2)+"</div>"),
 (14,18,"<div class='ar' style='font-size:76px'>حسابك كام؟<br>اكتبه 👇</div><div class='ar2' style='margin-top:30px'>وهنقولك تبدأ إزاي</div><div class='ar2 gold' style='margin-top:30px;font-size:38px'>ابدأ بفلوس تقدر تستغنى عنها 🤝</div>")]
js="for(let i=0;i<3;i++){const p=ease((t-10.1-i*0.6)/0.4);const c=document.getElementById('ch'+i);c.style.opacity=p;c.style.transform=`translateX(${(1-p)*140}px)`}"
build("account_simple",S,18,js=js,ticks=(10.5,11.1,11.7),hits=(3.05,6.05),mood='major')
print("ok")
