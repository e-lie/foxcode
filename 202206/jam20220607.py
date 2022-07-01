from FoxDot.preset import *


change_bpm(120)

sc >> supercollider()

m1 >> tb303(
    [0,2,4,-5,2],
    dur=cascara,
    amp=1.2,
    root=var([0,2,0,4], [16,8,8,16,8]),
    scale = Scale.minor,
    oct = 3,
    hpf=000,
).mpan(mrot(32))

sc >> supercollider(verb_w=linvar([.6,1], 8), verb_size=linvar([.8,1], 16))

tt >> play("x(---[--])", sample=(0,1), amp=[1.2,.8]).mpan(mrot(32)).stop()
t3 >> play(".(...(.(*[**]*)))", sample=(0,1), amp=[1.2,.8], room=3, dur=.5, sus=4)

t2 >> play("<XvvXv>< (*[**]) >", dur=clave23, sample=P[0,1,2].stutter(4))
t5 >> play("tt", dur=cascara, amp=2, sample=P[0,1,2].stutter(4))

dd >> ducker(0, sus=.5, ducking=.6)

t2.rate = sinvar([.5,3], 32)

ee >> click(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(2,3,4,7,8), dur=var([.25, .5, 1/3, 1], 8), amplify=pa32) + (0,2,4)


e6 >> ratic(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3, 1], 8))
e6.fadein(32)

e6.vol = 1.2

e7 >> fordrip([0], ).fadein()
e6 >> bnoise([0]).fadein()

d1 >> play("(   (---w))(---( V vV))", amp=linvar([0,6], 16), sample=var([0,1,2,3], 8), room=linvar([0,6], 32))

e6.stop()

b1 >> wobblebass([0,2,4], scale=Scale.minor, dur=2, oct=(3,4))
