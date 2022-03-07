from FoxDot.preset import *

change_bpm(120, True, 0.26)
bb >> mixer()
ss >> sends()

Scale.default = Pvar([Scale.minor, Scale.major], 16)

d1 >> jazzkit([2,3,4], dur=1/3, amplify=var([1,0],[8,8]), sreverb=.7)
d1.fadein(4)
d1.phaser_dw = .5
d1.human()

presets["reverb_default"]["reverb_dw"] = 0
reverb_full = presets["reverb_default"].copy()
reverb_full["reverb_dw"] = 1
reverb_full["reverb_decay"] = 1

pp >> kit808([0,1,2])
pp.top(phaser_default, 16)

print(phaser_default)

pp.showp("phaser")

print(getattr(pp, "reverb_dw"))

print(presets["reverb_default"])

pp.setp(interpolate_params(presets["reverb_default"], reverb_full, 16))
pp.setp(interpolate_params(reverb_full, presets["reverb_default"], 16))


monp = P[0,1,2,3,4,5,6]

pp >> piano(monp[:7], dur=cubalet[:4], oct=7, amp=PWhite(.5,.8)[:17])

d1.showp("phaser")

k1 >> kicker((3,1), amplify=var([1,0], 4), ssc=.6)

n1 >> piano(PWalk()[:17], dur=[4,3, 1/4,1/4, 1/4, 1/4], oct=(3,6), vol=.9, sreverb=.8)

n1.stop()

b1 >> crubass(PWalk()[:17], dur=2, vol=.7, oct=var([2,3], 16), sreverb=.8)

o1 >> owstr([0,2,3,4,0,2], dur=3, oct=2)
o2 >> owstr([4,0,0,2,4,0], dur=3, oct=6, vol=.8)
