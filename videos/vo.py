import asyncio, edge_tts, subprocess, json, sys, ssl, os
import edge_tts.communicate as C
C._SSL_CTX=ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
PX=os.environ.get('HTTPS_PROXY')
async def say(text, out, voice, rate="+0%"):
    await edge_tts.Communicate(text, voice, rate=rate, proxy=PX).save(out)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
async def main():
    s="خلّي الشغل التقيل علينا. إحنا بنحلل السوق، وبنتابع الأخبار، وبنحسب المخاطرة، وبنحدد وقف الخسارة والهدف."
    for v in ("ar-EG-ShakirNeural","ar-EG-SalmaNeural"):
        await say(s, f"sample_{v.split('-')[2]}.mp3", v)
        print(v, dur(f"sample_{v.split('-')[2]}.mp3"))
asyncio.run(main())
