import asyncio, json, subprocess, sys
sys.path.insert(0,'/home/claude/vo')
exec(open('/home/claude/vo/vo.py').read().split('async def main')[0])
L=[("أمسِ صباحاً… قلنا إننا نتوقّعُ هبوطاً للذهب.","+2%","-2Hz"),
   ("وانتظرنا تأكيداً واضحاً قبل الدخول.","+0%","-2Hz"),
   ("جاءَ التأكيد… فدخلنا بيعاً.","+0%","-3Hz"),
   ("وأغلقنا الصفقة على مئةٍ وأربعٍ وثمانين نقطة.","+2%","-1Hz"),
   ("وهذه واحدةٌ فقط من صفقات قناة الـ VIP.","+2%","-2Hz"),
   ("وأنت في بيتك… تتابع السوق من هاتفك.","+0%","-2Hz"),
   ("واليوم؟ كن مستعدّاً… وتابعنا.","+0%","-3Hz")]
async def m():
    for i,(t,r,p) in enumerate(L):
        await edge_tts.Communicate(t,"ar-SA-HamedNeural",rate=r,pitch=p,proxy=PX).save(f"n{i}.mp3")
asyncio.run(m())
AF=("silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
    "highpass=f=75,equalizer=f=180:t=q:w=1:g=2.5,equalizer=f=3200:t=q:w=1.2:g=1.5,equalizer=f=7500:t=q:w=1:g=-3,"
    "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=3,aecho=0.85:0.5:28|46:0.10|0.06")
d=[]
for i in range(len(L)):
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'n{i}.mp3','-af',AF,'-ar','44100','-ac','2',f't{i}.wav'],check=True); d.append(dur(f't{i}.wav'))
json.dump(d,open('durs.json','w')); print([round(x,2) for x in d], round(sum(d),1))
