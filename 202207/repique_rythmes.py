from FoxDot.preset.reaper import *
from FoxDot.preset import *

change_bpm(162)

l1 >> loop("200173-breakbeat5.wav", 0, rate=1.35, dur=4)

d1 >> play("<V O  VO ><[SS]><   [ o][ o] o >", sample=4, crush=sinvar([0,32], 16), pan=linvar([-1, 1], [4,8,0,2,4,1,8,0]))
d1.rate = var(linvar([.5,2], [4,0,8,1,0,8,0]))

d2 >> play("*", pan=[-1,1], dur=cascara)

################################################################

change_bpm(177)


Clock.bpm = 129.5

d2 >> play("V ")
l1 >> loop("Unknown Artist - Nique La BAC", 32, rate=1, dur=8)
