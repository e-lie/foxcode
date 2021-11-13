
def part1():
    k1 >> kicker([6,(4,12)], dur=1, oct=3, amp=var([1,0],[28,4])).every(16, "stutter", 2)
    Clock.future(32, part2)
def part2():
    k1 >> kicker(1, dur=1, oct=3, amp=var([1,0],[12,4])).every(8, "stutter", 3)
    Clock.future(32, part1)
    # Clock.future(32, stoploop)
def stoploop():
    k1.stop()
part1()


###################################################################

print(SynthDefs)
Scale.default = scale2
Root.default = root2
moct=var([5,6,4,3],4)

b2 >> ubass([0,2,4,0,4], dur=PSum(5,3), amp=1, oct=3)

p1 >> blip([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> dirt([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> lazer([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> scratch([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> space([0,2,4,0,4], dur=PSum(5,3), oct=moct)

p1 >> dbass([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> sawbass([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> jbass([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> bass([0,2,4,0,4], dur=PSum(5,3), oct=moct)

p1 >> pads([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> snick([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> prophet([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> soprano([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> bell([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> pasha([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> pulse([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> charm([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> squish([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> bug([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> gong([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> noise([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> feel([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> nylon([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> marimba([0,2,4,0,4], dur=PSum(5,3), oct=moct)
p1 >> quin([0,2,4,0,4], dur=PSum(5,3), oct=moct)

################################################################

print(Scale.names())
print(Scale.blues)

### Modes
# I Ionian (diatonic major)
# II Dorian
# III Phrygian
# IV Lydian
# V Mixolydian
# VI Aeolian
# VII Locrian

scalee = Pvar([Scale.locrianMajor, Scale.blues],4)
p1 >> gong(PWalk()[:32], oct=4, scale=scalee, dur=Pvar([PSum(3,1), PSum(4,1), PSum(3,2)],2))

d1 >> play(Pvar(["<X-(- =(xopo))><t p >","<OooO[oo][oo]><tXX>"],[30,2]), dur=gnawa)

p1 >> bells(Pvar([Scale.major, Scale.lydian, Scale.phrygian],8), dur=gnawa, vol=.8, root=0).every(4,"stutter",3)
p2 >> kora([P+(0,2,4,6)], dur=4, sus=2, vol=.7, root=var([0,5,4],8), scale=Scale.major)
