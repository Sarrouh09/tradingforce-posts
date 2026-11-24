import json
from vid import build
lens=[3.2,3.2,3.2,3.2,3.2,4.6,3.2]
ST=[0]
for L in lens: ST.append(round(ST[-1]+L,2))
json.dump(ST,open('/home/claude/out/why_st.json','w'))
IF="font-family:'Inter Display','Inter',sans-serif"
big=f"{IF};font-weight:900;direction:ltr;line-height:1"
P=lambda p: round((4200-p)/700*620,1)
pts=[(0,4150),(60,4110),(110,4130),(170,4060),(220,4085),(290,3990),(340,4010),(410,3900),(460,3925),(530,3800),(580,3830),(650,3690),(700,3720),(780,3530)]
S0=f"""<div class='ar' style='font-size:84px'>ليه الدهب نزل <span style='color:var(--loss)'>كده</span>؟ 📉</div>
<svg width='820' height='640' viewBox='0 0 820 640' style='margin-top:30px;direction:ltr'><polyline id='dl' points='' fill='none' stroke='#F87171' stroke-width='9' stroke-linejoin='round' stroke-linecap='round'/></svg>
<div style="{big};font-size:64px;color:#cfe0ff"><span>4150</span> → <span style='color:var(--loss)' id='px'>4150</span></div><div class='ar2' style='font-size:34px;margin-top:10px'>في أقل من ٣ أسابيع</div>"""
card=lambda n,e,t,s: f"""<div style="{big};font-size:110px;color:var(--gold)">{n}</div><div style='font-size:150px;margin-top:10px'>{e}</div><div class='ar' style='font-size:74px;margin-top:10px'>{t}</div><div class='ar2' style='font-size:42px;margin-top:20px'>{s}</div>"""
S1=card('01','🏦','الفيدرالي الأمريكي','توقعات إن الفايدة تفضل عالية أو تزيد<br>= ضغط على الدهب')
S2=card('02','💵','الدولار قوي','أعلى مستوى من حوالي سنة ونص<br>والدهب بيتسعّر بالدولار')
S3=card('03','🔥','التضخم','أرقام أعلى من المتوقع<br>خلّت السوق يتوقع فايدة أعلى')
S4=card('04','📤','فلوس خارجة من صناديق الدهب','بيع من صناديق الـ ETF<br>زوّد الضغط على السعر')
row=lambda d,t,i: f"<div id='r{i}' style='display:flex;justify-content:space-between;align-items:center;padding:26px 36px;margin:14px 0;border-radius:24px;background:#0E2253;border:2px solid #28498F;direction:rtl;opacity:0'><span class='ar' style='font-size:46px'>{t}</span><span style=\"{big};font-size:50px;color:var(--gold)\">{d}</span></div>"
S5=f"""<div class='ar' style='font-size:84px'>ديسمبر جاي <span style='color:var(--loss)'>سخن</span> 🔥</div><div style='width:860px;margin-top:40px'>{row('8–9 DEC','🏦 اجتماع الفيدرالي',0)}{row('10 DEC','🔥 أرقام التضخم CPI',1)}</div>
<div class='ar2' style='font-size:44px;margin-top:40px'>حركات قوية ممكنة… <b style='color:var(--fg)'>في الاتجاهين</b> ⚡</div>"""
S6="""<div class='ar' style='font-size:80px'>خليك جاهز 💪</div><div class='ar2' style='font-size:46px;margin-top:24px'>وإحنا هنتابعها معاك خطوة بخطوة 📊</div><div class='ar' style='font-size:64px;margin-top:60px;color:var(--gold)'>تابعنا وفعّل الإشعارات 🔔</div>"""
S=[S0,S1,S2,S3,S4,S5,S6]
sc=[(ST[i],ST[i+1],x) for i,x in enumerate(S)]
js=f"""const ST={ST};const D={json.dumps([(x,P(v)) for x,v in pts])};const V={json.dumps([v for x,v in pts])};
{{const k=Math.max(0,Math.min(1,(t-0.2)/2.4));const n=Math.max(1,Math.floor(k*(D.length-1))+1);const fr=k*(D.length-1)-(n-1);let ps=D.slice(0,n);
if(n<D.length){{const a=D[n-1],b=D[n];ps=ps.concat([[a[0]+(b[0]-a[0])*fr,a[1]+(b[1]-a[1])*fr]]);}}
const e=document.getElementById('dl');if(e)e.setAttribute('points',ps.map(p=>p.join(',')).join(' '));
const x=document.getElementById('px');if(x)x.textContent=Math.round(4150-(4150-3530)*k);}}
for(let i=0;i<2;i++){{const r=document.getElementById('r'+i);if(r){{const p=ease((t-ST[5]-0.6-i*0.6)/0.3);r.style.opacity=p;r.style.transform=`translateX(${{(1-p)*-120}}px)`;}}}}"""
build("why_drop",sc,ST[-1],risk="محتوى تعليمي · مش توقع مضمون · التداول فيه مخاطرة",js=js,ticks=[0.2+i*0.12 for i in range(20)],hits=(ST[1],ST[2],ST[3],ST[4],ST[5]),mood='minor')
print(ST)
