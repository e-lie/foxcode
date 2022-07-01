from FoxDot.preset import *

Scale.default=Scale.minorPentatonic

d1 >> play("@", sdb=1, sample=8, dur=16)
d2 >> play("~  ~ ", sdb=1)
d3 >> play("^ ^  ", sdb=1, sample=[0,1,2])
d4 >> play("([--]-.)", sdb=1, sample=5)
d5 >> play("V VV ", sdb=0, dur=clave23)

l1 >> loop("200173-breakbeat5", dur=4, amp=.7, rate=linvar([1,2],16))



v1 >> ceramic(PWalk()[:15], dur=cubalet, oct=[3,4,5])
