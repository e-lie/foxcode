
from .Extensions.VRender import vrender

b1 >> multibass(PWalk()[:65], dur=1/4, oct=3)



b1 >> crubass(PWalk()[:65], dur=1/4, oct=3)



b1 >> balafon(PWalk()[:65], dur=var([1/4, 1/3, 1], 8), oct=6)
b1 >> balafon(PWalk()[:65], dur=var([1/4, 1/3, 1], 8), oct=6, amp=var([1,0],[6,2]))
b1 >> balafon(PWalk()[:65], dur=var([1/4, 1/3, 1], 8), oct=6, amp=var([1,0],[6,2]), delay_vol=.5)
b1 >> balafon(PWalk()[:65], dur=var([1/4, 1/3, 1], 8), oct=(5,6,7), amp=var([1,0],[6,2]), delay_vol=.5, pan=sinvar([-1,1],16), vol=.8)

b2 >> tb303_2(PWalk()[:65],
               dur=var([1/4, 1/3, 1], 8), oct=3, tb303_i_freq=linvar([.1,.6],8),
               tb303_i_reso=sinvar([.6,1], 12), tb303_reverb_dw=linvar([0,.5], 6),
               pan=sinvar([1,-1],16), vol=.8)

d1 >> jazzkit([0,4,12], dur=[.5,1,.3,1.2], sus=.1, reverb_dw=.3, resob_dw=.3)
d1 >> jazzkit([0,4,12], dur=P[.5,.2,.2,.6,.3,1.2]*2, sus=.1, reverb_dw=.3, resob_dw=.3)
d1 >> jazzkit([0,4,12], dur=PWhite(.2,1.2)[:67], sus=.1, reverb_dw=.3, resob_dw=.3)

help(live.track)

# vrender([0,2,0,4], file="wavName", lyrics="hey ho lets go", dur=[1,1,1,1], sex="male") # Generate voice audio file
