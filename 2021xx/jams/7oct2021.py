Clock.clear()

set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
mixer_track = set.tracks[0]
dj_mastering = mixer_track.devices[1]
eq_low = dj_mastering.parameters[1]

set_param(eq_low, linvar([0.0,127.0],8))

kit808 = Instruc(3, 3, Clock)
advoca = Instruc(4, 3, Clock)
balafon =  Instruc(7, 6, Clock)

Clock.midi_nudge = -0.08

p1 >> blip([0,5], dur=PDur(3,8))

d1 >> kit808.init([0], dur=1).every(4, "offadd", 2)
b1 >> balafon.init([0,3], dur=PDur(3,8)).every(3, "offadd", 2)

@futureBar(12)
def bal4():
    low_cut = linvar([0.0,127.0],8)
    print(low_cut)
    kit808.set_param(1, low_cut, update_freq=0.1)
@futureBar(14)
def bal4():
    kit808.set_param(1, 127.0)
@futureBar(16)
def bal4():
    kit808.set_param(1, 0.0)

b1 >> balafon.init([0,2,7], dur=[1/2, rest(1/3), 1/3, rest(1/2), 2/3, 2/3], oct=7)

b2 >> play("x ")

b2 >> play("x-o(x-)")

b2.stop()

b1 >> balafon.init([2,7])

b1.stop()

@futureBar(0)
def bal():
    b1 >> balafon.init([0,2,7], dur=[1/2, rest(1/3), 1/3, rest(1/2), 2/3, 2/3], oct=7)
@futureBar(4)
def bal1():
    b1 >> balafon.setup([I, IV, V], oct=6)
    Clock.future(16, bal2)
def bal2():
    b1 >> balafon.setup([I, IV, V, VI, I])
    Clock.future(16, bal1)
@futureBar(10)
def bal3():
    kit808.set_param(1, 0)
    d1 >> kit808.init([0], dur=1)
@futureBar(12)
def bal4():
    low_cut = linvar([0.0,127.0],8)
    print(low_cut)
    kit808.set_param(1, low_cut, update_freq=0.1)
@futureBar(14)
def bal4():
    kit808.set_param(1, 127.0)
@futureBar(16)
def bal4():
    kit808.set_param(1, 0.0)
