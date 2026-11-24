import json
from vid import build
d=json.load(open('/home/claude/vo/journey/durs.json'))
mins=[5.0,7.4,7.6,5.4,5.6,3.4,7.0]
lens=[max(mins[i],d[i]+0.8) for i in range(7)]
ST=[0]
for L in lens: ST.append(round(ST[-1]+L,2))
json.dump(ST,open('/home/claude/vo/journey/starts.json','w'))
IF="font-family:'Inter Display','Inter',sans-serif"
def phone(inner,bg='#050c22'):
    return f"""<div style="width:740px;height:1440px;border-radius:90px;border:12px solid #2a3f73;background:{bg};position:relative;overflow:hidden;box-shadow:0 40px 120px #000d;direction:ltr;text-align:left">
<div style="position:absolute;top:22px;left:50%;transform:translateX(-50%);width:200px;height:40px;border-radius:24px;background:#000;z-index:5"></div>
<div style="position:absolute;top:26px;left:60px;{IF};font-weight:700;font-size:30px;color:#fff;z-index:4">15:31</div>{inner}</div>"""
LBL="<div class='ar2' style='font-size:30px;margin-top:22px;color:var(--gold)'>مثال توضيحي 🎬</div>"
# S0 lock screen + notification
s0=phone(f"""<div style="position:absolute;top:220px;width:100%;text-align:center;{IF};font-size:150px;font-weight:300;color:#cfe0ff">15:31</div>
<div style="position:absolute;top:400px;width:100%;text-align:center;{IF};font-size:34px;color:#9CB0DA">Tuesday, 24 November</div>
<div id="nt" style="position:absolute;top:560px;left:34px;right:34px;border-radius:40px;background:#1b2b55ee;padding:30px 34px;border:2px solid #3B82F6">
<div style="display:flex;align-items:center;gap:18px"><div style="width:64px;height:64px;border-radius:18px;background:linear-gradient(135deg,#3B82F6,#06B6D4);display:flex;align-items:center;justify-content:center;{IF};font-weight:900;font-size:30px;color:#fff">TF</div>
<div style="{IF};font-size:30px;color:#cfe0ff;font-weight:700">TRADING FORCE VIP <span style="color:#9CB0DA;font-weight:400">· now</span></div></div>
<div style="{IF};font-size:40px;font-weight:800;color:#fff;margin-top:18px">🔔 New trade: SELL LIMIT</div>
<div style="{IF};font-size:32px;color:#cfe0ff;margin-top:8px">Tap to view entry, stop loss & target</div></div>""","linear-gradient(180deg,#0b1a44,#050c22)")
# S1 chat
msg=lambda t,i: f"""<div id="m{i}" style="margin:14px 0;max-width:560px;border-radius:28px;background:#1e2d57;padding:22px 28px;{IF};font-size:40px;color:#fff;opacity:0">{t}</div>"""
s1=phone(f"""<div style="position:absolute;top:80px;left:0;right:0;height:120px;background:#0e1a3a;display:flex;align-items:center;gap:20px;padding:0 40px;border-bottom:2px solid #1e2d57">
<div style="width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,#3B82F6,#06B6D4);display:flex;align-items:center;justify-content:center;{IF};font-weight:900;color:#fff;font-size:30px">TF</div>
<div style="{IF};font-size:38px;font-weight:800;color:#fff">Trading Force VIP</div></div>
<div style="position:absolute;top:240px;left:40px;right:40px">
<div style="color:#a78bfa;{IF};font-size:30px;font-weight:700">Trading Force VIP</div>
{msg('🔻 <b>SELL LIMIT 3650</b>',0)}{msg('🛑 Stop loss <b>3680</b>',1)}{msg('🎯 Take profit <b>3630</b>',2)}{msg('Lot: <b>0.01</b> per $300 💡',3)}</div>""")
# S2 order ticket
fld=lambda lab,val,i: f"""<div style="display:flex;justify-content:space-between;align-items:center;padding:28px 34px;border-bottom:2px solid #1e2d57;{IF};font-size:40px"><span style="color:#9CB0DA">{lab}</span><span id="f{i}" style="color:#fff;font-weight:800" data-v="{val}"></span></div>"""
s2=phone(f"""<div style="position:absolute;top:110px;left:0;right:0;text-align:center;{IF};font-size:40px;font-weight:800;color:#fff">XAU/USD · New Order</div>
<div style="position:absolute;top:200px;left:30px;right:30px;border-radius:30px;background:#0e1a3a;border:2px solid #1e2d57">
{fld('Type','Sell Limit',0)}{fld('Volume','0.01',1)}{fld('Price','3650.00',2)}{fld('Stop Loss','3680.00',3)}{fld('Take Profit','3630.00',4)}</div>
<div id="pb" style="position:absolute;bottom:160px;left:60px;right:60px;height:140px;border-radius:34px;background:#DC2626;display:flex;align-items:center;justify-content:center;{IF};font-weight:900;font-size:54px;color:#fff">PLACE SELL LIMIT</div>
<div id="rp" style="position:absolute;bottom:200px;left:50%;width:70px;height:70px;margin-left:-35px;border-radius:50%;background:#ffffff99;opacity:0"></div>""")
# S3/S4 chart
CH=lambda pid,cid,extra: phone(f"""<div style="position:absolute;top:110px;left:0;right:0;text-align:center;{IF};font-size:38px;font-weight:800;color:#fff">XAU/USD · M5</div>
<svg width="716" height="900" viewBox="0 0 716 900" style="position:absolute;top:220px;left:0">
<line x1="0" y1="129" x2="716" y2="129" stroke="#F87171" stroke-width="3" stroke-dasharray="12 10"/><text x="10" y="116" fill="#F87171" font-size="28" font-weight="800" font-family="Inter">SL 3680</text>
<line x1="0" y1="514" x2="716" y2="514" stroke="#F5C451" stroke-width="3" stroke-dasharray="12 10"/><text x="10" y="501" fill="#F5C451" font-size="28" font-weight="800" font-family="Inter">SELL LIMIT 3650</text>
<line x1="0" y1="771" x2="716" y2="771" stroke="#34D399" stroke-width="3" stroke-dasharray="12 10"/><text x="10" y="758" fill="#34D399" font-size="28" font-weight="800" font-family="Inter">TP 3630</text>
<polyline id="{pid}" points="" fill="none" stroke="#EEF3FF" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
<circle id="{cid}" r="14" fill="#06B6D4"/></svg>{extra}""")
s3=CH('pl3','dt3',"""<div id="fl" style="position:absolute;top:1160px;left:40px;right:40px;border-radius:30px;background:#065F46;padding:26px;text-align:center;font-family:Inter;font-weight:800;font-size:38px;color:#A7F3D0;opacity:0">✅ ORDER FILLED · SELL 3650</div>""")
s4=CH('pl4','dt4',f"""<div style="position:absolute;top:1150px;left:0;right:0;text-align:center"><span id="pp" style="{IF};font-weight:900;font-size:110px;color:#34D399">+0</span><span style="{IF};font-weight:900;font-size:50px;color:#34D399"> pips</span></div>""")
s5=f"""<div style="font-size:200px">🎯</div><div style="{IF};font-weight:900;font-size:150px;color:var(--win);direction:ltr;text-shadow:0 0 60px #34D39988">TP HIT</div><div style="{IF};font-weight:900;font-size:120px;color:var(--win);direction:ltr">+200 pips</div>{LBL}"""
s6="""<div class='ar' style='font-size:80px'>من الإشعار 🔔<br>للإغلاق ✅</div><div class='ar2' style='font-size:44px;margin-top:30px'>كل الحسابات جاهزة… والقرار في إيدك 👆</div><div class='ar' style='font-size:62px;margin-top:60px;color:var(--gold)'>تابعنا وفعّل الإشعارات 🔔</div>"""
S=[s0,s1,s2,s3,s4,s5,s6]
sc=[(ST[i],ST[i+1],x) for i,x in enumerate(S)]
# price path: y = (3690-p)/70*900
P=lambda p: round((3690-p)/70*900,1)
rise=[3635,3638,3636,3641,3639,3644,3642,3647,3645,3650.5]
fall=[3650.5,3646,3648,3641,3644,3637,3639,3633,3635,3630]
pts_r=[(i*40, P(v)) for i,v in enumerate(rise)]
pts_f=[(360+i*36, P(v)) for i,v in enumerate(fall)]
js=f"""const ST={ST};const R={json.dumps(pts_r)};const F={json.dumps(pts_f)};
function draw(pl,dt,arr,k){{const n=Math.max(1,Math.floor(k*(arr.length-1))+1);const fr=k*(arr.length-1)-(n-1);let ps=arr.slice(0,n);
if(n<arr.length){{const a=arr[n-1],b=arr[n];ps=ps.concat([[a[0]+(b[0]-a[0])*fr,a[1]+(b[1]-a[1])*fr]]);}}
const e=document.getElementById(pl);if(e)e.setAttribute('points',ps.map(p=>p.join(',')).join(' '));const l=ps[ps.length-1];const c=document.getElementById(dt);if(c){{c.setAttribute('cx',l[0]);c.setAttribute('cy',l[1]);}}}}
{{const n=document.getElementById('nt');const p=ease((t-0.6)/0.6);n.style.transform=`translateY(${{(1-p)*-700}}px)`;}}
for(let i=0;i<4;i++){{const m=document.getElementById('m'+i);if(m){{const p=ease((t-ST[1]-0.5-i*1.1)/0.4);m.style.opacity=p;m.style.transform=`translateY(${{(1-p)*30}}px)`;}}}}
for(let i=0;i<5;i++){{const f=document.getElementById('f'+i);if(f){{const v=f.dataset.v;const a=ST[2]+0.6+i*0.9;const k=Math.max(0,Math.min(1,(t-a)/0.6));f.textContent=v.slice(0,Math.round(k*v.length));}}}}
{{const tp=ST[2]+5.6;const r=document.getElementById('rp');const b=document.getElementById('pb');if(r){{if(t>tp&&t<tp+0.6){{const q=(t-tp)/0.6;r.style.opacity=1-q;r.style.transform=`scale(${{1+q*7}})`}}else r.style.opacity=0;}}
if(b){{if(t>tp+0.15){{b.style.background='#059669';b.textContent='✓ ORDER PLACED'}}else{{b.style.background='#DC2626';b.textContent='PLACE SELL LIMIT'}}}}}}
draw('pl3','dt3',R,Math.max(0,Math.min(1,(t-ST[3]-0.3)/3.2)));
{{const f=document.getElementById('fl');if(f)f.style.opacity=ease((t-ST[3]-3.6)/0.4);}}
{{const k=Math.max(0,Math.min(1,(t-ST[4]-0.2)/4.2));draw('pl4','dt4',R.concat(F.slice(1)),(R.length-1+k*(F.length-1))/(R.length+F.length-2));
const pp=document.getElementById('pp');if(pp)pp.textContent='+'+Math.round(200*k);}}"""
build("journey",sc,ST[-1],risk="مثال توضيحي · التداول فيه مخاطرة · مش نصيحة مالية",js=js,
 ticks=[ST[2]+0.6+i*0.15 for i in range(28)]+[ST[4]+0.3+i*0.2 for i in range(20)],hits=(0.7,ST[2]+5.6,ST[3]+3.6,ST[5]),mood='major')
print(ST)
