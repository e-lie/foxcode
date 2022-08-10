from FoxDot.preset import *


reverb = ['ReaVerbate', 'reverb', 'testounet', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]
compost = newintru(plugin_name='vital', name='compost', params={"Macro 1":"phaser", "Macro 2":"formant", "Macro 3":"macro3", "Macro 4":"space"}, effects=[reverb])


d2 >> play("(XXX[ X])", amp=6, dur=.5, rate=1.2, hpf=5000)
d1 >> play("(XXX[ X]) ", amp=3, dur=.5, rate=1.2, lpf=200, sample=P[0].stutter(4), crush=2, bits=4)
d3 >> play("s", amp=2, dur=P[.5,.25,.25]<<[0,.13,.06, 0, .09, .05])
d4 >> play("(V) ", amp=6, dur=clave23<<[0,.1,.05,.05,.1], rate=1.2, hpf=1000)
p1 >> compost([0,-2], oct=3, dur=8)

@nextBar()
def a():
    p1 >> compost([0,-2], oct=3, dur=8).fadein()

@nextBar(16)
def b():
    d2 >> play("(XXX[ X])", amp=4, dur=.5, rate=1.2, hpf=5000).fadein()

@nextBar(32)
def c():
    d1 >> play("(XXX[ X]) ", amp=3, dur=.5, rate=1.2, lpf=200, sample=P[0].stutter(4), crush=2, bits=4)

@nextBar(48)
def c():
    d3 >> play("s", amp=2, dur=P[.5,.25,.25]<<[0,.13,.06, 0, .09, .05])
    d1 >> play("(XXX[ X]) ", amp=3, dur=.5, rate=1.2, lpf=linvar([200,1000],[32,inf], start=Clock.mod(4)), sample=P[0].stutter(4), crush=2, bits=4)
