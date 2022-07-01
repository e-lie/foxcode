
# elec: space, blip, click, vibass, sinepad, laserbeam, virus, sillyvoice
# lead: noisynth, epiano, square, faim2
# mallets: tubularbell, rissetobell
# borgan, harp,
# pads: drone
# Basses: tb303, acidbass, bbass, filthysaw, mhping, noquarter
# melodic noise: spick, alva
# Noise: bnoise, hnoise, glitcher, shore

# Effects : room, bits, crush, fmod, chop, tremolo, echo, flanger, formant,
# shape, drive, tanh, chorus, dubd, tek, krush, drop, squiz, triode, shift,
# lofi, room2

change_bpm(120)

sc >> supercollider()
Scale.default=Scale.minor

r1 >> hpluck([0,2,4,0,2], dur=clave23, oct=2, bits=1, scale=Scale.minor)
r2 >> hpluck([0,2,4,0,2], dur=cascara, oct=3, bits=1, scale=Scale.minor) + (0,2,4)

r_all.root = var([0,2,0,2,4], 16)

pp >> play("Vvvv", rate=linvar([1,1.6], 16), dur=.25, sample=1, hpf=100)
p3 >> play(" (---[ (-*)])", amp=2, rate=linvar([1,1.6], 16), dur=.5, sample=1, hpf=100)

sc.sfadeout(16)

################################################################

from FoxDot.preset import  *

# marimba, vibra, ceramic
#
# acccidbass
# nlead
# fordrip, insiders, whibot, ratic, irise
# crazykit, kicker, rdrum
# lofijoy, strpad

b1 >> hpluck([0,0,2], oct=4, dur=cubalet).humz()
blip
pp >> kicker("<c><f>", rate=linvar([1,1.6], 16), dur=1, sample=1, hpf=100, oct=5).solo(0)
dd >> ducker("a", rate=linvar([1,1.6], 16), dur=1, sample=1, hpf=100, oct=3)

t1 >> play("-", dur=.25, amp=3, rate=linvar([1,2], [17,0]), formant=linvar([0,4], 7), crush=linvar([0,64], 4), pan=sinvar([-1,1],8))
t2 >> play("   [ *]", dur=.5, amp=2, room=3)

sc >> supercollider(verb_w=1, verb_size=.93)

i2 >> whibot([0,0,2], dur=16, oct=3, vol=1.2).span(srot(8), linvar([0,1],16)).fadein()
i1 >> ratic2([0,0,2], dur=16, oct=3, vol=1.2, verb_w=1, verb_size=1).fadein()


b2 >> play(" (----[ooooooOOO][-*])", amp=2, sample=range(4))

b1 >> blip(PWalk(2)[:16], scale=Scale.minor, dur=.25)
