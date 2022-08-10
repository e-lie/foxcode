from FoxDot.preset import *

reverb = [
    'ReaVerbate', 'reverb', 'verb base', {
        "Wet": "wet",
        "Dry": "dry",
        "Room size": "size"
    }
]
lpf = [
    'ReaEQ', 'lpf', 'lpf', {
        "Freq-Low Pass 4": "freq",
        "Q-Low Pass 4": "bw",
        "Gain-Low Pass 4": "gain"
    }
]
hpf = [
    'ReaEQ', 'hpf', 'hpf', {
        "Freq-High Pass 1": "freq",
        "Q-High Pass 1": "bw",
        "Gain-High Pass 1": "gain"
    }
]
sur = ['ReaSurround', 'sur', 'hexa_spatial', {"in 1 X": "x", "in 1 Y": "y"}]
limit8 = ['ReaLimit', 'limit8', 'limit8', {}]
# hamp = ['ReaVerbate', 'reverb', 'testounet', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]
# delay = ['ReaVerbate', 'reverb', 'testounet', {"Wet":"wet", "Dry":"dry", "Room size": "size"}]
full_effect_stack = [reverb, lpf, hpf, sur, limit8]

################################################################
### Mallets

marimba = newintru(
    plugin_name='kontakt', name='marimba', params={}, effects=full_effect_stack
)

vibra = newintru(
    plugin_name='kontakt', name='vibra', params={}, effects=full_effect_stack
)

ceramic = newintru(
    plugin_name='vital',
    name='ceramic',
    params={
        "Macro 1": "mute",
        "Macro 2": "tone",
        "Macro 3": "sustain",
        "Macro 4": "mod"
    },
    effects=full_effect_stack
)

################################################################
### Noise

fordrip = newintru(
    plugin_name='vital',
    name='fordrip',
    params={
        "Macro 1": "bit_crush",
        "Macro 2": "drip",
        "Macro 3": "psy",
        "Macro 4": "ambiance"
    },
    effects=full_effect_stack
)

whibot = newintru(
    plugin_name='vital',
    name='whibot',
    params={
        "Macro 1": "wash",
        "Macro 2": "warp"
    },
    effects=full_effect_stack
)

################################################################
### Bass

darkpass = newintru(
    plugin_name='vital',
    name='darkpass',
    params={
        "Macro 1": "rm",
        "Macro 2": "detune",
        "Macro 3": "sustain",
        "Macro 4": "reverb"
    },
    effects=full_effect_stack
)

hpluck = newintru(
    plugin_name='vital',
    name='hpluck',
    params={
        "Macro 1": "width",
        "Macro 2": "drive",
        "Macro 3": "reverb",
        "Macro 4": "release"
    },
    effects=full_effect_stack
)

growlside = newintru(
    plugin_name='vital',
    name='growlside',
    params={
        "Macro 1": "drive",
        "Macro 2": "filter",
        "Macro 3": "space",
        "Macro 4": "warp"
    },
    effects=full_effect_stack
)

jupiter = newintru(
    plugin_name='vital',
    name='jupiter',
    params={
        "Macro 1": "vibrato",
        "Macro 2": "noise",
        "Macro 3": "unison",
        "Macro 4": "analog"
    },
    effects=full_effect_stack
)
