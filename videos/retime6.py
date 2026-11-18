import json
s=open('special.py').read()
d=json.load(open('/home/claude/vo/durs6.json'))
lens=[max(6.4,d[0]+0.7), d[1]+0.8, max(7.6,d[2]+0.8), max(3.8,d[3]+0.9), max(3.8,d[4]+0.9), d[5]+1.3]
st=[0]
for L in lens: st.append(round(st[-1]+L,2))
print(st)
s=s.replace('sc=[(0,4.6,S0),(4.6,5.6,S1),(5.6,11,S2),(11,15.2,S3),(15.2,19,S4),(19,22.5,S5),(22.5,26,S6)]',f'ST={st}\nsc=[(ST[i],ST[i+1],x) for i,x in enumerate([S0,S1,S2,S3,S4,S6])]')
s=s.replace('js="""','js="""const ST='+str(st)+';')
s=s.replace("if(t<4.6){","if(t<ST[1]){").replace("const k=Math.min(1,t/4.2)","const k=Math.min(1,t/(ST[1]-0.4))").replace("e.style.opacity=Math.min(1,Math.max(0,(t-i*0.18)/0.3));","e.style.opacity=Math.min(1,Math.max(0,(t-i*0.3)/0.3));").replace("(Math.min(1,t/4.3)*100)","(Math.min(1,t/(ST[1]-0.3))*100)")
s=s.replace("const a=6.3+i*0.85;","const a=ST[2]+2.6+i*1.35;")
s=s.replace("ease((t-11.6)/0.5)","ease((t-ST[3]-1.2)/0.5)").replace("const tp=16.6;","const tp=ST[4]+4.2;")
s=s.replace("وإنت تقرر… وتدوس 👆","القرار في إيدك 👆")
s=s.replace('build("we_do_the_work",sc,26,','build("we_do_the_work_v3",sc,ST[-1],')
s=s.replace("ticks=[6.65+i*0.85 for i in range(5)],hits=(4.6,11.6,16.6)","ticks=[ST[2]+2.95+i*1.35 for i in range(5)],hits=(ST[1],ST[3]+1.2,ST[4]+4.2)")
open('special_v3.py','w').write(s); json.dump(st,open('/home/claude/vo/starts.json','w'))
