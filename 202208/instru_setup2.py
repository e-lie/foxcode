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

sc1_facade.add_effect_plugin('glitch6_1', 'glitch')
sc1_facade.add_effect_plugin('sverb6_1', 'sverb')

sc2_facade.add_effect_plugin('glitch1', 'glitch')
sc2_facade.add_effect_plugin('sverb1', 'sverb')
sc2_facade.add_effect_plugin('sur6_1', 'sur')

sc3_facade.add_effect_plugin('glitch1', 'glitch')
sc3_facade.add_effect_plugin('sverb1', 'sverb')
sc3_facade.add_effect_plugin('sur6_1', 'sur')


# supercollider 6chan fx groups/chains : glitch6_1, sverb6_1

marimba = newintru('marimba', 'marimba1', effects=effects1)[0]
candy = newintru('candy', 'candy1', effects=effects2)[0]

change_bpm(120)

t1 >> candy([0,0,2,2,-2,4,0], dur=PSum(3,2), sverb_dwarp=var(PWhite(0,1), 2), sverb_fb=sinvar([0,1], 8))

d1 >> play("+", dur=var([.25, 1 / 3, 1 / 5]), sample=(0,1), output=8)
s2 >> sc2(glitch_dw=.05, sverb_dw=.05).span(srot(64))
s2 >> sc2(glitch_dw=linvar([0,.2],8), sverb_dw=0).span(srot(64))

.mpan(mrot(64))

tt >> blip([3,2,0,-2,0,1], dur=.25, sus=.2, amp=[.2,.6,.8,0,1,0,1,.8], lpf=500, amplify=2).mpan(mrot(18))
s1 >> sc1(glitch_dw=0, sverb_dw=0).span(srot(64))

sc >> supercollider(sverb_dw=linvar([0,.3]), glitch_dw=.3)

d3 >> play("*", dur=cascara, amp=3, amplify=1, rate=PWhite(4,7)).mpan([0,1,2,4,3])
d4 >> play("<v>", dur=clave23, amp=1, amplify=1, rate=var([.9,1.1],8), sample=var([0,4],7)).mpan(.5)

d3.formant = linvar([1,8])
d4.formant = linvar([0,2], 16)

d1.dur = Pvar([P[.25] << [.05,.1,0,0], gnawa, 1 / 5])

t2 >> candy([0,0,2,2,-2,4,0], dur=.25, oct=7)

t2.shuffle()
t2 + P*(0,4)
t2.oct = [4,5,6]

t1 + [0,2,-2]
t1.oct = 5
t1.dur = .25

Scale.default = Pvar([Scale.major, Scale.minor, Scale.chromatic], [12,12,8])

d3 >> play("*", dur=cascara, amp=3, amplify=1, rate=PWhite(4,7), output=8, pan=var([-1, 1]))
ss >> sc2(kverb_dw=.5, kverb_size=.7, glitch_dw=sinvar([.1,.4], 16)).span(srot(16), .5)
