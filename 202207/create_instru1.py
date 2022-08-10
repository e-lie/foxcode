from FoxDot.preset import *

reverb = ['ReaVerbate', 'reverb', 'testounet', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]

darkpass = newintru(plugin_name='vital', name='darkpass', params={"Macro 1":"rm", "Macro 4":"reverb"}, effects=[reverb])
marimba = newintru(plugin_name='kontakt', name='marimba', params={}, effects=[reverb])

rdrum = newintru(plugin_name='kontakt', name='rdrum', params={}, effects=[reverb])


p1 >> darkpass([0,4,-2,2,-2], oct=4, dur=4, reverb_size=linvar([.2,.8],8), darkpass_rm=sinvar([0,1],4))
p2 >> marimba([0,4,-2,2,-2], oct=6, dur=cascara, reverb_size=linvar([.2,.8],8))

p3 >> rdrum([2], oct=4, dur=cascara, reverb_size=linvar([.7,.1],12))

p_all.stop()

################################################################


change_bpm(120)

darkpass = reainstru_factory.add_instrument('darkpass', 'vital', params={"Macro 1":"rm", "Macro 4":"reverb"})
accciddd = reainstru_factory.add_instrument('accciddd', 'vital', params={"Macro 1":"reso", "Macro 2":"drive"})
ceramic = reainstru_factory.add_instrument('ceramic', 'vital', params={"Macro 1":"mute", "Macro 2":"tone", "Macro 3":"sus", "Macro 4":"mod"})
marimba = reainstru_factory.add_instrument('marimba', 'kontakt', params={})
vibra = reainstru_factory.add_instrument('vibra', 'kontakt', params={})

p3 >> ceramic([0,1,-2,2,-2], oct=6, dur=cascara, ceramic_tone=linvar([0,1],8), ceramic_mod=linvar([0,1],5)).fadeout()

d2 >> play(" -", amp=3, crush=[0,4,2,8,0])

d1 >> play("V ", amp=2, sample=range(4), rate=sinvar([1,2],[16,0]))

p1 >> darkpass([0,4,-2,2,-2], oct=3, dur=4, darkpass_reverb=linvar([0,1],8), darkpass_rm=sinvar([0,1],4))

p2 >> accciddd([0,1,-2,2,-2], oct=3, dur=2)

d3 >> play("t", amp=2, sample=1, dur=clave23, rate=[1,2,2,1,.8], crush=[4,8,16,32])

################################################################

d3 >> play("t", amp=3, sample=1, dur=clave23, rate=linvar([.6,2],17), crush=32)

m1 >> blip([0,4,2,-2], dur=.25, oct=var([4,5,7,4,3,6],4), root=var([0,-1,2,-2,4,-5,2,0],3))

m2 >> blip([0,4,2,-2], dur=cascara, oct=var([4,5,7,4,3,6],2.5), root=var([0,-1,2,-2,4,-5,2,0],5))

m5 >> vibra([0,4,2,-2], dur=cascara, oct=var([4,5,7,4,3,6],2.5), root=var([0,-1,2,-2,4,-5,2,0],5))

m3 >> ceramic([0,4,2,-2], dur=cubalet, oct=var(P[4,5,7,4,3,6]+2,1), root=var([0,-1,2,-2,4,-5,2,0],5))
