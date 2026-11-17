import asyncio, json, sys
sys.argv=['x']; exec(open('vo.py').read().split('async def main')[0])
L=["بتعمل ده كله لوحدك؟ مؤشرات، وأخبار، وسهر لحد الفجر؟",
   "استنى.",
   "خلّي الشغل التقيل علينا: تحليل السوق، والأخبار، والمخاطرة، ووقف الخسارة، والهدف.",
   "وإنت بتوصلك خطة واضحة على موبايلك.",
   "وإنت اللي بتقرر، وتدخل بضغطة.",
   "وبصراحة، مش كل صفقة بتكسب. عشان كده وقف الخسارة موجود دايماً، والقرار في إيدك.",
   "عايز تعرف بيشتغل إزاي؟ اكتب: إزاي، في الكومنتات، وتابعنا."]
async def m():
    d=[]
    for i,t in enumerate(L):
        await say(t,f"l{i}.mp3","ar-EG-ShakirNeural","+15%"); d.append(dur(f"l{i}.mp3"))
    print(json.dumps(d)); json.dump(d,open('durs.json','w'))
asyncio.run(m())
