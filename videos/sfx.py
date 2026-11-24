import numpy as np, json, wave
SR=44100
ST=json.load(open('/home/claude/out/journey_fast_st.json')); D=ST[-1]
out=np.zeros(int(SR*(D+0.5)))
def add(sig,t,g=1.0):
    i=int(t*SR); e=min(len(out),i+len(sig)); out[i:e]+=sig[:e-i]*g
def env(n,a=0.005,r=0.15):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/r)
def tone(f,d,r=0.15,a=0.005,shape='sine'):
    n=int(d*SR); t=np.arange(n)/SR
    w=np.sin(2*np.pi*f*t) if shape=='sine' else np.sign(np.sin(2*np.pi*f*t))*0.5
    return w*env(n,a,r)
def ding(t): add(tone(1318.5,0.6,0.25)+0.6*tone(1975.5,0.6,0.2),t,0.5); add(tone(1568,0.6,0.25),t+0.12,0.4)
def pop(t,f=880): 
    n=int(0.09*SR); tt=np.arange(n)/SR; add(np.sin(2*np.pi*(f+2000*np.exp(-tt*60))*tt)*env(n,0.002,0.03),t,0.55)
def click(t): add(np.random.default_rng(int(t*1000)).normal(0,1,int(0.012*SR))*env(int(0.012*SR),0.0005,0.004),t,0.25)
def arp(t,notes,step=0.07,g=0.4,shape='square'):
    for k,f in enumerate(notes): add(tone(f,0.25,0.12,0.003,shape),t+k*step,g)
def sweep(t,d,f0,f1,g=0.18):
    n=int(d*SR); tt=np.arange(n)/SR; f=f0+(f1-f0)*tt/d; ph=2*np.pi*np.cumsum(f)/SR
    add(np.sin(ph)*np.minimum(1,tt/0.05)*np.minimum(1,(d-tt)/0.05),t,g)
ding(0.3)
for i in range(4): pop(ST[1]+0.3+i*0.5, 700+i*120)
for i in range(5):
    a=ST[2]+0.3+i*0.45
    for k in range(5): click(a+k*0.07)
pop(ST[2]+2.8,500); arp(ST[2]+2.9,[784,988,1175],0.06,0.35)
sweep(ST[3]+0.2,1.8,300,900)
arp(ST[3]+2.1,[523,659,784,1047],0.06,0.4)          # power-up
for k in range(20): pop(ST[4]+0.2+k*0.13, 900+k*40)  # counter coins
arp(ST[5],[523,659,784,1047,1319,1568],0.08,0.45)    # victory
arp(ST[5]+0.55,[1047,1319,1568,2093],0.05,0.3,'sine')
out=out/np.max(np.abs(out))*0.9
st=np.stack([out,out],1); pcm=(st*32767).astype(np.int16)
with wave.open('/home/claude/out/journey_sfx.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok',D)
