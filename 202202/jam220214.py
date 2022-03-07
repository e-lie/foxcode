from FoxDot.preset import *

change_bpm(120, True, 0.26)
bb >> mixer()
ss >> sends()

mmdur = [1,1,1]+[1/4]*3+[1/8]*3
mm >> marimba([0,2,4], dur=mmdur) + var([(2,5), (0,4)], 8)

mm.showp("hpf")

Root.default = var([0,2,0,4], 36)

d1 >> harshkit(
    [0,5],
    dur=gnawa,
    amp=PWhite(.5,1)[:17],
    reverb_dw = .5,
)



d1.solo()

b1 >> crubass(
    [0, 3, 4],
    dur=4,
)

b2 >> owstr([0,2,4], dur=PSum(3,5)*2, oct=5)

k1 >> kicker(12, ssc=.8)
