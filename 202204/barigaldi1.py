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

d1 >> play(
    # "* ",
    # degree="<*><[--]><w>",
    # degree="V",
    degree="<w w><TTT>",
    # sample=0,
    sample=range(5),
    dur=cascara,
    # amp=1,
    # dur=PTri(1, 32)/32,
    # dur=Pvar([PTri(1, 16)/16, .5], [24, 8]),
    amp=PWhite(.8, 2)[:17],
    # formant=0,
    # rate=P[.3, 1, 4, 7].stutter(5),
    # rate=P[.2, 7].stutter(5),
    # room=linvar([0, 2], 16),
    formant=0,
)
# d1.fadein(12)
# d1.only()
# d1.mpan(PTri(5))
# d1.mpan(range(6))
# d1.mpan([4])
# d1.mpan(PTri(0, 15, 2))
# d1.mpan(PTri(5).stutter(2))
d1.mpan(PTri(5).stutter(5))

d2 >> play(
    degree="w",
    sample=2,
    dur=PTri([16, 32])/32,
    amp=PWhite(.8, 2)[:17],
    formant=1,
    room=linvar([0, 2], 16),
    # formant=sinvar([0, 1], 7),
)
d2.fadein(32)
d2.mpan(PTri(5))

d1.dur = 1

d2.mpan(PTri(5).stutter(7))

k1 >> kicker(
    # degree="d",
    degree="<d><jJ>",
    # degree="J",
    sample=2,
    # dur=1,
    dur=PTri([7, 17, 27])/64,
    # dur=
    amp=PWhite(.8, 1)[:17],
    formant=0,
)
k1.fadein(32)
k1.span(rot16)
# k1.sfadeout(16)
k1.only()
# k1.sfadein(16)

################################################################
