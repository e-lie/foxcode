from FoxDot.preset import *

rot16 = linvar([0, 5.9], [16, 0])
rotrand1 = sinvar([0, 5.9], [7, 22, 4, 16])
rotrand2 = sinvar([0, 5.9], [17, 13, 7])
pa16 = var([1, 0, 1], [6, 4, 6])
pa16_2 = var([1, 0, 1], [2, 4, 10])
pa32 = var([1, 0], [24, 8])
pa32_2 = var([1, 0, 1], [16, 8, 8])
pa64 = var([1, 0, 1], [12, 16, 36])
ampr = PWhite(.8, 1.1)[:17]
Scale.default = Scale.minor

change_bpm(110)
sc >> supercollider(reverb_wet=0).fadein(16)
mi >> mixer()
wh >> uber(feedback=0)  #sinvar([.7, .9], 8))
sv >> sverb()
de >> delay()
tx >> tex()
sh >> shim(mix=1)

b1 >> nlead(
    PTri(8) * 2,
    dur=1,
    oct=PRand(2, 3),
    amplify=pa32,
    root=P[2, 4, 0].stutter(3)
).mpan(range(6))

b2 >> pluck(
    PTri(8) * 2,
    dur=.25,
    oct=P[2, 4].stutter(3),
    amp=3,
    amplify=pa32,
    formant(linvar([0, 2], 16))
).mpan(range(6))
b2.fmod = sinvar([0, 2], 17)

k1 >> kicker(
    "<(dabc) >",
    dur=.5,
    amplify=pa16_2,
).every(8, "stutter", 2)

b2 >> blip(PTri(16).stutter(2) * 3, dur=.25).mpan(range(6))
b1 >> blip(PTri(8).stutter(3) * 3, dur=1/3).mpan(range(6))
b4 >> blip(PTri(4).stutter(2) * 3, dur=cubalet,
           oct=P[3, 4].stutter(6)).mpan(range(6))
b1 >> blip(PTri(16).stutter(2) * 3, dur=cascara, oct=2, amp=4).mpan(range(6))

d1 >> play("<(X)(   =)><oo><[--]>", sample=PRand(0, 3), amp=4).mpan(range(6))

b2.fadeout(32)

k1.sfadeout(32)

d4 >> play(
    "-o**",
    dur=PTri(16)/16,
    amp=3,
    sample=PRand(0, 3),
    amplify=pa16,
    rate=PWhite(.2, 6)[:17]
).mpan(PTri(5).stutter(3))
d1.fadein(16)

d2 >> play(
    "<---(---*)><   =>",
    dur=.25,
    amp=5,
    sample=PRand(0, 3),
    amplify=pa16,
    rate=PWhite(.5, 3)
).mpan(range(6))
# d2.fadein(32)

n1 >> nlead(PTri(4) * 2, dur=.25, root=[2, 4, 0].stutter(16))
