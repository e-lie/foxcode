# Pattern function
from copy import Error

def interpolate(start, end, step=7, go_back=True):
    if len(start) == 1 and len(end) > 1:
        start = [start[0]] * len(end)
    if len(end) == 1 and len(start) > 1:
        end = [end[0]] * len(start)
    assert len(start) == len(end)
    diffs = []
    result = []
    for i in range(len(start)):
        diffs += [start[i] - end[i]]
    base_pattern = start
    for j in range(step):
        new_pattern = [
            e - diffs[k]/(step + 1) for k, e in enumerate(base_pattern)
        ]
        result.append(new_pattern)
        base_pattern = new_pattern
    if not go_back:
        result = [start] + result + [end]
    else:
        result = (
            [start] + result + [end] + result[::-1]
        )  # result except last elem + end + reversed result
    return result


interp = interpolate

def interpvar(start, end, total_dur=None, step=6, dur=1, go_back=True):
    if total_dur is not None:
        step = (total_dur - 2) // 2
        dur = 1
    return Pvar(interpolate(start, end, step, go_back), dur)


Pvi = interpvar


def zipvar(duration_pattern_list):
    if len(duration_pattern_list) == 1:
        return duration_pattern_list[0][0]
    patterns = [item[0] for item in duration_pattern_list]
    durations = [item[1] for item in duration_pattern_list]
    return Pvar(patterns, durations)


Pvz = zipvar


def Pzr(root_pattern_list):
    if len(root_pattern_list) == 1:
        return {
            "degree": root_pattern_list[0][0],
            "root": root_pattern_list[0][1]
        }
    patterns = [item[0] for item in root_pattern_list]
    roots = [item[1] for item in root_pattern_list]
    durations = [item[2] for item in root_pattern_list]
    return {"degree": Pvar(patterns, durations), "root": Pvar(roots, durations)}

# Param shortcut functions to use with dict unpack : **lpf(linvar([0,.3],8))

@player_method
def human(self, velocity=20, humanize=5, swing=0):
    """ Humanize the velocity, delay and add swing in % (less to more)"""
    humanize += 0.1
    if velocity!=0:
        self.delay=[0,PWhite((-1*humanize/100)*self.dur, (humanize/100)*self.dur) + (self.dur*swing/100)]
        self.amplify=[1,PWhite((100-velocity)/100,1)]
    else:
        self.delay=0
        self.amplify=1
    return self



# def pattern_tweak(pattern, tweak_len=None, config="random", random_amount=.1, compensation=True):
#     plen = len(pattern)
#     tweak_len = tweak_len if tweak_len else plen-1
#     assert plen > 1

#     if config == "random":
#         tweak_serie = PWhite(-random_amount,random_amount)[:tweak_len]
#         print(tweak_serie)
#     else:
#         raise Error("This tweak pattern config doesn't exist : {}".format(config))

#     result = []
#     current_modulo = 0
#     total_tweak_amount = 0
#     for i, tweak_value in enumerate(tweak_serie):
#         current_modulo = i%plen
#         result.append(pattern[current_modulo] + tweak_value)
#         total_tweak_amount += tweak_value

#     if compensation:
#         print(current_modulo)
#         remaining_values = [value for value in pattern[(current_modulo+1+1)%plen:-1]]
#         print(remaining_values)
#         tweak_compensation_values = [-total_tweak_amount/len(remaining_values) for value in remaining_values]
#         result += tweak_compensation_values
#     print(result)
#     return result


def rnd(pattern, random_amount=0.05, compensation=True):
    tweak_serie = PWhite(-random_amount, random_amount)[: len(pattern)]
    result = [pattern[i] + tweak_serie[i] for i in range(len(pattern))]
    if compensation:
        result += [pattern[i] - tweak_serie[i] for i in range(len(pattern))]
    print(result)
    return result


def rnd1(pattern):
    average_value = sum(pattern) / len(pattern)
    return rnd(pattern, random_amount=0.1 * average_value)


def rnd2(pattern):
    average_value = sum(pattern) / len(pattern)
    return rnd(pattern, random_amount=0.2 * average_value)


def rnd5(pattern):
    average_value = sum(pattern) / len(pattern)
    return rnd(pattern, random_amount=0.05 * average_value)


def microshift(pattern, shifts):
    for key, value in shifts.items():
        if key in range(len(pattern) - 1):
            pattern[key] += value
            pattern[key + 1] -= value
    print(pattern)
    return pattern


def zipat(*args):
    notes = [item for i, item in enumerate(args) if i % 2 == 0]
    dur = [item for i, item in enumerate(args) if i % 2 == 1]
    return {"degree": notes, "dur": dur}


ZP = zipat



def ampfadein(dur=4, famp=.8, iamp=0):
    return {"amp": linvar([iamp, famp], [dur, inf], start=Clock.mod(4))}


def ampfadeout(dur=16, iamp=.8, famp=0):
    return {"amp": linvar([iamp, famp], [dur, inf], start=Clock.mod(4))}




def run_now(f):
    f()
    return f

# This is not really a decorator, more a currying mechanism using the decorator syntax
# Cf: https://www.geeksforgeeks.org/currying-function-in-python/ and https://www.saltycrane.com/blog/2010/03/simple-python-decorator-examples/


def later_clockless(clock):
    def later_clocked(future_dur):
        def later_decorator(f):
            clock.future(future_dur, f)
            return f
        return later_decorator
    return later_clocked