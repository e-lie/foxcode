Scale.default = 'minor'

Clock.bpm = 120


p1 >> pads(dur=8) + P*(0,4,3,4.5)
p1.only()

p1 >> pads(dur=8) + P*(0,4,4.5,0.5)

p1.stop()

p1 >> pads(dur=8, oct=5, chop=320, coarse=16) + P*(0,4,4.5,0.5)
p1 >> pads(dur=8, room=1, chop=320, coarse=16) + P*(0,4,4.5,0.5)

d1 >> play("(xxxX)(   [---])", sample=2, dur=1/2)
# d1 >> play("(xxxX)(   ([V--][V--][V--][----]))", amp=PWhite(0.7,1)[:17], room=0.6)

# b4 >> bass([0,4,7], dur=PDur(3,5), rate=var([1,2,3,4],4), oct=(3,4))

d2 >> play("[ii]", amp=linvar([0,1,0],[2,0,2]), rate=2, crush=8, pan=[-1,1])
d2 >> play("[ii]", amp=linvar([0,1,0],[2,0,2]), rate=2, crush=8, pan=[-1,1])

d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]), bits=4, rate=2, crush=4, room=0.5, pan=[-1,1])

d1 >> play("xn", sample=[0,PRand(7)]).every(6, "stutter", 4, dur=3)
d3 >> play("  u ")


b1 >> bass([0,0.5], dur=4, oct=5, shape=2)
b1 >> bass([0,0.5], dur=4, oct=5, shape=2, slide=PRand([-1,0,-2,-3]), coarse=PRand([4,8,16]))
b1 >> bass([0,0.5], dur=4, oct=5, shape=2, slide=PRand([-1,0,-2,-3,-4,2]), coarse=PRand([4,8,16,32,0,64]))


d3 >> play(Pvar(["  u ","  u u"],8))
d3 >> play(Pvar(["  u ","  u u"],8), dur=PDur(var([4,5],16),8))


d1 >> play("xn", sample=[0,PRand(7)]).every(6, "stutter", 4, dur=3).every(8,"amen")

Master().lpf=var([0,200],[28,4])

Master().amplitude=var([1,0.2],[28,4])

Root.default = var([0,2],64)

Master().lpf=var([0,1000],[28,4])
Master().lpr=linvar([0.1,1])

b1 >> bass([0,0.5], dur=4, oct=3, shape=2, slide=PRand([-1,0,-2,-3,-4,2]), coarse=PRand([4,8,16,32,0,64])*PRand([1,1.5]))

c1 >> play("#", dur=8, bits=4, cut=1/4, room=1)
c1 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,1], slide=-1)
c1 >> play("#", dur=P[8:12], bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,1], slide=-1)

#break
c1.solo()

c1 >> play("#", dur=P[8:12], bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,1], slide=-1, chop=320, rate=PRand(8))

#relaunch preceding drum
d1 >> play("xn", sample=[0,PRand(7)]).every(6, "stutter", 4, dur=3)

c1.rate=PRand(8)+10

s1 >> saw(PWhite(32), dur=1/4)
s1 >> saw(PWhite(32), dur=1/6, fmod=10)
s1 >> pulse(PWhite(32), dur=1/4, fmod=10, oct=5)

Group(s1,b1).only()

s1 >> pulse(PWhite(32)[:8], dur=1/6, fmod=10, oct=4)

d4 >> play("funky", rate=10, dur=1/4)
d4 >> play("funky", rate=4*PRand([1,1.5,1.25]), dur=1/4)
d4 >> play("funky", rate=4*PRand([1,1.5,1.25]), dur=1/4, pan=PStep(6,P*(-1,1)))

b1.stop()

s1 >> pulse(PWhite(32)[:8], dur=1/4, fmod=10, oct=4) + var([0,(0,4)],[12,4])
d4 >> play("<funky><  (ew)l>", rate=4*PRand([1,1.5,1.25]), dur=1/2, pan=PStep(6,P*(-1,1)))
d4 >> play("<funky><  (+q)l>", rate=4*PRand([1,1.5,1.25]), dur=1/2, pan=PStep(6,P*(-1,1)))

s1.every(8, "degrade")

s1.stop()

d3 >> play("*", sample=2, dur=1/4, amp=1)
d3 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16])
d3 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1])
d3 >> play("*", sample=2, dur=1/4, amp=PRand(1.5)[:16], pan=[-1,0,1], rate=var([1,2]))

d3.stop()

d1 >> play("xn", sample=[0,PRand(7)]).every(6, "stutter", 4, dur=3) #relaunch
d1 >> play("<Vn><  u >", sample=[0,PRand(7)]).every(6, "stutter", 4, dur=3)

p1 >> pads(dur=8, room=1, chop=320, coarse=16) + P*(0,4,4.5,0.5) # relaunch
p1 >> pads(dur=8, room=1, chop=320, coarse=16, lpf=linvar([400,800],24), lpr=linvar([0.1,1],14)) + P*(0,4,4.5,0.5)
p1 >> pluck(dur=8, room=1, chop=320, coarse=16, lpf=linvar([400,800],24), lpr=linvar([0.1,1],14)) + P*(0,4,4.5,0.5)

p1.only()


d_all.amplify=var([1,0],[28,4])

p2 >> blip(dur=12, fmod=4, vib=12, slide=-1, oct=7, pan=P+(-1,0,1), sus=4)
p2 >> blip(dur=12, fmod=4, vib=12, slide=-1, oct=7, pan=P+(-1,0,1), sus=4, bits=8, crush=8)
p2 >> blip(dur=12, fmod=4, vib=12, slide=-1, oct=7, pan=P+(-1,0,1), sus=4, bits=8, crush=8) + (0,2)


d1 >> play("n", sample=PRand(7), pan=PWhite(-1,1))
d1 >> play("n", sample=PRand(7)+PStep(7,P*(0,1)), pan=PWhite(-1,1))

d2 >> play("(s )( s)O ")
d2 >> play("(X )( X)O ", rate=(.9,1), pan=(-1,1))
d2 >> play("(X )( X)O ", rate=(.9,1), pan=(-1,1)).every(6, "stutter", n=4, dur=3)
d2 >> play("< s><(X )( X)O >", rate=(.9,1), pan=(-1,1)).every(6, "stutter", n=4, dur=3)

d3 >> play("[oo]", amp=linvar([0,0.5],[32,0]))
d4 >> play("#", dur=32)

d5 >> play("[oo]", amp=linvar([0,0.8],[32,0]))
