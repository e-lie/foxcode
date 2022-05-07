from FoxDot.preset import *

l1 >> loop("004_Drum_Loop", dur=4, rate=1.2).mpan(range(6))

p1 >> play("x", sdb=1, sample=range(10)).mpan(range(6))
