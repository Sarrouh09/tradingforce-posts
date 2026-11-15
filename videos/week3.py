from vid import build
big="font-family:'Inter Display';font-weight:800;direction:ltr;line-height:1"
def n(v,c,s=200,i=""): return f"<div style=\"{big};font-size:{s}px;color:var(--{c})\" {('id='+repr(i)) if i else ''}>{v}</div>"
# 1) No stop loss
path="M40,60 L120,90 L180,70 L260,160 L320,140 L400,260 L460,230 L540,360 L600,340 L680,470 L760,450 L860,560"
svg=f"""<svg width='900' height='620' viewBox='0 0 900 620' style='margin-top:30px'>
<line x1='0' y1='60' x2='900' y2='60' stroke='#60A5FA' stroke-dasharray='10 10' stroke-width='3'/>
<text x='10' y='45' fill='#60A5FA' font-size='30' font-family='DejaVu Sans'>Entry</text>
<path id='pp' d='{path}' fill='none' stroke='#F87171' stroke-width='10' stroke-linecap='round' stroke-linejoin='round' stroke-dasharray='1400' stroke-dashoffset='1400'/></svg>"""
A=[(0,3,"<div class='ar' style='font-size:86px'>الغلطة دي<br><span style='color:var(--loss)'>مسحت حسابات كتير</span> 🚨</div>"),
 (3,9,f"<div class='ar2'>دخلت صفقة من غير وقف خسارة…</div>{svg}<div style=\"{big};font-size:150px;color:var(--loss)\" id='dd'>0 pips</div>"),
 (9,12.5,"<div class='ar' style='font-size:74px'>وتقول «هيرجع» 🙏</div><div class='ar2' style='margin-top:26px'>وهو مبيرجعش… والحساب بيخلص</div>"),
 (12.5,16.5,f"<div class='ar2'>الحل؟ وقف الخسارة<br>يتحط <b style='color:var(--gold)'>قبل</b> ما تدخل</div>{n('30 pips','gold',190)}<div class='ar2'>خسارة صغيرة ومعروفة من الأول ✅</div>"),
 (16.5,20,"<div class='ar' style='font-size:70px'>اكتب «وقف» 👇<br>لو كنت بتتداول من غيره 👀</div><div class='ar2 gold' style='margin-top:26px'>احفظ الفيديو 📌 وتابعنا 🔔</div>")]
build("no_stop_loss",A,20,js="var p=Math.max(0,Math.min(1,(t-3.3)/5));document.getElementById('pp').style.strokeDashoffset=1400*(1-p);document.getElementById('dd').textContent='-'+Math.round(850*ease((t-3.3)/5))+' pips';",ticks=[3.3+i*0.12 for i in range(42)],hits=(3.0,12.6))
# 2) News at 15:30
B=[(0,3,"<div class='ar' style='font-size:84px'>ليه الدهب بيتجنن<br>الساعة <span class='grad'>٣:٣٠</span>؟ 🤯</div>"),
 (3,7,f"<div class='ar2'>أخبار أمريكا بتنزل الساعة</div>{n('15:30','blue-2',210)}<div class='ar2'>بتوقيت القاهرة</div>"),
 (7,11,f"<div class='ar2'>في ثواني الدهب ممكن يتحرك</div>{n('+0','gold',210,'mv')}<div class='ar2'>في أي اتجاه ⚡</div>"),
 (11,16,"<div class='ar' style='font-size:66px'>٣ قواعد وقت الخبر</div><div class='ar2' style='margin-top:30px;line-height:1.9'>١. متدخلش قبل الخبر بدقيقتين ⏳<br>٢. استنى أول شمعة تقفل 🕯️<br>٣. لوت أصغر من العادي 📉</div>"),
 (16,20,"<div class='ar' style='font-size:68px'>تابعنا 🔔<br>بنفكرك قبل كل خبر</div><div class='ar2 gold' style='margin-top:26px'>ابعت الفيديو لصاحبك اللي بيدخل وقت الأخبار 😅</div>")]
build("news_330",B,20,js="document.getElementById('mv').textContent='+'+Math.round(300*ease((t-7.2)/1.4))+' pips';",ticks=[7.2+i*0.07 for i in range(20)],hits=(7.1,11.1),mood='major')
# 3) What is a pip
C=[(0,3,"<div class='ar' style='font-size:90px'>يعني إيه <span class='grad'>pip</span>؟ 🤔</div><div class='ar2' style='margin-top:26px'>في ١٥ ثانية</div>"),
 (3,7.5,f"<div class='ar2'>الدهب كان</div>{n('3900.00','fg',170)}<div class='ar2' style='margin-top:20px'>وطلع</div>{n('3900.00','win',170,'px')}"),
 (7.5,11.5,f"<div class='ar2'>دولار واحد في السعر =</div>{n('10 pips','gold',220)}<div class='ar2'>كل 0.10 = pip واحد</div>"),
 (11.5,15.5,f"<div class='ar2'>وعلى لوت 0.01</div>{n('$0.10','blue-2',200)}<div class='ar2'>لكل pip</div>"),
 (15.5,19,"<div class='ar' style='font-size:72px'>اكتب «فهمت» 👇</div><div class='ar2 gold' style='margin-top:26px'>واحفظه 📌 الدرس الجاي: حجم اللوت</div>")]
build("what_is_pip",C,19,risk="محتوى تعليمي · قيمة النقطة ممكن تختلف حسب البروكر",js="document.getElementById('px').textContent=(3900+ease((t-5)/1.5)).toFixed(2);",ticks=[5+i*0.08 for i in range(18)],hits=(7.6,))
# 4) 3 questions before Buy
D=[(0,3,"<div class='ar' style='font-size:84px'>قبل ما تدوس <span style='color:var(--win)'>BUY</span><br>اسأل نفسك ٣ أسئلة ✋</div>"),
 (3,6.5,"<div style=\"font-family:'Inter Display';font-weight:800;font-size:160px;color:var(--gold)\">1</div><div class='ar' style='font-size:76px'>وقف الخسارة فين؟ 🛑</div><div class='ar2'>لو مش عارف… متدخلش</div>"),
 (6.5,10,"<div style=\"font-family:'Inter Display';font-weight:800;font-size:160px;color:var(--gold)\">2</div><div class='ar' style='font-size:76px'>بخاطر بكام ٪؟ ⚖️</div><div class='ar2'>١–٢٪ من الحساب بالكتير</div>"),
 (10,13.5,"<div style=\"font-family:'Inter Display';font-weight:800;font-size:160px;color:var(--gold)\">3</div><div class='ar' style='font-size:76px'>فيه خبر قريب؟ 📰</div><div class='ar2'>شوف الأجندة الاقتصادية الأول</div>"),
 (13.5,17,"<div class='ar' style='font-size:72px'>٣ أسئلة بس…<br><span class='grad'>بيحموا حسابك</span> 🛡️</div>"),
 (17,20.5,"<div class='ar' style='font-size:66px'>ابعته لصاحبك اللي<br>بيدخل عشوائي 😅</div><div class='ar2 gold' style='margin-top:26px'>احفظ 📌 · تابع 🔔 · اكتب سؤالك 👇</div>")]
build("three_questions",D,20.5,hits=(3.05,6.55,10.05),mood='major')
print("ok")
