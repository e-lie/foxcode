
rhythm_list = [
    "----=",
    "-x--=",
    "-x-x=",
    "x-x-=",
]

def playr(player, rhythm):
    player >> play(rhythm)

def recursive_score(player, rhythm_list, wait_list):
    if len(rhythm_list) == 0:
        return
    player >> play(rhythm_list[0])
    Clock.future(16, playlist, args=(player, rhythm_list[1:], []))
recursive_score(rr, rhythm_list, [])

def iterative_score(player, rhythm_list, wait_list):
    for rhythm in rhythm_list:
        player >> play(rhythm_list[0])
        Clock.future(20, playlist, args=(player, rhythm_list[1:], []))
iterative_score(rr, rhythm_list, [])


playr(rr, rhythm_list[0])
Clock.future(16, playr, args=(rr, rhythm_list[1]))
Clock.future(32, playr, args=(rr, rhythm_list[2]))
Clock.future(48, playr, args=(rr, rhythm_list[3]))
