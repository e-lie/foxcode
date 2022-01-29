

# def delay(config=None, vol=None, time=None, feedback=None, pan=None, dry=None):
#     delay_base = { "delay_vol": 0, "delay_time": .5, "delay_feedback": .5, "delay_pan": .5, "delay_dry": 1 }
#     if config and 'var' in config:
#         dur = int(config[3:])
#         vol = sinvar([0,.6],dur)
#         time = 1 / (Clock.bpm / 60) # synchro delay time with current bpm
#     vol = vol if vol is not None else delay_base["delay_vol"]
#     time = time if time is not None else delay_base["delay_time"]
#     feedback = feedback if feedback is not None else delay_base["delay_feedback"]
#     pan = pan if pan is not None else delay_base["delay_pan"]
#     dry = dry if dry is not None else delay_base["delay_dry"]
#     return { "delay_vol": vol, "delay_time": time, "delay_feedback": feedback, "delay_pan": pan, "delay_dry": dry}


def delay(subdiv=1 / 2, vol=0.6, time=None, feedback=0.5, pan=0.5, dry=1):
    config = {
        "delay_vol": vol,
        "delay_feedback": feedback,
        "delay_pan": pan,
        "delay_dry": dry,
    }
    if time is not None:
        config["delay_time"] = time
    else:
        beat_dur = 1 / (Clock.bpm / 60)  # synchro delay time with current bpm
        config["delay_time"] = subdiv * beat_dur
    return config


def lpf(freq, low_vol=0):
    return {"eq_gainlo": low_vol, "eq_freqlo": freq}


def tb3(config=None, decay=None, freq=None, reso=None, drive=None, delay=None):
    default_conf = {
        "i_decay": 0.33,
        "i_freq": 0.15,
        "i_reso": 0.66,
        "i_drive": 0.4,
        "i_delay": 0,
    }
    return default_conf


def fadein(dur=4, fvol=1, ivol=0):
    return {"vol": linvar([ivol, fvol], [dur, inf], start=Clock.mod(4))}


def fadeout(dur=16, ivol=1, fvol=0):
    return {"vol": linvar([ivol, fvol], [dur, inf], start=Clock.mod(4))}


def fadeoutin(dur=16, outdur=16, ivol=1, mvol=0, fvol=1):
    return {"vol": linvar([ivol, mvol, mvol, fvol], [dur, outdur, dur, inf], start=Clock.mod(4))}


def change_bpm(bpm, midi_nudge=True, nudge_base=0.22):
    Clock.bpm = bpm
    liveset.tempo = bpm

    @nextBar()
    def nudging():
        if midi_nudge:
            Clock.midi_nudge = 60 / bpm - nudge_base

def randomize_params(param_dict, seed=0):
    params_values = PWhite(seed=seed)[:len(param_dict.keys())]
    for i, key in enumerate(param_dict.keys()):
        param_dict[key] = params_values[i]
    return param_dict

rndp = randomize_params