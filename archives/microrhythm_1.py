Clock.bpm = 120

d1 >> play("<5[f[ f]--]>")


p1 >> bass([0,4,5,3], dur=4, amp=0.3)
p2 >> pluck([0,4,7,9], dur=1/4, amp=[1, 0.3, 0.3, 0.3])


aa >> play("<4[ftf2[tf[tt]]]>", dur=1)

# Equivalent rhythm using variable duration instead of pgroup+ spread on sustain value
aa >> play("ftftftt",
            dur=4*(P[1/5, 1/5, 1/5]|2/5*(P[1/3, 1/3]|1/6*P[1,1])),
            amp=P[4]|[2]*6
        )


ac >> play("x - x - ", amp=4)

ac.stop()


a2 >> MidiOut([4, 8], dur=1, oct=4, amp=0.5, channel=1)
a2 >> MidiOut([4, 8], dur=1, oct=4, amp=0.5, channel=1)

Clock.midi_nudge=0.07
