from FoxDot.preset.common import *
from FoxDot.preset.reaper import *

Scale.default = Scale.phrygian
Scale.default = Scale.egyptian

bb >> bbass([0,2,4])

pp >> play("<x>< -(   *) ><truc>", dur=.25, rate=linvar([.5,2],4))

pp.dur = mimov(mimov(cascara, 2, -0.05), 4, -0.05)
pp.sample = 0
pp.amp=.4

print(cascara)

p2 >> play("<--- ><X (vvv )>", sample=2, dur=brafflet, amp=.7, amplify=pa16)
p2.dur = mimov(mimov(brafflet, 2, -0.05), 4, -0.05)


Clock.bpm = 100

p1 >> play("-", dur=.25, rate=sinvar([.5, 2], 16))
p2 >> play("===", sample=1, dur=cubalet).stop()
p2 >> blip([0,2,-1], dur=cubalet, sus=linvar([.1, .5], [16,0]), crush=8, oct=3)
p3 >> play("-", sample=2, dur=clave23)
p4 >> play("x", sample=3, dur=cascara)

b1 >> play("x", dur=[.5, .25, .25])
b1 >> play("x", dur=cubalet)

b1 >> play("x", dur=[1/3])






dur1 = [1/3]*3
dur2 = mimov([1/3]*3, 0, .12)
dur3 = mimov(dur2, 2, -.12)

cubaa = (
    mimov(cubalet, 1, -0.02)
    | mimov(cubalet, 1, -0.05)
    | mimov(cubalet, 1, 0.02)
)

print(cubalet)

b1 >> play("-", dur=cubaa, sample=0)
# b1.rate = PWhite(.7,1.5)[:17]
# b1.crush = var([0,2,0,8,0,32], 8)
b2 >> play("V(  [ i](i[ii][ i][ii]))", dur=mimov([1/2]*2, 0, -.05 ))


b1 >> play("-", dur=mimov(P[1/2]|P[.25,.25], 1, -.02 ), sample=0)
# b1.rate = PWhite(.7,1.5)[:17]
# b1.crush = var([0,2,0,8,0,32], 8)
b2 >> play("V(  [ i](i[ii][ i][ii]))", dur=mimov([1/2]*2, 0, -.02 ))

b2 >> play("V(  [ i](i[ii][ i][ii]))", dur=mimov([1/2]*2, 0, -.02 ))


b1.stop()
b2 >> play("<V(  [ i](i[ii][ i][ii]))><-[--]>", dur=.5)

b2.amp=.8

b3 >> play(" =  = = =", dur=cascara).stop()

C = var([0,2,-2,4], [8,4,2,2])
m1 >> pluck(C, oct=4, amp=sinvar([.1,.9],32), dur=cubaa)
m2 >> blip(C, oct=5, amp=sinvar([.1,.9],16), dur=mimov([1/2]*2, 0, -.05 ))
m3 >> marimba(C, oct=6, amp=sinvar([.1,.9],24), dur=cascara)

vari1 = [[0,2,(0,2),-2,0,4,(0,4),1]]
vari2 = [[0,2,(0,2),(0,4), [0,2,4]]]
vari3 = [[[0,(-2,2)],0,[0,2],[0,2,4]]]

for mplay in [m1, m2, m3]:
    mplay + vari2

vari0 = [0,P*(0,2),P*(-2,4,0),0]
m1 + vari0

m_all.sus=linvar([.2, 1.5], 16)

m3.oct=P[4,6,7].stutter(2)

m1.solo()

print(clave23)

m_all.span(srot(17))

################################################################
