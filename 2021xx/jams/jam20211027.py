import live
Clock.bpm = 110
Clock.midi_nudge = 0.35

set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
ab = SmartSet(Clock, set)
kit909 = InstrumentFacadeClockless(Clock, smart_track=ab.kit909, midi_channel=2, oct=3).out
sawbass = InstrumentFacadeClockless(Clock, smart_track=ab.sawbass, midi_channel=3, oct=5, scale=Scale.major).out
strings = InstrumentFacadeClockless(Clock, smart_track=ab.strings, midi_channel=4, oct=6, scale=Scale.major).out
bells = InstrumentFacadeClockless(Clock, smart_track=ab.bells, midi_channel=5, oct=6, scale=Scale.major).out
kitdatai = InstrumentFacadeClockless(Clock, smart_track=ab.kitdatai, midi_channel=6, oct=3).out
opbass = InstrumentFacadeClockless(Clock, smart_track=ab.opbass, midi_channel=7, oct=4, scale=Scale.major).out



ch = var([0,5,2,3],[8,4,2,2])
bb >> sawbass(ch, dur=PSum(3,2), sus=PSum(3,2)-0.05, oct=(2,3), pan=var([-1,1]), vol=.6, scale=Scale.major)

vv >> strings(ch + [[2,0,0],0,[0,2,2],[0,0,2]], dur=ch.dur,
            oct=(3,4)) + var([(0,2),(2,4)],[28,4])

vv.amp=var([.7,0],[48,16])

b1 >> opbass([0,2,2,3], dur=P[3,3,5,5]/8, oct=3, sus=P[3,3,5,5]/8-0.05, root=var([0,2,5,0]))
b1 >> opbass(Pvar([[0,2,0,2,3],[0,0,3,2,3]],8), dur=PSum(5,3), oct=2, sus=PSum(5,3)-0.05, root=var([0,2,0,5], scale=Scale.majorPentatonic))

b1 >> opbass(Pvar([[0,1,4,0,1,4,4,0],P[0,2,4,0,5,4,4,0].reverse()],16), dur=Pvar([PSum(6,4), PSum(5,4)], 12), oct=2, sus=Pvar([PSum(6,4)-0.05, PSum(5,4)-0.05], 12), root=var([0,1,4,0],4), scale=Scale.majorPentatonic)
d2 >> play("<V ><X >", dur=1/2, sample=2)


d1 >> play("o-o---o----=", dur=[4/10,3/10,3/10], amp=[.8,.8,1.5])

print(PSum(5,3))

A = var([1,0],[16.5,15.5])
zz >> zap([3,2,0], dur=1/3, sus=1/2, amp=A*2, pan=1) + [0,[0,(0,2),0],0]
pp >> pluck([0,2], dur=1/4, sus=1/2, amp=A, pan=-1) + [0,0,[0,0,1]]

be >> bells([2,1,0,2,3], dur=1/2, oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])
be >> bells([2,1,0,2,3], dur=PSum(5,4), oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])

d1 >> kitdatai([0,1,2], channel=2, dur=1/2, scale=Scale.chromatic)

Scale.default.set(Scale.chromatic)
