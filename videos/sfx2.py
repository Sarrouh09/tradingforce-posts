import numpy as np, json, wave
exec(open('sfx.py').read().split("ding(0.3)")[0].replace("json.load(open('/home/claude/out/journey_fast_st.json'))","json.load(open('/home/claude/out/why_st.json'))"))
sweep(0.2,2.4,900,200,0.22)          # falling sweep for the drop
for k in range(20): click(0.2+k*0.12)
for i in range(1,5): pop(ST[i]+0.05,600+i*100); arp(ST[i]+0.15,[659,880],0.06,0.25)
for i in range(2): pop(ST[5]+0.6+i*0.6,800); 
arp(ST[5]+0.1,[440,415,392],0.12,0.3)   # tension
arp(ST[6]+0.1,[523,659,784,1047],0.07,0.35)
out=out/np.max(np.abs(out))*0.9
st=np.stack([out,out],1); pcm=(st*32767).astype(np.int16)
with wave.open('/home/claude/out/why_sfx.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok')
