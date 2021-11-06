import live
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
ab = SmartSet(Clock, set)
kitcuba = Instruc(smart_track=ab.kitcuba, midi_channel=1, scale=Scale.chromatic, oct=3).out
kicker = Instruc(smart_track=ab.kicker, midi_channel=2, scale=Scale.chromatic, oct=3).out
kitdatai = Instruc(smart_track=ab.kitdatai, midi_channel=3, scale=Scale.chromatic, oct=3).out
ubass = Instruc(smart_track=ab.ubass, midi_channel=4, oct=4, scale=Scale.major).out
crubass = Instruc(smart_track=ab.crubass, midi_channel=5, oct=4, scale=Scale.major).out
strings = Instruc(smart_track=ab.strings, midi_channel=6, oct=5, scale=Scale.major).out
owstrings = Instruc(smart_track=ab.owstrings, midi_channel=7, oct=5, scale=Scale.major).out
balafon = Instruc(smart_track=ab.balafon, midi_channel=8, oct=6, scale=Scale.major).out
bells = Instruc(smart_track=ab.bells, midi_channel=9, oct=6, scale=Scale.major).out
kora = Instruc(smart_track=ab.bells, midi_channel=9, oct=6, scale=Scale.major).out

Clock.bpm = 120
Clock.midi_nudge = 0.29 # bpm 120

Clock.bpm = 130
Clock.midi_nudge = 0.22 # bpm 120

Clock.bpm = 140
Clock.midi_nudge = 0.19 # bpm 140

################################################################

base1 = var([0,2,0,4],4)
root1 = var([0,4,2,0],16)

bin3 = P[1/2,1/4,1/4]
gnawa = P[4/10,3/10,3/10]
ter3 = P[1/3,1/3,1/3]

b1 >> crubass(base1, dur=PSum(3,2), oct=3, root=root1, scale=Scale.minor, vol=.9)

p1 >> kitcuba(PRand(range(20))[:32], dur=gnawa, amp=Pvar([[1,.5],0],[6,2]))

k1 >> kicker(1, dur=1, oct=3, amp=var([1,0],[12,4])).every(8, "stutter", 3)

s1 >> strings(base1, dur=2, oct=4, root=root1, scale=Scale.minor, vol=.8, amp=var([1,0], [12,4]), i_release=.8 )

k1.only()

################################################################

base2 = var([0,4,1,4,0,2,4,2],2)
root2 = var([0,6],16)
scale2 = Pvar([Scale.minor,Scale.major],32)

d1 >> play(" (---[oo])", sample=var([2,3,4],1), amp=.2)
k1 >> kicker([6,(4,12)], dur=1, oct=3, amp=var([1,0],[28,4])).every(16, "stutter", 2)

b1 >> crubass(base2, dur=PSum(5,3), oct=3, root=root2, scale=scale2, vol=.9, i_cutoff=sinvar([.3,1], 8), i_intensity=sinvar([.3,1], 32), i_wt_pos=sinvar([0,1], 8))
b2 >> ubass(base2, dur=PSum(5,3), amp=1, oct=3, root=root2, scale=scale2)


################################################################

def part1():
    k1 >> kicker([6,(4,12)], dur=1, oct=3, amp=var([1,0],[28,4])).every(16, "stutter", 2)
    Clock.future(32, part2)
def part2():
    k1 >> kicker(1, dur=1, oct=3, amp=var([1,0],[12,4])).every(8, "stutter", 3)
    Clock.future(32, part1)
    # Clock.future(32, stoploop)
def stoploop():
    k1.stop()
part1()
