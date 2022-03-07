from FoxDot.preset import *


change_bpm(110, True)
bb >> mixer()
ss >> sends()
sa >> sca()
sb >> scb()
sc >> scc()

m1 >> marimba([0,1,-5], amp=1, oct=4, reverb_dw=.6) + var([2,4,5], 4)
m1.fadein(16)
m1.root=var([0,2],12)
m1.hamp_dw=sinvar([.1,.3],32)

r1 >> kit808("=-")
r1.degree="=(-[--])"
r1.phaser_dw=.4
r1.degree="<=(-[--])><w w>"


r2 >> play("<X ><o (ooo\)>", dur=gnawa, output=2, amp=[.6,1], sample=var([0,1],16))
r2.amplify = var([1,0], [24,8])

r1.amplify = var([1,0], [24,8])

t1 >> owstr([0,2,4], dur=4)

t1.setp(owstr_1)
