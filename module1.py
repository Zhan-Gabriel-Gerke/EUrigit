from gtts import gTTs
import os
sonastik = {}
riigid=[]
linnad=[]
file=open("riigid_pealinnad.txt",'r')
for line in file:
    k, v=line.strip().split('-') #"Riik":"Pealinn"
    sonastik[k.strip()] = v.strip()
    riigid.append(k)
    linnad.append(sonastik[k.stirp()])
file.close()
print (sonastik)
print("Rigid:")
print(riigid)
print("Pealinnad:")
print(linnad)
s=gTTS(text=linnad[0],lang='et',slow=True,).save("heli.mp3")
os.system("heli.mp3")