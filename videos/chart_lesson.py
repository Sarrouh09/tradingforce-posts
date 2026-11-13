import json, numpy as np
from vid import build
rng=np.random.default_rng(3)
# illustrative path: rise into sell zone ~4058, rejection, fall to TP 4010
path=list(np.linspace(4028,4060,18))+list(np.linspace(4060,4050,5))+list(np.linspace(4050,4006,19))
c=[];prev=path[0]
for p in path:
    o=prev; cl=p+rng.normal(0,2.2); hi=max(o,cl)+abs(rng.normal(0,3)); lo=min(o,cl)-abs(rng.normal(0,3)); c.append([round(o,1),round(hi,1),round(lo,1),round(cl,1)]); prev=cl
c[17][1]=4068; c[18][1]=4066  # wick into zone, below SL
W,H,X0,Y0=960,860,60,560; lo_,hi_=3995,4085
data=json.dumps(c)
ov=f"""<svg id='ch' width='1080' height='1920' style='position:absolute;inset:0;pointer-events:none'>
<text x='540' y='{Y0-20}' text-anchor='middle' fill='#9CB0DA' font-size='26' font-family='Inter'>XAU/USD · M15 · مثال توضيحي (Illustration)</text>
<rect x='{X0}' y='{Y0}' width='{W}' height='{H}' rx='24' fill='rgba(14,34,83,.55)' stroke='#28498F'/>
<g id='lines'></g><g id='cd'></g></svg>
<script>const C={data},LO={lo_},HI={hi_},X0={X0+30},Y0={Y0+30},W={W-60},H={H-60};
const Y=v=>Y0+(HI-v)/(HI-LO)*H, step=W/C.length;
function line(v,col,lab,op){{return `<g opacity='${{op}}'><line x1='${{X0}}' x2='${{X0+W}}' y1='${{Y(v)}}' y2='${{Y(v)}}' stroke='${{col}}' stroke-width='4' stroke-dasharray='14 10'/><rect x='${{X0+W-230}}' y='${{Y(v)-26}}' width='230' height='52' rx='12' fill='${{col}}'/><text x='${{X0+W-115}}' y='${{Y(v)+11}}' text-anchor='middle' font-size='30' font-weight='800' fill='#071331' font-family='Inter'>${{lab}}</text></g>`}}
window.CH=function(t){{const n=Math.max(0,Math.min(C.length,Math.floor((t-0.2)/13.2*C.length)));let s='';
for(let i=0;i<n;i++){{const [o,h,l,c]=C[i],x=X0+i*step+step/2,up=c>=o,col=up?'#34D399':'#F87171';
s+=`<line x1='${{x}}' x2='${{x}}' y1='${{Y(h)}}' y2='${{Y(l)}}' stroke='${{col}}' stroke-width='3'/><rect x='${{x-step*0.32}}' y='${{Y(Math.max(o,c))}}' width='${{step*0.64}}' height='${{Math.max(3,Math.abs(Y(o)-Y(c)))}}' fill='${{col}}' rx='2'/>`}}
document.getElementById('cd').innerHTML=s;
const f=a=>Math.max(0,Math.min(1,(t-a)/0.4));
document.getElementById('lines').innerHTML=line(4058,'#60A5FA','SELL 4058',f(6.6))+line(4075,'#F87171','SL 4075',f(7.6))+line(4010,'#34D399','TP 4010',f(8.6));
document.getElementById('ch').style.opacity=t>14.2?Math.max(0.06,1-(t-14.2)/0.5):1;}}</script>"""
top="style='position:absolute;top:200px;left:60px;right:60px;justify-content:flex-start;padding:0'"
def sc(a,b,h): return (a,b,f"<div {top} class='x'>{h}</div>")
scenes=[
 (0,3,"<div style='position:absolute;top:220px;left:0;right:0'><div class='ar' style='font-size:66px'>إزاي بنقرا صفقة دهب<br><span class='grad'>على الشارت؟</span></div></div>"),
 (3,6.5,"<div style='position:absolute;top:240px;left:0;right:0'><div class='ar' style='font-size:58px'>١. السعر طالع<br><span class='grad'>لمنطقة البيع</span> 📈</div></div>"),
 (6.5,10,"<div style='position:absolute;top:240px;left:0;right:0'><div class='ar' style='font-size:56px'>٢. بنحدد الدخول<br><span style='color:var(--loss)'>ووقف الخسارة فوقه</span> 🛑</div></div>"),
 (10,14.2,"<div style='position:absolute;top:240px;left:0;right:0'><div class='ar' style='font-size:56px'>٣. والهدف تحت…<br><span style='color:var(--win)'>والسعر وصله</span> ✅</div></div>"),
 (14.2,19,"<div class='ar' style='font-size:76px'>كل صفقة عندنا<br><span class='grad'>واضحة من الأول</span></div><div class='ar2' style='margin-top:30px'>دخول · وقف خسارة · هدف</div><div class='ar2 gold' style='margin-top:10px'>تابعنا 🔔 وابعتلنا «ذهب»</div>")]
print(build("chart_lesson",scenes,19,js="CH(t);",overlay=ov,hits=(13.3,)))
