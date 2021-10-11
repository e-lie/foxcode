Clock.bpm = 160

futureBar(Clock.clear)


@nextBar
def part1():
    b1 >> play("x Xo", amp=2)
@futureBar(4)
def part2():
    b1 >> play("X-o--Xo-")
@run_later(32)
def part3():
    b1 >> play("X-o[-X][-o][-X]o ")
@run_later(48)
def part4():
    b1 >> play("X-o[-X][-o][-X]o[oo]")
@run_later(64)
def part5():
    b1 >> play("<X o[ X][ o][ X]o[Xo]><-------=><  p  p  >")
@run_later(80)
def part6():
    b1 >> play("<X o[  ][ o][  ]o[Xo]><-------=><  p  p  >")
@run_later(96)
def part7():
    b1 >> play("<X o[  ][ o][  ]o[Xo]><- - - - ><  p  p  >")
@run_later(112)
def part8():
    b1 >> play("<X      X><  o[  ][ o][  ]o[ o]><- - - - ><  p  p  >")
@run_later(128)
def part9():
    b1 >> play("<X[ X][ X]    [==]><  o[  ][ o][  ]o[ o]><- - - - ><  p  p  >")
@run_later(144)
def part10():
    b1 >> play("<[XX] [ X]   [XX]X><  o[  ][ o][  ]o[ o]><- - - - ><  p  t  >")
@run_later(176)
def part10():
    b1.stop()
