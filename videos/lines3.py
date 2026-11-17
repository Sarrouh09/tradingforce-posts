import asyncio, json, subprocess
exec(open('vo.py').read().split('async def main')[0])
L=[("هل تقوم بكل هذا وحدك؟ مؤشرات، وأخبار، وسهرٌ حتى الفجر؟","+2%","-2Hz"),
   ("انتظر.","-5%","-3Hz"),
   ("دَعِ العملَ الشاقَّ علينا. نحن نحلّل السوق، ونتابع الأخبار، ونحسب لك المخاطرة، ووقف الخسارة، والهدف.","+4%","-2Hz"),
   ("وأنت؟ تصلك خطةٌ واضحة… على هاتفك.","+0%","-1Hz"),
   ("والقرار بيدك. إن كنت مقتنعاً… تدخل بضغطةٍ واحدة.","+0%","-2Hz"),
   ("ولنكن صريحين معك: ليست كلُّ صفقةٍ رابحة. ولهذا… وقفُ الخسارة موجودٌ دائماً.","+2%","-3Hz"),
   ("هل تريد أن تعرف كيف نعمل؟ اكتب لنا في التعليقات… وسنردُّ عليك.","+2%","-1Hz")]
async def say2(t,out,r,p):
    await edge_tts.Communicate(t,"ar-SA-HamedNeural",rate=r,pitch=p,proxy=PX).save(out)
async def m():
    for i,(t,r,p) in enumerate(L): await say2(t,f"n{i}.mp3",r,p)
asyncio.run(m())
# humanize: trim, warm EQ, gentle compression, tiny room
AF=("silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
    "highpass=f=75,equalizer=f=180:t=q:w=1:g=2.5,equalizer=f=3200:t=q:w=1.2:g=1.5,equalizer=f=7500:t=q:w=1:g=-3,"
    "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=3,aecho=0.85:0.5:28|46:0.10|0.06")
d=[]
for i in range(len(L)):
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'n{i}.mp3','-af',AF,'-ar','44100','-ac','2',f't{i}.wav'],check=True)
    d.append(dur(f't{i}.wav'))
json.dump(d,open('durs.json','w')); print([round(x,2) for x in d], round(sum(d),1))
