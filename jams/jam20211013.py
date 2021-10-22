
Scale.default = Scale.major
Clock.bpm = 120

Clock.midi_nudge = 0

set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)

mixer_track = set.tracks[0]
supercollider_track = set.tracks[1]
dj_master_chan = mixer_track.devices[1]
eq_low = dj_master_chan.parameters[1]
eq_mid = dj_master_chan.parameters[2]
eq_low = dj_master_chan.parameters[3]

balafon=Instruc(1, 5, Clock)
kit808=Instruc(3, 5, Clock)

triolet = P[1/3,1/3,1/3]
gnawa = P[4/10,3/10,3/10]
binaire = [1/2,1/4,1/4]
interpol = Pvar(interpolate(triolet, binaire, step=6))

# ---------------------------

d1 >> play("---", sample=2, amp=[1.5, 1, 1], dur=binaire)
d1 >> play("---", sample=2, amp=[1.5, 1, 1], dur=gnawa)

d2 >> play("o ", sample=3)

d1 >> play("<P ><--->", sample=2, amp=[1.5, 1, 1], dur=gnawa)

d3 >> bass(var([0,[1,-1],8]), dur=triolet)
d3 >> bass(var([0,[1,-1],8]), dur=triolet) + [0,4,const(7)]
d3 >> bass(var([0,[1,-1],8]), dur=gnawa) + [0,4,const(7)]

d3.stop()

d1 >> play("<P ><--(---X)>", sample=2, amp=[1.5, 1, 1], dur=gnawa)

d2 >> play("(oooV) ", sample=3)
d2 >> play("(oooV)(   [---])", sample=3)

p1 >> balafon.init([0,4,7,9,0,4], oct=6, sus=2, dur=gnawa)
d3 >> bass(var([0,[1,-1],8]), dur=gnawa*2, lpf=linvar([0,1000], 8)) + [0,4,const(7)]

d3 >> pluck(var([0,[1,-1],8]), dur=[4/10,3/10,3/10], lpf=linvar([100,1000], 8), amp=3, oct=3) + [0,4,const(7)]

p1 >> balafon.init([var([0,-1,-1,0]),4,[7,10],9,0,4], oct=6, sus=2, dur=interpol).stop()

b1 >> kit808.init([0], oct=3, dur=1, sus=1/2).stop()


d_all.hpf = var([0, 100, 200, 400, 800], [24,2,2,2,2])

d_all.hpf=0

eq_low.value = 0

@nextBar
def break1():
    d3.solo()
@futureBar(0.5)
# def break2():
    c1 >> play("XXX   ", sample=2, dur=1/3, amp=[1.5,1,1]).solo()
@futureBar(2)
def unbreak1():
    c1.solo(0)
    c1.stop()
