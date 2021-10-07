

print(SynthDefs)

cc >> swell(P[I, IV, I, V, IV], dur=P[4, 4, 4, 2, 2], amp=PRand([1, 0.5, 0.8, 1]), room=1, mix=0.3)

cc.stop()

cc >> pluck(P[P+(I), P+(IV), P+(V)], dur=2, sus=P[1, 2/3, 1/2], room=1, mix=0.3, amp=2)
