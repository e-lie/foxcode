################################################################


# dt.add_value_range(ParamRange(2,8,P[4,-5]))
Root.default = 0
dt = Pt(16, P[0,2,4])
dt << (12,16,0) << (2,4,P[0,4]) << (3,5,P[0,5])
p1 >> piano(dt.out(), dur=.25)

print(dt.out())

M = Pm(16, degree=P[0,2,4].stutter(3), dur=P[.5,.25].stutter(4), amp=PWhite(.5,1)[:77])
M << ("degree", 2, 8, P[-12])
M << ("dur", 6, 8, 1/3)
p1 >> piano(**M.out())

M = Pm(16, degree=P[0,2,4].stutter(3), dur=P[.5,.25].stutter(4), amp=PWhite(.5,1)[:77])
M << Pv(2, 8, degree=P[-12], dur=1/3)
# M << Pv(5, 12, dur=.1)
M << Pv(sus=4)
M << Pv(2,8,sus=linvar([.1,.3],8))
# M << Pv(7,13,sus=.25)
# M << Pv(7,13,sus=.25)
p1 >> click(**M.out())

################################################################

M = Pm(16, degree=[0,1,2,4,5,2,3,0], dur=.5, amp=linvar([.4,1.2], 2), sus=linvar([.25,1], 8))
M << Pv(12, 16, dur=.25)
M << Pv(24, 32, dur=1/3)
M *= 2
print(M)
p1 >> marimba(**M.out())
