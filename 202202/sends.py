from FoxDot.preset import *
from FoxDot.lib.Extensions.Live import live_set


print([track.name for track in live_set.tracks])



k1 >> kicker((1,6), amp=2)
b1 >> ubass([0,0,2], dur=2, amp=2, oct=4)


d1 >> kit808("www")
