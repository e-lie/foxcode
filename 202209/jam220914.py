from FoxDot.preset import *


Scale.default = Scale.majorPentatonic

d1 >> bbass([0,1,2,-2,-2], sus=3, oct=var([3,4,3,4], [8,8,12,4]), crush=linvar([0,64], 16))

d2 >> blip([0,1,2,-2,-2], dur=1/8, amplify=pa32_2, sus=linvar([.1, 1]), amp=linvar([.5,1], 16), oct=var([4,5,8,6], [8,8,12,4]), crush=linvar([0,64], 16))

d3 >> play("lululu", dur=clave23, amplify=pa32, amp=2, crush=linvar([0,4])).solo(0)

d4 >> play("V.[xx].", amp=4)

d5 >> click([0,4], oct=(3,4), dur=cascara, amplify=pa16)

d_all.stop()
