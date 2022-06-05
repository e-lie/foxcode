from FoxDot.preset import *


change_bpm(120)

c1 >> ceramic(sus=.5, oct=[3,5,7], dur=clave23*2) + P*(0,2,4)
c1.span(srot(16))
c1.ceramic_tone = linvar([0,1], 7)




def c1p():
    period = 32
    timing = [2,4,16]
    dvals = {
        "degree": 0,
        "dur": 1/2,
        "scale": Scale.major,
    }
    vals = {
        "degree": [[0,(2,6),4], [-5,-4,-3]],
        "dur": [1/3,1/4],
        "scale": [Scale.majorPentatonic, Scale.minor],
    }
    res = {}
    for k, v in vals.items():
        res[k] = Pvar(v, timing)
    return res






    # def add_degree_change(value, start=0, stop=duration):
    #     assert stop > start and start > 0 and stop < self.duration
    #     if start > 0 and start < self.duration:
    #         self.add_timing_step(start)
    #     if stop < duration:
    #         self.add_timing_step(stop)
    #
    #     for step in self.timings:


class ParamMatriiix:
    pass



c1 >> ceramic(**c1p())

pp >> play("XTT")
