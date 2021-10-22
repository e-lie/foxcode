Clock.bpm=120


p1 >> loop("foxdot", P[:16])

p1 >> loop("foxdot", 0, dur=PDur(3,8) | [0.5,1.5],
           pshift=(0,0.1), pan=(-1,1), formant=var([0,4],[12,4]))

p1.rate=1/2

d1 >> play("x-")
d1 >> play(P["(V )( V)O "].amen())
d2 >> play("----") + 2

Root.default= -2
Scale.default = "minor"

b1 >> bass(var([0,-1],[3,1]), dur=PDur(5,12), shape=0.5, fmod=(0,1))

k1 >> klank(var([9,6,7]), rate=P[4:24].stutter(2))
