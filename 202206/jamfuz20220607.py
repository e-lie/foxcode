from FoxDot.preset import *


e2 >> crazykit("fF", dur=P[7,1,8,3,5]/2, amp=[.6,.7,.9,1.23], scale=Scale.major)

d2 >> play("<(     w) w>", room=3)
d3 >> play(" -", room=3, amp=2, sample=P[0,1,2].stutter(3)).mpan(mrot(16))


b3 >> bbass([3,4,5]*2 + [1,1], dur=[2,2,3,1], sus=[2,2,3,1], oct=3).fadein()

m4 >> blip([4], dur=.25, amplify=pa16_2)
m3 >> blip([12,0], dur=clave23, amplify=pa16, oct=(2,4,6))

d1 >> play("<X >", dur=.5, sample=2)

e2.sfadeout(16)

d2 >> play("x(---[--])", sample=(0,1), amp=[1.2,.8], pan=[-1,.5,1]).fadein()

m1 >> tb303(
    [0,2,4,-5,2],
    dur=cascara,
    amp=1.2,
    root=var([0,2,0,4], [16,8,8,16,8]),
    scale = Scale.minor,
    oct = 3,
    hpf=000,
).mpan(mrot(32))
m1.fadein()

t3 >> play(".(...(.(*[**]*)))", sample=(0,1), amp=[1.2,.8], room=3, dur=.5, sus=4).mpan(mrot(11))

t5 >> play("tt", dur=cascara, sample=P[0,1,2].stutter(4)).mpan(mrot(7))

t2 >> play("<XvvXv>< (*[**]) >", dur=clave23, sample=P[0,1,2].stutter(4)).mpan(mrot(16))

ee >> click(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3, 1], 8), amplify=pa32) + (0,2,4)
ee.mpan(mrot(8))

ee.fadeout()

e6 >> whibot(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3, 1], 8)).span(srot(16))
e6.fadein(32)

e6.sfadeout()
