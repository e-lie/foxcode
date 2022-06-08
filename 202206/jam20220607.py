from FoxDot.preset import *


change_bpm(120)

sc >> supercollider()

m1 >> tb303(
    [0,2,4,-5,2],
    dur=cascara,
    amp=1.2,
    root=var([0,2,0,4], [16,8,8,16,8]),
    scale = Scale.minor,
    oct = 4,
).mpan(mrot(32))

sc >> supercollider(verb_w=linvar([.6,1], 8), verb_size=linvar([.8,1], 16))

tt >> play("x(---[--])", sample=(0,1), amp=[1.2,.8]).mpan(mrot(32))
t3 >> play(".(...(.(*[**]*)))", sample=(0,1), amp=[1.2,.8], room=3, dur=.5).mpan(mrot(11))

t2 >> play("<Vvv>< (*[**]) >", dur=clave23, sample=P[0,1,2].stutter(4)).mpan(mrot(16))
t5 >> play("tt", dur=cascara, sample=P[0,1,2].stutter(4)).mpan(mrot(7))

t2.rate = sinvar([.5,3], 32)

ee >> click(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3, 1], 8), amplify=pa32) + (0,2,4)
ee.mpan(mrot(8))
