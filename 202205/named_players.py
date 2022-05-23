from FoxDot.preset import *


change_bpm(90)

jackie = Player()
hurleur = Player()
mémé = Player()
les3nazes = Group(mémé, jackie, hurleur)

jackie >> play("X-x-").stop(1.8)

hurleur >> play("trololo").mpan(drot(17))
hurleur.stop(4.5)

mémé >> accciddd()

hurleur >> play("mathis").mpan(drot(17))

hurleur.stop(4.8)

les3nazes.fadeout(8)

p1 >> play("x-o[oo]")
p1.stop()
