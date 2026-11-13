from vid import build
big="font-family:'Inter Display';font-weight:800;direction:ltr;line-height:1"
# A) Lot size
A=[(0,3,"<div class='ar' style='font-size:88px'>أغلب الناس بتخسر<br><span style='color:var(--loss)'>بسبب الرقم ده</span> 👇</div><div class='ar2' style='margin-top:30px'>حجم اللوت</div>"),
 (3,6.5,f"<div class='ar2'>حسابك</div><div style=\"{big};font-size:200px;color:var(--blue-2)\" id='acc'>$0</div>"),
 (6.5,10,f"<div class='ar2'>خاطر بـ <b style='color:var(--gold)'>١٪</b> بس في الصفقة</div><div style=\"{big};font-size:200px;color:var(--gold)\">$5</div><div class='ar2'>مش أكتر</div>"),
 (10,13.5,f"<div class='ar2'>وقف الخسارة</div><div style=\"{big};font-size:180px;color:var(--loss)\">50 pips</div><div class='ar2'>كل 0.01 لوت = $0.10 للنقطة على الدهب</div>"),
 (13.5,17.5,f"<div class='ar2'>يبقى حجم اللوت</div><div style=\"{big};font-size:220px;color:var(--win)\">0.01</div><div class='ar2' style='font-size:36px'>50 × $0.10 = $5 ✅</div>"),
 (17.5,21,"<div class='ar' style='font-size:76px'>احفظ الفيديو 📌</div><div class='ar2' style='margin-top:26px'>وابعته لصاحبك اللي بيدخل بلوت كبير 😅</div><div class='ar2 gold'>تابعنا 🔔 لدروس الدهب كل يوم</div>")]
build("lot_size",A,21,risk="محتوى تعليمي · قيمة النقطة ممكن تختلف حسب البروكر",js="document.getElementById('acc').textContent='$'+Math.round(500*ease((t-3.2)/1.5));",ticks=[3.2+i*0.07 for i in range(21)],hits=(4.8,13.6))
# B) Risk reward
B=[(0,3.2,"<div class='ar' style='font-size:84px'>ممكن تخسر ٦ صفقات<br>من ١٠… <span class='grad'>وتكسب؟</span> 🤯</div>"),
 (3.2,7,"<div class='ar'>السر في<br><span class='grad'>المخاطرة للعائد</span></div><div style=\"font-family:'Inter Display';font-weight:800;font-size:170px;color:var(--gold);direction:ltr;margin-top:30px\">1 : 2</div><div class='ar2'>بتخاطر بـ $10 عشان تكسب $20</div>"),
 (7,11,"<div class='ar2'>٦ صفقات خسرانة</div><div style=\"font-family:'Inter Display';font-weight:800;font-size:170px;color:var(--loss);direction:ltr\" id='l'>-$0</div><div class='ar2'>٦ × $10</div>"),
 (11,15,"<div class='ar2'>٤ صفقات كسبانة</div><div style=\"font-family:'Inter Display';font-weight:800;font-size:170px;color:var(--win);direction:ltr\" id='w'>+$0</div><div class='ar2'>٤ × $20</div>"),
 (15,18.5,"<div class='ar2'>النتيجة</div><div style=\"font-family:'Inter Display';font-weight:800;font-size:220px;color:var(--win);direction:ltr\">+$20</div><div class='ar2'>رغم إنك خسرت أكتر من نص الصفقات</div>"),
 (18.5,22,"<div class='ar' style='font-size:72px'>عشان كده كل صفقاتنا<br><span class='grad'>بنسبة واضحة</span></div><div class='ar2 gold' style='margin-top:26px'>اكتب «فهمت» لو الفكرة وصلتلك 👇</div>")]
build("risk_reward",B,22,js="document.getElementById('l').textContent='-$'+Math.round(60*ease((t-7.3)/1.6));document.getElementById('w').textContent='+$'+Math.round(80*ease((t-11.3)/1.6));",ticks=[7.3+i*0.08 for i in range(20)]+[11.3+i*0.08 for i in range(20)],hits=(15.1,),mood='major')
print("ok")
