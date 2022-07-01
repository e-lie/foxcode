from FoxDot.preset import *
from FoxDot.lib.Extensions.MidiMapFactory import MidiMapFactory

print(MidiMapFactory.linear_midimap())

change_bpm(120)


sc >> supercollider()
# dd >> ducker(0, sus=.5, ducking=.6)

k1 >> kicker("gGaAbB", dur=.25, verb_size=linvar([.6,.9], 16), vol=.8).humz()
k2 >> kicker2("F", dur=cubalet, verb_size=linvar([.6,.9], 16), vol=.8).humz()

k1.amplify=pa16
k2.stop()

d1 >> crazykit("www.", amp=PWhite(.3,1)[:32], midi_map='linear', dur=cascara, verb_size=.8)
d2 >> crazykit("W", amp=PWhite(.3,1)[:32], midi_map='linear', dur=clave23)
d_all.verb_size=.8
d_all.pitch_full=linvar([.1,.9],16)
d_all.vol=1.2

k2 >> crazykit(" (a[aa])", dur=.5, amp=.7, vol=.6)

m1 >> tb303(
    [0,2,4,-5,2],
    dur=cascara,
    amp=1.2,
    root=var([0,2,0,4], [16,8,8,16,8]),
    scale = Scale.minor,
    oct = 3,
    hpf=000,
)

sc >> supercollider(verb_w=linvar([.6,1], 8), verb_size=linvar([.8,1], 16))

tt >> play("x(---[--])", sample=(0,1), amp=[1.2,.8])
t3 >> play(".(...(.(*[**]*)))", sample=(0,1), amp=[1.2,.8], room=3, dur=.5, sus=4)

t2 >> play("<XvvXv>< (*[**]) >", dur=clave23, sample=P[0,1,2].stutter(4))
t5 >> play("tt", dur=cascara, sample=P[0,1,2].stutter(4))

dd >> ducker(0, sus=.5, ducking=.6)


t2.rate = sinvar([.5,3], 32)

ee >> click(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3, 1], 8), amplify=pa32) + (0,2,4)

e6 >> ratic(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3, 1], 8)).span(srot(16))
e6.fadein(32)

e6.vol = 1.2

e7 >> fordrip([0]).fadein()
e6 >> bnoise([0]).fadein()

d1 >> play("(   (---w))(---( V vV))", amp=linvar([.5,2], 16), sample=var([0,1,2,3], 8), room=linvar([0,6], 32))

d1.crush=32
d1.rate=linvar([1,4],17)

################################################################

m4 >> blip([4], dur=.25, amplify=pa16_2, amp=2, oct=6)
m1 >> blip([12,0], dur=1/3, amplify=pa32, oct=(2,4,6))

################################################################


d1 >> play("(   (---w))(---( V vV))", amp=linvar([.5,2], 16), sample=var([0,1,2,3], 8), room=linvar([0,6], 32))
d2 >> rdrum(PRand(0,32)[:17], dur=cascara, pan=1)
d3 >> rdrum(PRand(0,32)[:17], dur=clave23, pan=-1)
d4 >> play("XxxXV", dur=clave23)

################################################################

change_bpm(110)

pp >> kicker("<c><f>", rate=linvar([1,1.6], 16), dur=1, sample=1, hpf=100, oct=5)
dd >> ducker("a", oct=3, ducking=.4)

t1 >> play("-", dur=.25, amp=3, rate=linvar([1,2], [17,0]), formant=linvar([0,4], 7), crush=linvar([0,64], 4), pan=sinvar([-1,1],8))
t2 >> play("...(...[.*](./))", dur=.5, amp=2, room=3, sample=0)

sc >> supercollider(verb_w=1, verb_size=.8)

sc >> supercollider()
Scale.default=Scale.minor

r1 >> hpluck([0,2,4,0,2], dur=clave23, oct=var([2,4],16), bits=1, scale=Scale.minor)
r2 >> hpluck([0,2,4,0,2], dur=cascara, oct=3, bits=1, scale=Scale.minor) + var([0,4], 16)

r_all.root = var([0,2,0,2,4], 16)
