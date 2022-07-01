Clock.bpm = 136
root.default = -4


d1 >> play(P["x--(-[--])o--(=-)"].layer("mirror"),
    pan=(-1, 1),
    dur=PDur(5,8),
    sample=-1,
    rate=var([1,4],[28,4])).every(5,'stutter', 0, pan=[-1,1], rate=4)

d2 >> play(PZip("Vs", "  n "), sample=2, hpf=var([0,4000], [28,4])).every(3, 'stutter', dur=1)
# d2.stop()

s1 >> swell((0,2,4,const(6)), dur=4) + var([0,[1,-1]], 8)

d3 >> play("[--]", amp=1.5)

b1 >> bbass(var([0,[1,-1],8]), dur=PDur(5,12), bits=0, lpf=0, fmod=(0,1), amp=0.7, oct=3) + [0,4,const(7)]

k2 >> karp([0,7,6,4,2], sus=2)

k1 >> karp(dur=1/4, oct=var([6,7]), sus=1, rate=P[:32]*(1,2), delay=(0, 1/8), lpf=linvar([400,5000],12), pan=linvar([-1,1], 8)+var([0,-1,1,-7]))

p1 >> piano([var([0,-1,-1,0]),4,[7,10],9], oct=(6), amp=2, sus=2, dur=PDur(5,8)*2 )

p1.solo()

Scale.default = Pvar([Scale.major, Scale.minor], 16)
