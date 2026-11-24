import json, base64
from vid import build
d=json.load(open('/home/claude/vo/r1124/durs.json'))
lens=[max(3.4,x+0.8) for x in d]; lens[-1]+=0.6
ST=[0]
for L in lens: ST.append(round(ST[-1]+L,2))
json.dump(ST,open('/home/claude/vo/r1124/starts.json','w'))
b=lambda f,m: f"data:{m};base64,"+base64.b64encode(open(f,'rb').read()).decode()
ana=b('/home/claude/out/analysis1123.png','image/png'); mt=b('/home/claude/clients/mt1123.jpg','image/jpeg')
big="font-family:'Inter Display';font-weight:900;direction:ltr;line-height:1"
S=[
f"<div class='ar' style='font-size:76px'>إمبارح الصبح قلنا… 📉</div><img src='{ana}' id='ana' style='width:720px;margin-top:40px;border-radius:24px;border:3px solid #28498F;box-shadow:0 20px 60px #000b'>",
"<div style='font-size:150px'>⏳</div><div class='ar' style='font-size:84px'>مستنيين <span class='grad'>تأكيد</span></div><div class='ar2' style='margin-top:20px'>مش بندخل عشوائي</div>",
f"<div class='ar' style='font-size:84px'>التأكيد جه ✅</div><div id='sb' style=\"margin-top:60px;width:560px;height:150px;border-radius:30px;background:#DC2626;display:flex;align-items:center;justify-content:center;{big};font-size:72px\">SELL 3686</div>",
f"<div style=\"{big};font-size:200px;color:var(--win);text-shadow:0 0 60px #34D39988\" id='pp'>+0</div><div style=\"{big};font-size:80px;color:var(--win)\">PIPS</div><img src='{mt}' style='width:820px;margin-top:40px;border-radius:22px;border:3px solid #28498F'><div class='ar2' style='font-size:28px;margin-top:10px'>📸 من حسابنا الحقيقي · المبالغ مخفية</div>",
"<div style='font-size:170px'>👑</div><div class='ar' style='font-size:76px'>ودي صفقة واحدة بس<br>من قناة الـ <span class='grad'>VIP</span></div>",
"<div style='font-size:170px'>📲🏠</div><div class='ar' style='font-size:76px'>وإنت في بيتك…<br>متابع السوق من موبايلك</div>",
"<div class='ar' style='font-size:84px'>والنهارده؟</div><div class='ar' style='font-size:96px;margin-top:20px'><span class='grad'>خليك جاهز</span> 🔥</div><div class='ar' style='font-size:60px;margin-top:50px;color:var(--gold)'>تابعنا وفعّل الإشعارات 🔔</div>"]
sc=[(ST[i],ST[i+1],x) for i,x in enumerate(S)]
js=f"""const ST={ST};
{{const a=document.getElementById('ana');const p=Math.min(1,t/ST[1]);a.style.transform=`scale(${{1+p*0.08}})`;}}
{{const s=document.getElementById('sb');const tp=ST[2]+1.4;if(t>tp){{s.style.transform=`scale(${{t<tp+0.25?0.92:1}})`;}}}}
{{const e=document.getElementById('pp');e.textContent='+'+Math.round(184*ease((t-ST[3]-0.2)/1.6));}}"""
build("recap1124",sc,ST[-1],risk="النتايج اللي فاتت مش ضمان للي جاي · التداول فيه مخاطرة · مش نصيحة مالية",js=js,
 ticks=[ST[3]+0.2+i*0.08 for i in range(20)],hits=(ST[1],ST[2]+1.4,ST[3]+1.8),mood='major')
print(ST)
