
Clock.bpm = 200
Clock.clear()

@run_now
def straight():
    d1 >> play("o oo", amp=[3, 1, 2, 1])
@run_later(8)
def quitestraight():
    d1 >> play("o[   o][       o] ", amp=[3, 1, 2, 1])
@run_later(16)
def quiteternary():
    d1 >> play("o[   o ][    o] ", amp=[3, 1, 2, 1])
@run_later(24)
def quitequiteternary():
    d1 >> play("o[    o  ][     o ] ", amp=[3, 1, 2, 1])
@run_later(32)
def ternary():
    d1 >> play("[o  ][ o ][  o] ", amp=[3, 1, 2, 1])
p1 >> bass([0,4,5,3], dur=8, amp=0.9)
p2 >> pluck([0,4,7,9], dur=1/2, amp=0.9)
