Clock.bpm = 170
Clock.meter = (4,4)



piano = Instruc(1, 6, Clock)

percu = Instruc(2, 3, Clock)

percu2 = Instruc(2, 3, Clock)

kit808 = Instruc(3, 3, Clock)

advoca = Instruc(4, 3, Clock)

basss =  Instruc(5, 4, Clock)

offworld =  Instruc(6, 4, Clock)

balafon =  Instruc(7, 6, Clock)


advoca.stop()

congL=0
clave=1
congH=2
cowb=3
congM=4
egg=5
cabasa=6
bonL=7
triM=8
bonH=9
triO=10
woodB=11
tamO=12
tamS=13
vib=14
chim=15

percu.update([bonL]*8 + [bonH], dur=[3/10,4/10,3/10])
percu.update(amp=PWhite(0.6,0.9)[:30])

percu2.stop()

percu2.update(cowb, dur=[4/10,3/10,3/10])
percu2.update(amp=PWhite(0.4,0.6)[:30])

kit808.update([0], dur=[1], amp=PWhite(0.6,0.9)[:30])

chp1 = var([0,4,5,7], 4)
scp1 = Pvar([Scale.major, Scale.minor],16)

balafon.update(chp1, oct=3, dur=PDur(3,8), scale=scp1)
balafon.update(amp=PWhite(0.1,0.9)[:30])
balafon.stop()

qcp1 = var([0,4,8])

balafon.update(PWalk(max=8)[:100]+qcp1, scale=scp1, oct=5, dur=P[4/10,3/10,3/10], amp=(abs(PWalk(max=8)[:100])+2)/10)
balafon.stop()

print(abs(PWalk(max=10)[:16])/10)

advoca.update(chp1 + (0,2), dur=PDur(7,16), oct=6, amp=0.2, scale=scp1)

advoca.set_param(1, 10, update_freq=0.3)

@run_now
def tttt():
    p2 >> play("X-X-")
    p2.stop()
