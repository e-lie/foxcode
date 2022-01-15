change_bpm(160)
bb >> mixer()




s1 >> strings(P[0,2,4], dur=[4,3,5], vol=.8)

d3 >> play("[--]", amp=1.5)
d4 >> kit808("([oo][soo]s)", amp=[1,1,1,0], hamp_dw=expvar([0,.7],16), resob_dw=.2)

s1 >> owstr(P[0,2,4], dur=[4,3,5], root=var([0,2,4,5,0],16))
s1 >> owstr(P[0,2,4], dur=[4,3,5], root=var([0,2,4,5,0],16))

d4 >> kit808("([oo][soo]s)", amp=[1,0,0,0], hamp_dw=expvar([0,.7],16), resob_dw=.2)

bb >> mixer(delay_vol=0)
