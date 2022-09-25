from FoxDot.preset.common import *

Scale.default = Pvar([Scale.major, Scale.minor, Scale.egyptian], 4)
# Root.default = var([0,4,-2,2])

Root.default = var([0,-2,2,0,4], [2,4])

change_bpm(100)

b1 >> blip([0,-2,4], dur=[1/2,1,.25,.25], sus=linvar([0.1,1],16))

b1 >> blip([num/20 for num in range(100)], dur=.25, sus=sinvar([0.1,.7], 7), crush=linvar([0,16], 32))


b1 >> blip([num/20 for num in range(100)], dur=.25, sus=sinvar([0.1,.7], 7), crush=linvar([0,16], 32))

b1.fadeout()

b2 >> pluck([0,-2,2,-4], dur=cascara, sus=linvar([0.1,1],16), oct=[4], amp=3)

b1 >> blip([0,-2,2,-4], dur=1/4, sus=linvar([0.1,1],16), oct=[6], amp=2)

b3 >> pluck([0,-2,2,6,2], dur=2/5, sus=linvar([0.1,2],16), oct=[5], amp=2)

d1 >> play(" (-[-------...----]-[--])", dur=cascara, amp=2)
d1 >> play(" (-[-------...----]-[--])", dur=brafflet, amp=2)

d2 >> play("<(***[**])><Vxx>", dur=clave23)

b6 >> hpluck([0,2,0,-2], dur=clave23, hpluck_reverb=linvar([0,1], 8), hpluck_drive=sinvar([0,1], 5), oct=4)

d_all.crush = linvar([0,16],8)

d_all.sample = var([0,1,2,3], 7)

b_all.crush = linvar([0,16],4)

d1.pause(4, 16)
d2.pause(4, 16, 5)
d3.pause(8, 20, 7)
b1.pause(6, 16, 7)
b2.pause(6, 16, 4)

d3 >> play("(vvV[vv])(**.)", dur=.5, sample=[0,1])

d3 >> play("(vvvV)-", dur=.5, sample=0)

arrêter()

b1 >> play("--[--]=", dur=2/3, amp=2).stop()
b2 >> play("xxx[xx]", dur=4/4, amp=1).mpan(1)

b3 >> play("*", dur=var([2/5, 2/3, .5]), amp=2)

b_all.crush=linvar([0,16],8)
b_all.crush=0
b_all.sample=var([0,1,2,4],[1,.5,2,4,2])

Clock.bpm = 120
