from FoxDot.preset import *


def grc(rythm, groove):
    rythm = list(rythm)
    groove = list(groove)
    dur_sum = sum(rythm)
    lcm = math.lcm(len(groove), dur_sum)
    groove *= lcm // len(groove)
    rythm *= lcm // dur_sum
    res = []
    index = 0
    # print(f"{rythm} - {dur_sum}")
    while True:
        # print(f"len ry:{len(rythm)} len gro:{len(groove)}")
        if len(groove) == 0:
            break
        current_rythm = rythm[index%len(rythm)]
        current_dur = 0
        for i in range(current_rythm):
            current_dur += groove.pop(0)
        index += 1
        print(i)
        res.append(current_dur)
    # print(res)
    return res

def PEu(nb_strokes, total, shift=0, base_dur=.5):
    res = []
    accu = 0
    Peu = PEuclid(nb_strokes, total)
    for e in Peu[1:]|Peu[0]:
        accu += base_dur
        if e == 1:
            res.append(accu)
            accu = 0
    if shift > 0:
        res = [Rest(base_dur*shift)]+res[:shift]+res[:-shift]
        res[-1] -= base_dur
    return P[res]

Root.default = var([0,-2,4,0,2])
Scale.default = Pvar([Scale.major, Scale.minor, Scale.egyptian], 8)

b1 >> blip([0,2,-2], dur=grc([1,2,6,2,3,7], P[.4,.3,.3]), oct=[4,5,6]).stop()
b2 >> pluck(0, dur=grc([1,2,1,1,2], P[.4,.3,.3]<<[0,.03,.01]), oct=7, sus=.2)

b2 >> blip(0, dur=grc([1,2,1,1,2], brafflet), oct=7, sus=.2)
b4 >> blip(0, dur=.25, oct=[6,3,5,4], sus=.2)
b3 >> space([0,2,4], dur=grc([1,2,1,1,2], cascara), oct=[4,5], amp=PWhite(.6,1.2))

b_all.sus = linvar([.1,1.5], 16)

d1 >> play("(oo )(---   - -  -)(--- - --)", dur=cascara, sample=0)
d2 >> play("<v><---[--]>", dur=brafflet, crush=linvar([4,32]), rate=sinvar([.2,4],7))

################################################################

b1 >> blip([0,2,-2], dur=grc([1,2,2,2,2,3,2,2,2], cascara), oct=6, amp=PWhite(.6,1.2))
b2 >> pluck([0,2,4], dur=grc([1,2,1,1,2], clave23), oct=3, amp=PWhite(.6,1.2))
d1 >> play("x", dur=cascara, sample=0, rate=PWhite(.7,2), amp=1, crush=PRand(0,16))

d2 >> play("<(vvvV)(==*[**])><(xx[xx][xx]) >", dur=.5, sample=3)


################################################################

d2 >> play("<(vvvV)(==*[**])><(xx[xx][xx]) >", dur=.5, sample=3)
d3.stop()

d2.stop()

d2 >> play("<(==*[**])>", sample=3, dur=PEu(5,12)/2)
d3 >> play("<(vvvV)><(xxx[xx])>", sample=3, dur=PEu(7,12)/2)
b1 >> blip([0,2,-2], dur=grc([1,2,2,2,2,3,2,2,2], PEu(7,12)/2), oct=6, amp=PWhite(.6,1.2))
b2 >> bbass([0,2,-2], dur=grc([1,2,1,1,1,3,1,2], PEu(5,12)/2), oct=3, amp=PWhite(.6,1.2))

################################################################

b1.amplify=pa16
b2.amplify=pa16_2
d1.amplify=pa32
d2.amplify=pa32_3

################################################################

b1 >> blip([0,2,-2], dur=grc([1,2,6,2,3,7], brafflet), oct=6)
b2 >> blip([0,2,4], dur=grc([1,2,1,1,2], [1/2]), oct=4)
b2 >> blip([0,2,4], dur=grc([1,2,1,1,2], brazlet), oct=4)
# b3 >> blip([0,2,4], dur=grc([1,2,3,1,4], cubalet), oct=7)
d3 >> play("<(vvvV)=><(xx[xx][xx]) >", sample=var([0,3],16), crush=linvar([0,2]), rate=PWhite(.7,1.5))

#####################And i have to clean th###########################################

print(PEu(7,12,1))
print(PEu(5,12,0),)
grc([1,2,2,1,1,2,1,1,1],
print(PEuclid(5,12))
print(PEuclid(7,12))

b1 >> blip(0, dur=.5, amp=PEuclid(5,12)[0]|PEuclid(5,12)[:-1])
b2 >> blip(0, dur=.5, amp=PEuclid(7,12), oct=4)

b1 >> blip(0, dur=grc([1,2,2,1,1,2,1,1,1], PEu(5,12,1)/2), oct=var([6,8,5,7],1))
b2 >> blip(0, dur=grc([1,2,2,1,1,2,3], PEu(7,12,0)/2), oct=P[3,4].stutter(2))

b2 >> blip(0, dur=.25, oct=[3,4,5,6,7], crush=linvar([0,19]))
b1 >> play("<vvV><->", dur=cascara, crush=linvar([0,16]))
b1.mpan(P[range(6)].stutter(4))

b2.pause(8,32)
b1.pause(8,32, 12)
b2.pause(8,32)


b1.mpan(range(6))
b2.mpan(range(6))
d1.mpan(range(6))
d3.mpan(range(6))
d2.mpan(var([2,5]))
b3.mpan(range(6))

b1 >> blip(0, dur=var([.25,1/3,.5,.75,1],4), oct=P[range(6)]+2, sus=linvar([.1,3],8)).mpan(range(6)).pause(8,32)

d1 >> play("< (---=)><..(*.***.[**])>", amp=3)
d2 >> play("(x x[vv] x x xv[VV] x).", amp=1)


b1 >> blip(0, dur=cascara, oct=P[range(10)]+2, sus=linvar([.1,2])).mpan(range(6))
b4 >> blip(0, dur=clave23, oct=P[range(10)]+2, sus=linvar([.1,2])).mpan(range(6))
b2 >> bbass(0, dur=cascara, oct=P[range(6)]+2, crush=linvar([0,16])).mpan(2)

print()

################################################################
## Fix PEu
################################################################

print(PEu(5,8))

tt >> blip(0, dur=P[.5, Rest(.5), .5, .5, Rest(.5), .5, .5, Rest(.5) ])
