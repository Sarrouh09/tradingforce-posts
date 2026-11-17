from vid import build
import random
random.seed(3)
words=["RSI","MACD","Fibonacci","CPI","NFP","Support","Resistance","ICT","FVG","Order Block","Trendline","الساعة ٣ الفجر ☕","خبر!! 📰","EMA 200","Liquidity","Spread","Lot size؟","SL فين؟"]
fl="".join(f"<div class='fw' id='w{i}' style='position:absolute;left:{random.randint(40,760)}px;top:{random.randint(560,1450)}px;font-size:{random.randint(34,58)}px;font-weight:800;color:{random.choice(['#F87171','#FCA5A5','#9CB0DA','#F5C451','#60A5FA'])};white-space:nowrap'>{w}</div>" for i,w in enumerate(words))
S0=f"""<div style='position:absolute;top:250px;left:0;right:0' class='ar'><span style='font-size:84px'>بتعمل ده كله<br><span style='color:var(--loss)'>لوحدك؟</span> 🤯</span></div>{fl}
<div style='position:absolute;bottom:250px;left:140px;right:140px;direction:rtl'><div class='ar2' style='font-size:36px;text-align:right'>مستوى التوتر</div>
<div style='height:34px;border-radius:20px;background:#1B3572;overflow:hidden;margin-top:10px'><div id='stress' style='height:100%;width:0%;background:linear-gradient(90deg,#F5C451,#F87171)'></div></div></div>"""
S1="<div class='ar' style='font-size:140px'>✋</div><div class='ar' style='font-size:96px'>استنى…</div>"
items=[("تحليل السوق","📊"),("متابعة الأخبار","📰"),("حساب المخاطرة","⚖️"),("وقف الخسارة","🛑"),("الهدف","🎯")]
chk="".join(f"<div id='c{i}' style='display:flex;justify-content:space-between;align-items:center;direction:rtl;padding:26px 40px;margin:14px 0;border-radius:24px;background:#0E2253;border:2px solid #28498F;font-size:52px;font-weight:700;opacity:0'><span>{e} {t}</span><span id='k{i}' style='color:var(--win);font-size:60px'>✓</span></div>" for i,(t,e) in enumerate(items))
S2=f"<div class='ar' style='font-size:76px;margin-bottom:40px'>خلّي الشغل التقيل<br><span class='grad'>علينا</span> 💪</div><div style='width:860px'>{chk}</div>"
phone=f"""<div style='width:620px;height:1000px;border-radius:70px;border:10px solid #28498F;background:#050c22;position:relative;overflow:hidden;box-shadow:0 30px 90px #000c'>
<div style='position:absolute;top:22px;left:50%;transform:translateX(-50%);width:170px;height:34px;border-radius:20px;background:#13295F'></div>
<div style='position:absolute;top:120px;left:0;right:0;text-align:center;font-family:Inter Display;font-size:110px;font-weight:300;color:#9CB0DA'>15:31</div>
<div id='notif' style='position:absolute;top:330px;left:26px;right:26px;border-radius:34px;background:#13295Fee;border:2px solid #3B82F6;padding:30px;text-align:right;direction:rtl'>
<div style='font-size:30px;color:#9CB0DA'>🔔 Trading Force · الآن</div>
<div style='font-size:44px;font-weight:800;margin-top:10px'>صفقة جديدة 📍</div>
<div style='direction:ltr;text-align:left;margin-top:20px;font-family:Inter Display;font-weight:800;font-size:40px;line-height:1.6'><span style='color:#F87171'>SELL</span> 3925<br><span style='color:#FCA5A5'>SL</span> 3960 · <span style='color:#34D399'>TP</span> 3800</div></div>
<div id='btn' style='position:absolute;bottom:120px;left:70px;right:70px;height:130px;border-radius:30px;background:#DC2626;display:flex;align-items:center;justify-content:center;font-family:Inter Display;font-weight:800;font-size:56px'>SELL</div>
<div id='rip' style='position:absolute;bottom:155px;left:50%;width:60px;height:60px;margin-left:-30px;border-radius:50%;background:#ffffff88;opacity:0'></div></div>"""
S3=f"<div class='ar' style='font-size:66px;margin-bottom:34px'>وإنت بتوصلك <span class='grad'>خطة واضحة</span> 📲</div>{phone}"
S4=f"<div class='ar' style='font-size:66px;margin-bottom:34px' id='s4t'>وإنت تقرر… وتدوس 👆</div>{phone.replace('notif','notif2').replace('btn','btn2').replace('rip','rip2')}"
S5="<div class='ar' style='font-size:82px'>ومش كل صفقة<br>بتكسب 🤝</div><div class='ar2' style='margin-top:36px'>عشان كده وقف الخسارة<br>موجود في كل صفقة،<br>والقرار دايماً <b style='color:var(--gold)'>في إيدك</b></div>"
S6="<div class='ar' style='font-size:70px'>عايز تعرف<br>بيشتغل إزاي؟ 🤔</div><div class='ar' style='font-size:80px;margin-top:40px;color:var(--gold)'>اكتب «إزاي» 👇</div><div class='ar2' style='margin-top:30px'>في الكومنتات وهنرد عليك</div><div class='ar2' style='margin-top:20px'>وتابعنا 🔔</div>"
ST=[0, 6.55, 7.86, 15.61, 19.41, 23.21, 31.06, 38.66]
sc=[(ST[i],ST[i+1],x) for i,x in enumerate([S0,S1,S2,S3,S4,S5,S6])]
js="""const ST=[0, 6.55, 7.86, 15.61, 19.41, 23.21, 31.06, 38.66];
if(t<ST[1]){for(let i=0;i<18;i++){const e=document.getElementById('w'+i);const k=Math.min(1,t/(ST[1]-0.4));
e.style.transform=`translate(${Math.sin(t*(2+i%5)+i)*k*60}px,${Math.cos(t*(3+i%4)+i*2)*k*50}px) rotate(${Math.sin(t*4+i)*k*14}deg)`;
e.style.opacity=Math.min(1,Math.max(0,(t-i*0.28)/0.3));}
document.getElementById('stress').style.width=(Math.min(1,t/(ST[1]-0.3))*100)+'%';}
for(let i=0;i<5;i++){const c=document.getElementById('c'+i);const a=ST[2]+1.6+i*1.05;const p=ease((t-a)/0.35);c.style.opacity=p;c.style.transform=`translateX(${(1-p)*-120}px)`;
document.getElementById('k'+i).style.opacity=t>a+0.35?1:0;}
{const n=document.getElementById('notif');const p=ease((t-ST[3]-0.3)/0.5);n.style.transform=`translateY(${(1-p)*-500}px)`;}
{const n=document.getElementById('notif2');n.style.transform='none';const r=document.getElementById('rip2');const b=document.getElementById('btn2');
const tp=ST[4]+1.9;if(t>tp&&t<tp+0.6){const q=(t-tp)/0.6;r.style.opacity=1-q;r.style.transform=`scale(${1+q*6})`}else r.style.opacity=0;
if(t>tp+0.15){b.style.background='#059669';b.textContent='✓ تم الدخول'}else{b.style.background='#DC2626';b.textContent='SELL'}}
"""
build("we_do_the_work_vo",sc,ST[-1],risk="التداول فيه مخاطرة · النتايج مش مضمونة · مش نصيحة مالية",js=js,
 ticks=[ST[2]+1.95+i*1.05 for i in range(5)],hits=(ST[1],ST[3]+0.3,ST[4]+1.9),mood='major')
print("ok")
