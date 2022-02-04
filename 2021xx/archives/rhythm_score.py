
rhythm_list = [
    "x--=",
    "xo-=",
    "xoo=",
    "xxo=",
]

def playr(player, rhythm):
    player >> play(rhythm)


# def iterative_score(player, rhythm_list, wait_list):
#     for rhythm in rhythm_list:
#         player >> play(rhythm_list[0])
#         Clock.future(20, playlist, args=(player, rhythm_list[1:], []))
# iterative_score(rr, rhythm_list, [])


playr(rr, rhythm_list[0])
Clock.future(16, playr, args=(rr, rhythm_list[1]))
Clock.future(32, playr, args=(rr, rhythm_list[2]))
Clock.future(48, playr, args=(rr, rhythm_list[3]))

print(Clock)


playr(aa, "----")
@later(4)
playr(aa, "x---")
@later(16)
playr(aa, "x-o-")

playr(aa, "x-o[-x][-o][-x]o ")
for i in range(10):
    Clock.future(i*16+3*4, playr, args=(aa, "x-o[-x][-o][-x]o[oo]"))
    Clock.future((i+1)*16, playr, args=(aa, "x-o[-x][-o][-x]o "))

aa.stop() # doesn't empty the future function to play only the currently playing function
print(Clock)

playr(aa, 3*"x-o[-x][-o][-x]o "+"x-o[-x][-o][-x]o[oo]")
