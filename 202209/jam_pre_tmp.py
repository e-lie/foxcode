from FoxDot.preset import *

effects1 = [
    ['kverb1', 'kverb'],
    ['lpf2', 'lpf'],
    ['hpf2', 'hpf'],
    ['sur6_1', 'sur'],
    ['limit8_1', 'limit8'],
]

effects2 = [
    # ['kverb1', 'kverb'],
    ['lpf2', 'lpf'],
    ['hpf2', 'hpf'],
    ['sur6_1', 'sur'],
    ['limit8_1', 'limit8'],
]

marimba = newintru('marimba', 'marimba1', effects=effects1)[0]
darkpass = newintru('darkpass', 'darkpass', effects=effects1)[0]
growlside = newintru('growlside', 'growlside', effects=effects1)[0]
candy = newintru('candy', 'candy1', effects=effects2)[0]

################################################################

Scale.default = Pvar([Scale.major, Scale.minor, Scale.egyptian], 16)

Scale.default = Scale.chromatic

Root.default = var([0,2,-2,4,2])

p1 >> candy([0,0,-2], dur=[1,1,1,2])
p2 >> candy([0,0,-2], dur=P[1,1,1,2]/2, oct=6)

p3 >> marimba([0,0,-2], dur=1/4, oct=[4,6,7])

p5 >> marimba([0,0,-2], dur=1/8, oct=8, amp=linvar([0,1], 8))

p1.pause(4,17)
p2.pause(8,20,3)
d1.pause(8,20,7)
d2.pause(8,20,17)

d1 >> play(" (----[--]--[---])", sample=[0,0,0,2,1,0,(0,2)], dur=var([1/4,1/2],8))
d2 >> play("(XxxV.).", sample=[0,0,0,2,1,0,(0,2)], dur=var([1/4,1/2],8))

d2.pause()

d_all.crush=linvar([0,16],16)

################################################################

Scale.default = Scale.major
Root.default = 0

change_bpm(150)

b1 >> darkpass([0,2], dur=5, oct=var([3,4],16), darkpass_rm=linvar([0,1], 7))
b2 >> darkpass([0,2], dur=3, oct=var([5,6,4],7), darkpass_detune=linvar([0,1],9))

b3 >> growlside([0,4], dur=8, oct=3)

d1 >> play("Vv", dur=1/4, amp=1)
d2 >> play("O*[Oo]*O.[OO]", dur=brafflet, amp=1)

d2 >> play(" (o[---])", dur=1, amp=linvar([0,1.2],16))
d3 >> play(" *", dur=cascara, amp=linvar([0,1.2],16))
d3 >> play("*", dur=cascara, amp=linvar([0,1.2],16))
d4 >> play("x", dur=clave, amp=1)

b_all.fadeout()

d1 >> play("Vv", dur=1/4, amp=.5)

d2 >> play("O*[Oo]*O.[OO]", dur=brafflet, amp=1)

d2 >> play("*", dur=P[.5,.25,.25] << P[0,.1,.05], amp=.8, )

d1 >> play("Vv.V", dur=1, amp=.8, )

print(P[.5,.25,.25] << P[0,.1,.05])

d2 >> play("V", dur=clave23, amp=1)

d_all.sample = var([0,2,4,1],8)

d_all.crush = linvar([0,64],8)

d_all.bits = linvar([16,2],32)

m1 >> marimba([0,2,-2,1], dur=cascara, oct=4)

################################################################

d1 >> rdrum("abEdcc", dur=cascara)
d2 >> rdrum("abEdcc", dur=cascara*2)

d3 >> rdrum("d", dur=1/4)
d4 >> rdrum("D", dur=clave23)
