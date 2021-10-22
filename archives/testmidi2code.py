import FoxDot
from FoxDot.lib.TempoClock import TempoClock
from functools import wraps

def later(future_dur):
    def later_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            Clock = TempoClock()
            Clock.future(future_dur, f, args=args, kwargs=kwargs)
            return f
        return wrapped
    return later_decorator

Scale.default = list(range(12))


@run_later(8)
def a0():
	d0 >> pluck([0, (2,), (10,), (7,), (5,)],dur=[rest(5.5), 0.5, 0.5, 0.5, 1.0])
	d2 >> pluck([(-24,), (-24,), (-24,), (-24,), (-24,), (-24,), (-24,), (-24,)],dur=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],amp=[1, 1, 1, 1, 1, 1, 1, 1])
	# d3 >> pluck([(-60,)],dur=[8],amp=[0])

Clock.clear()