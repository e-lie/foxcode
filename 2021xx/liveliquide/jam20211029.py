Clock.bpm = 130
Clock.midi_nudge = 0.29
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

print(ab.__track_ids)

ab.kitcuba.reverb.dry_wet=sinvar([.6,0],8)

print(ab.crubass.vol)

ch = var([0,5,2,3],[8,4,2,2])
ch = var([0],[4])

#TODO add a new simple bass but with good params
#TODO code instru factory
#TODO create a multibass ableton instrument (combining 3 bass sounds, techno, normal, sub)
#TODO look at atom hotkeys and code snippets

cc >> kitdatai("e((ec)ee(c )((ec)ee(c )))", dur=P[4/10,3/10,3/10], amp=[.6,.3], vol=.6)

b1 >> ubass(0, amp=1 , dur=PSum(3,2), vol=.8)
b2 >> crubass(0, amp=1, dur=PSum(3,2), vol=1)
k1 >> kicker(P(1), amp=var([0,.2],8), vol=1.17)

d2 >> ubass(Pvar([P[0,2,4,2,0], P[0,2,0,6,0]],8), dur=Pvar([PSum(5,2),PSum(3,2)],16), sus=PSum(3,2)-.3, amp=1, oct=3, scale=Scale.minor) # + Pvar([(2,4),(-1,2),(-2,4)],[12,14,4])
dd >> crubass(P[0,2,4,2,0], dur=PSum(3,2), amp=1, oct=3, scale=Scale.minor)
dd >> crubass(Pvar([P[0,2,4,2,0], P[0,2,0,6,0]],8), dur=PSum(3,2), amp=1, oct=3, scale=Scale.minor)
dd >> crubass(Pvar([P[0,2,4,2,0], P[0,2,0,6,0]],8), dur=Pvar([PSum(5,2),PSum(3,2)],16), amp=1, oct=3, scale=Scale.minor)

b1 >> owstrings(Pvar([P[0,2,4,2,0], P[0,2,0,6,0]],8), dur=8, vol=.5)

cc >> kitcuba(PRand(range(20))[:32], dur=P[4/10,3/10,3/10], amp=Pvar([[1,.5],0],[6,2]))
c1 >> kitcuba("A(a )(aA )(TTT[TT])Tt", dur=1/3, oct=3, amp=Pvar([[1,.5],0],[7,3,6]), vol=1, reverb_dry_wet=sinvar([.4,0],8))
c2 >> kicker(Pvar([P(1,1),1],8), dur=1, oct=3, amp=var([1,0],[12,4])).every(8, "stutter", 3)
