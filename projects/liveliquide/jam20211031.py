Clock.bpm = 50

k1 >> kitcuba("AT", dur=1/2)

base1 = var([0, 2, 0, 4], 4)
root1 = var([0, 4, 2, 0], 16)

b1 >> crubass(base1, dur=PSum(3, 2))
b1 >> crubass(base1, dur=PSum(3, 2), oct=3, scale=Scale.minor)
b1 >> crubass(base1, dur=PSum(3, 2), sus=1, oct=[
              2, 2, 2, 3], root=root1, scale=Scale.minor, vol=.6, **rndp(crubassp, 8), reverb_dw=sinvar([0, .6], 16))


k1 >> kitcuba("Aa T (ttt[tT])", dur=1/3)
k1 >> kitcuba("Aa T (ttt[tT])", dur=1/3, amp=[1, .6, .8])

Root.default.set(var([0, 2, 4], 16))

k2 >> kicker(1, dur=1)

s1 >> owstrings(0, dur=8, vol=.5, oct=(4, 5), scale=Scale.minor)

k2 >> kicker(1, dur=1, amp=1)
# var([1,0],[12,4]))
k3 >> kicker(1, dur=P[rest(3/10), 1, 1, 1/2, rest(7/10)]/2, amp=1)

s1 >> owstr([0, 2, 6, 0, 4], dur=4, oct=[4, 5, 6]) + \
            Pvar([P(2, 4), P(-1, 2)], 8)


k2 >> kicker([1, 5, 6], dur=1, amp=var([1, 0], [12, 4]),
             root=0).every(8, "stutter", 3).stop()

b1 >> crubass(base, dur=Pvar(interpolate(bin3, ter3, step=8, go_back=False), 2)
              * 2, oct=3, scale=Scale.minor, amp=var([1, 0], [6, 2, 7, 1]))
k2 >> kicker(1, dur=Pvar(interpolate(bin3, ter3, step=8, go_back=False), 2)
             * 2, amp=var([1, 0], [12, 4]), root=0).every(4, "stutter", 2)

k1 >> kitcuba("Aa T (ttt[tT])", dur=gnawa, amp=P[1, .6, .8]+PWhite(0, .2)[:77])

b1 >> ubass(base, dur=PSum(3, 2), oct=4, vol=.8)

c1 >> kitcuba("A(a )(aA )(TTT[TT])Tt", dur=interpolate(
    binlet, triplet, 32), amp=Pvar([[1, .5], 0], [7, 3, 6]))

b2 >> crubass(var([0, 2, 0, 4], 4), oct=3, amp=1,
              dur=PSum(3, 2), scale=Scale.minor)

c1 >> kitcuba("Aa T (ttt[tT])", dur=1/3, amp=[1, .6, .8])

c1 >> kitcuba("A(a )(aA )(TTT[TT])Tt", dur=1/3,
              amp=Pvar([[1, .5], 0], [7, 3, 6]))
c1 >> kitcuba("A(a )(aA )(TTT[TT])Tt", dur=1/3, amp=Pvar(
    [[1, .5], 0], [7, 3, 6]), reverb_dry_wet=sinvar([.4, 0], 8))


b1 >> ubass(0, amp=1, dur=PSum(3, 2), vol=.8)
b2 >> crubass(0, amp=1, dur=PSum(3, 2))
k1 >> kicker(P(1), amp=var([0, .2], 8), vol=1.17)

d2 >> ubass(Pvar([P[0, 2, 4, 2, 0], P[0, 2, 0, 6, 0]], 8), dur=PSum(3, 2), sus=PSum(
    3, 2)-.3, amp=1, oct=3, scale=Scale.minor)  # + Pvar([(2,4),(-1,2),(-2,4)],[12,14,4])
dd >> crubass(P[0, 2, 4, 2, 0], dur=PSum(3, 2),
              amp=1, oct=3, scale=Scale.minor)
dd >> crubass(Pvar([P[0, 2, 4, 2, 0], P[0, 2, 0, 6, 0]], 8),
              dur=PSum(3, 2), amp=1, oct=3, scale=Scale.minor)
dd >> crubass(Pvar([P[0, 2, 4, 2, 0], P[0, 2, 0, 6, 0]], 8),
              dur=PSum(3, 2), amp=1, oct=3, scale=Scale.minor)

s1 >> owstr(Pvar([P[0, 2, 4, 2, 0], P[0, 2, 0, 6, 0]], 8), dur=8, vol=1)

cc >> kitcuba(PRand(range(20))[:32], dur=P[4/10,
              3/10, 3/10], amp=Pvar([[1, .5], 0], [6, 2]))
c1 >> kitcuba("A(a )(aA )(TTT[TT])Tt", dur=1/3, oct=3, amp=Pvar(
    [[1, .5], 0], [7, 3, 6]), vol=1, reverb_dry_wet=sinvar([.4, 0], 8))
c2 >> kicker(1, dur=1, oct=3, amp=var([1, 0], [12, 4])).every(8, "stutter", 3)

cc >> kitdatai("e((ec)ee(c )((ec)ee(c )))",
               dur=P[4/10, 3/10, 3/10], amp=[.6, .3], vol=.6, root=0)
