from FoxDot.preset.com import *


Scale.default = Scale.egyptian
Root.default = var([0,5,3,1,-1])
Root.default = 0

b1 >> blip([0,0,1], dur=4/12, amp=PEuclid(5,12).rotate(-1), oct=[3,6])
b2 >> blip([0,0,2,0], dur=4/12, amp=PEuclid(7,12), oct=[4,8,7])

b3 >> blip([0,0,4,0], dur=2/8, amp=PEuclid(3,8), oct=[2,5,3,7])
b4 >> noisynth([-1,0,0,1,0], dur=2/8, amp=PEuclid(5,8), oct=[3,4,5,6,7])

b_all.sus = var(PWhite(.1,3)[:16], 1)
b_all.amplify=2

d1 >> play("<X( -  )><.((^.=.)   )><.((..[==])..)>", dur=cascara, sample=var([0,2,3], 8)).mpan(var([0,4], 16))
d2 >> play("<X( -  )><.((^.=.)   )><.((..[==])..)>", dur=clave23, rate=linvar([1,3],32), sample=var([1,2], 5)).mpan(var([1,3], 16))

d_all.stop()

d_all.pause(4,16)

b1.pause(16,64)
b2.pause(16,64,12)
b3.pause(16,64, 24)
b4.pause(16,64)
