"""Original, royalty-free sound design generated from scratch: beat + pad + whooshes + ticks."""
import numpy as np, wave
SR=44100
def _env(n,a,d):
    e=np.ones(n); ai=int(a*SR); di=int(d*SR)
    if ai: e[:ai]=np.linspace(0,1,ai)
    if di: e[-di:]=np.linspace(1,0,di)
    return e
def make(path,dur,cuts=(),ticks=(),hits=(),bpm=100,mood='minor'):
    n=int(dur*SR); t=np.arange(n)/SR; L=np.zeros(n); R=np.zeros(n)
    beat=60/bpm; rng=np.random.default_rng(7)
    # kick on every beat, hat on off-beats
    k=np.arange(int(0.35*SR))/SR; kick=np.sin(2*np.pi*(50*k+45*(1-np.exp(-k*30))/30))*np.exp(-k*9)
    h=rng.standard_normal(int(0.06*SR)); h=np.diff(h,prepend=0)*np.exp(-np.arange(len(h))/SR*70)
    b=0.0
    while b<dur-0.2:
        i=int(b*SR); seg=kick[:max(0,min(len(kick),n-i))]; L[i:i+len(seg)]+=0.55*seg; R[i:i+len(seg)]+=0.55*seg
        j=int((b+beat/2)*SR)
        if j<n: s=h[:min(len(h),n-j)]; L[j:j+len(s)]+=0.12*s; R[j:j+len(s)]+=0.10*s
        b+=beat
    # warm pad (minor or major chord), slow swell
    ch=[110,130.81,164.81,220] if mood=='minor' else [110,138.59,164.81,220]
    pad=sum(np.sin(2*np.pi*f*t+0.3*np.sin(2*np.pi*0.2*t))+0.3*np.sin(2*np.pi*2*f*t) for f in ch)/len(ch)
    pad*=0.10*(0.6+0.4*np.sin(2*np.pi*t/(beat*8)))*_env(n,1.0,1.5)
    L+=pad; R+=pad*0.95
    # whoosh at each cut
    for c in cuts:
        m=int(0.5*SR); i=int(max(0,c-0.25)*SR); w=rng.standard_normal(m)
        w=np.convolve(w,np.ones(12)/12,'same')*np.hanning(m)*0.35
        e=min(m,n-i); L[i:i+e]+=w[:e]; R[i:i+e]+=w[:e][::-1]*0.9
    # ticks (counter) and hits (impact)
    tk=np.sin(2*np.pi*1800*np.arange(int(0.03*SR))/SR)*np.exp(-np.arange(int(0.03*SR))/SR*120)
    for x in ticks:
        i=int(x*SR); e=min(len(tk),n-i)
        if e>0: L[i:i+e]+=0.15*tk[:e]; R[i:i+e]+=0.15*tk[:e]
    hm=np.arange(int(0.6*SR))/SR; hit=(np.sin(2*np.pi*80*hm)*0.8+rng.standard_normal(len(hm))*0.15)*np.exp(-hm*6)
    for x in hits:
        i=int(x*SR); e=min(len(hit),n-i)
        if e>0: L[i:i+e]+=0.5*hit[:e]; R[i:i+e]+=0.5*hit[:e]
    st=np.stack([L,R],1); st/=max(1e-9,np.abs(st).max())/0.85; st*= _env(n,0.02,0.6)[:,None]
    with wave.open(path,'wb') as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes((st*32767).astype(np.int16).tobytes())
