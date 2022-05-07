from FoxDot.preset import *

q1 >> template([0, 2, 3, 0, -5, 4], oct=6,
               dur=var([.33, 1], 8)).span(linvar([0, 5.9], [8, 0]), 1)

q1.showp()
