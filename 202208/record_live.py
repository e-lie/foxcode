from FoxDot.preset import *


reverb = ['ReaVerbate', 'reverb', 'verb base', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]
sur = ['ReaSurround', 'sur', 'hexa_spatial', {"in 1 X":"x", "in 1 Y":"y"}]
limit8 = ['ReaLimit', 'limit8', 'limit8', {}]
lpf = ['ReaEQ', 'lpf', 'lpf', {"Freq-Low Pass 4":"freq", "Q-Low Pass 4":"bw", "Gain-Low Pass 4": "gain"}]
hpf = ['ReaEQ', 'hpf', 'hpf', {"Freq-High Pass 1":"freq", "Q-High Pass 1":"bw", "Gain-High Pass 1": "gain"}]

hamp = ['ReaVerbate', 'reverb', 'testounet', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]
# delay = ['ReaVerbate', 'reverb', 'testounet', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]

marimba = newintru(plugin_name='kontakt', name='marimba', params={}, effects=[reverb, lpf, hpf, sur, limit8])

vibra = newintru(plugin_name='kontakt', name='vibra', params={}, effects=[reverb])
hpluck = newintru(plugin_name='vital', name='hpluck', params={"Macro 1":"width", "Macro 2":"drive", "Macro 3":"reverb", "Macro 4":"release"}, effects=[reverb])
fordrip = newintru(plugin_name='vital', name='fordrip', params={"Macro 1":"bit_crush", "Macro 2":"drip", "Macro 3":"psy", "Macro 4":"ambiance"}, effects=[reverb])
whibot = newintru(plugin_name='vital', name='whibot', params={"Macro 1":"wash", "Macro 2":"warp"}, effects=[reverb])
darkpass = newintru(plugin_name='vital', name='darkpass', params={"Macro 1":"rm", "Macro 2":"detune", "Macro 3":"sustain", "Macro 4":"reverb"}, effects=[reverb])

240 -> .01


m1 >> marimba("aabb", lpf_freq=sinvar([500,4000],.5)/24000, lpf_bandwidth=.1, dur=cascara, oct=[2,5,8], root=var([-2,4,0,0,-5,0]), reverb_wet=0, reverb_size=.9)
m1.span(2)
m1.dur=.125


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
def d():
    d3 >> play("s", amp=2, dur=P[.5,.25,.25]<<[0,.13,.06, 0, .09, .05])
    d1 >> play("(XXX[ X]) ", amp=3, dur=.5, rate=1.2, lpf=linvar([200,1000],[32,inf], start=Clock.mod(4)), sample=P[0].stutter(4), crush=2, bits=4)
