


tester = Player()
tester2 = Player()

tester >> rissetobell([0,2,4], dur=Pvar([P[.6, .6, .4]*2, .25], 16), oct=4).mpan(mrot(16))
tester >> harp([0,2,4]).mpan(mrot(16))
tester >> epiano([0,2,4], dur=Pvar([P[.6, .6, .4]*2, .25], 16), oct=4).mpan(mrot(16))

tester >> marimba([0,2,4], dur=.)

tester2 >> bnoise([0,2,4], dur=Pvar([P[.6, .6, .4]*2, .25], 16), oct=5)

#
pp >> play("Vvvv", rate=linvar([1,1.6], 16), dur=.25, sample=0, hpf=100).mpan(mrot(8))
p3 >> play(" (---[ (-*)])", amp=2, rate=linvar([1,1.6], 16), dur=.5, sample=2, hpf=100).mpan(mrot(32))
p2 >> play("X.XXX.X", rate=linvar([1,1.6], 16), dur=clave23, sample=1, hpf=100).mpan(mrot(16))
bb >> filthysaw(PWalk()[:17], root=var([0,4,2,0], 16), oct=3, dur=PSum(3,2))
bb >> filthysaw(PWalk()[:17], root=var([0,4,2,0], 16), oct=3, dur=2)
ee >> space(PWalk()[:16].stutter(4), root=var([0,4,2,0], 16), oct=(4,7), dur=var([.25, .5, 1/3], [16,8,8])) + (0,2,4)

Scale.default=Scale.minor

# elec: space, blip, click, vibass, sinepad, laserbeam, virus, sillyvoice, spick, alva
# lead: noisynth, epiano, square, faim2
# mallets: tubularbell, rissetobell
# borgam, harp,
# pads: drone
# Basses: tb303, acidbass, bbass, filthysaw, mhping, noquarter
# Noise: bnoise, hnoise, glitcher, shore
