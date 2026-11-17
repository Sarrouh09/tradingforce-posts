import asyncio, json, subprocess
exec(open('vo.py').read().split('async def main')[0])
L=[("بص… إنتَ بتعمل ده كله لوحدك؟ مؤشرات، وأخبار، وسهر لحد الفجر؟","+4%","-2Hz"),
   ("طب استنى.","-5%","-4Hz"),
   ("خلّي الشغل التقيل ده علينا. إحنا بنحلل السوق، وبنتابع الأخبار، وبنحسبلك المخاطرة، ووقف الخسارة، والهدف.","+6%","-2Hz"),
   ("وإنتَ؟ بتوصلك خطة واضحة… على موبايلك.","+0%","-1Hz"),
   ("والقرار في إيدك. لو مقتنع… تدخل بضغطة.","+0%","-2Hz"),
   ("وخليني أكون صريح معاك: مش كل صفقة بتكسب. وعشان كده… وقف الخسارة موجود دايماً.","+3%","-3Hz"),
   ("عايز تعرف بتشتغل إزاي؟ اكتبلي «إزاي» في الكومنتات… وأنا هرد عليك.","+3%","-1Hz")]
async def say2(t,out,r,p):
    await edge_tts.Communicate(t,"ar-EG-ShakirNeural",rate=r,pitch=p,proxy=PX).save(out)
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
