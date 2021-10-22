


lowcase = list(range(97,123))
upcase = list(range(65,91))
base_midi_map = {'default':0}
for i in range(52):
    if i % 2 == 0:
        base_midi_map[chr(lowcase[i//2])] = i
    else:
        base_midi_map[chr(upcase[i//2])] = i

drumm = Instruc(7, 4, Clock)
drumm2 = Instruc(7, 4, Clock)

d1 >> drumm.init("a(aB)(aaah)", oct=3, dur=P[4/10,3/10,3/10]*1.5, midi_map=base_midi_map)

d2 >> drumm2.init

d1 >> MidiOut(range(53), channel=6, oct=3, scale=Scale.chromatic, dur=PWhite(0.2,1)[:200], amp=PWhite(0.2,1)[:200])
# d1 >> drumm.init("(0[11])", oct=PRand(3,6)[:16], dur=[4/10,3/10,3/10], amp=PWhite(0.4,0.9)[:32])

print(ord("A"))


d2 >> play("X ", sample=2)
