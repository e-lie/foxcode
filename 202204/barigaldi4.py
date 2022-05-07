m1 >> marimba(
    # '<A >',
    '<ab(dadD) ABD >',
    # dur=.25,
    dur=cascara,
    oct=3,
    amp=[.8, 1],
    amplify=1,
)
m1.span(1)
# m1.fadein(32)

ampr = PWhite(.8, 1.1)[:17]

m3 >> nlead(
    '<cC >',
    #dur=cascara,
    oct=5,
    amp=ampr,
    amplify=pa16,
)

m4 >> marimba(
    '<h h hff>',
    # '<h h h h>',
    dur=cascara,
    oct=[4, 5, 6, 7]
)

m2 >> marimba('(aG) ', dur=clave23, oct=[5, 6, 5],
              amp=1.2).every(8, "stutter", 3)
