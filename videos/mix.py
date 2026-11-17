import json,subprocess,os,sys
src,dst,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
st=json.load(open('/home/claude/vo/starts.json'))
offs=[st[i]+(0.2 if i else 0.1) for i in range(n)]
inp=[];fl=[]
for i in range(n):
    inp+=['-i',f'/home/claude/vo/t{i}.wav']; fl.append(f"[{i+1}:a]adelay={int(offs[i]*1000)}|{int(offs[i]*1000)},volume=1.5[v{i}]")
fc=";".join(fl)+";"+"".join(f"[v{i}]" for i in range(n))+f"amix=inputs={n}:normalize=0[vo];[vo]asplit=2[voa][vob];[0:a]volume=0.42,lowpass=f=9000[m];[m][voa]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=500[md];[md][vob]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]"
tmp=dst.replace('.mp4','_tmp.mp4')
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src]+inp+['-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k',tmp],check=True)
os.replace(tmp,dst); print('mixed',dst)
