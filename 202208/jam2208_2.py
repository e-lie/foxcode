from FoxDot.preset import *

vital1 = newintru(
    plugin_name='vital',
    name='init',
    params={
        "Macro 1": "macro1",
        "Macro 2": "macro2",
        "Macro 3": "macro3",
        "Macro 4": "macro4"
    },
    effects=[sverb]
)

sc >> supercollider(glitch_dw=0)
^

t1 >> candy([0,0,2,2,-2,4,0], dur=PSum(3,2), sverb_dwarp=var(PWhite(0,1), 2), sverb_fb=sinvar([0,1], 8))
d1 >> play("+", dur=var([.25, 1 / 3, 1 / 5]), sample=(0,1)).mpan(mrot(64))
d3 >> play("*", dur=cascara, amp=3, amplify=1, rate=PWhite(4,7)).mpan([0,1,2,4,3])
d4 >> play("<v>", dur=clave23, amp=1, amplify=1, rate=var([.9,1.1],8), sample=var([0,4],7)).mpan(.5)

d3.formant = linvar([1,8])
d4.formant = linvar([0,2], 16)

d1.dur = Pvar([P[.25] << [.05,.1,0,0], gnawa, 1 / 5])

t2 >> candy([0,0,2,2,-2,4,0], dur=.25, oct=7)

t2.shuffle()
t2 + P*(0,4)
t2.oct = [4,5,6]



t1 + [0,2,-2]
t1.oct = 5
t1.dur = .25

Scale.default = Pvar([Scale.major, Scale.minor, Scale.chromatic], [12,12,8])
