from vid import build
big="font-family:'Inter Display';font-weight:800;direction:ltr;line-height:1"
def bar(i,acc,pct,col,lab):
    return f"""<div style='margin:26px 0;direction:ltr;text-align:left'><div style='display:flex;justify-content:space-between;font-size:44px;font-weight:800'><span>{acc}</span><span style='color:{col}' id='p{i}'>0%</span></div>
<div style='height:46px;border-radius:24px;background:#1B3572;overflow:hidden;margin-top:12px'><div id='b{i}' style='height:100%;width:0%;background:{col};border-radius:24px'></div></div>
<div style='font-size:32px;color:var(--muted);margin-top:8px;direction:rtl;text-align:right'>{lab}</div></div>"""
S=[(0,3,"<div class='ar' style='font-size:86px'>تقدر تبدأ تداول دهب<br>بـ <bdi dir='ltr' class='gold'>$100</bdi> بس؟ 🤔</div>"),
 (3,6,"<div class='ar' style='font-size:96px'>أيوه… بس 👀</div><div class='ar2' style='margin-top:30px'>خلينا نحسبها مع بعض</div>"),
 (6,11,f"<div class='ar2'>أقل لوت</div><div style=\"{big};font-size:190px;color:var(--blue-2)\">0.01</div><div class='ar2'>يعني <bdi dir='ltr'>$0.10</bdi> لكل pip</div><div class='ar2' style='margin-top:40px'>لو وقف الخسارة 200 pip</div><div style=\"{big};font-size:150px;color:var(--loss)\">-$20</div>"),
 (11,16.5,"<div class='ar' style='font-size:60px;margin-bottom:20px'>الـ <bdi dir='ltr'>$20</bdi> دول يعني كام ٪ من حسابك؟</div><div style='width:880px'>"+bar(0,"$100",20,"#F87171","🔴 كتير جداً")+bar(1,"$300",7,"#F5C451","🟡 أحسن")+bar(2,"$1000",2,"#34D399","🟢 مريح")+"</div>"),
 (16.5,20,"<div class='ar' style='font-size:78px'>عشان كده بننصح<br>بـ <bdi dir='ltr' class='gold'>$300</bdi> على الأقل 💡</div><div class='ar2' style='margin-top:30px'>ولكل حساب خطة لوت<br>حسب حجمه 📏</div>"),
 (20,23.5,"<div class='ar' style='font-size:64px'>ابدأ بفلوس<br>تقدر تستغنى عنها 🤝</div><div class='ar' style='font-size:58px;margin-top:40px;color:var(--gold)'>حسابك كام؟ اكتبه 👇</div><div class='ar2' style='margin-top:20px'>وهنقولك اللوت المناسب</div>")]
js="""[[20,0],[7,1],[2,2]].forEach(([v,i])=>{const p=ease((t-11.5-i*0.9)/0.9);document.getElementById('b'+i).style.width=(p*v/20*100)+'%';document.getElementById('p'+i).textContent=(p*v).toFixed(v<10?1:0).replace('.0','')+'%';});"""
build("account_size",S,23.5,risk="محتوى تعليمي · قيمة النقطة ممكن تختلف حسب البروكر · التداول فيه مخاطرة",js=js,ticks=[11.5+i*0.06 for i in range(15)]+[12.4+i*0.08 for i in range(10)]+[13.3+i*0.1 for i in range(6)],hits=(3.05,8.6))
print("ok")
