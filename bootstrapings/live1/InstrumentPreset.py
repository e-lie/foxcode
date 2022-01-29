
from FoxDot.lib.Extensions.Ableton import arm_all, create_instruc

from .EffectsPreset import *

arm_all()

Clock.midi_nudge = 0

mixer = create_instruc(track_name="mixer", channel=-1,
                scale=Scale.chromatic, oct=3, midi_map="stdrum")


metronome = create_instruc(
    track_name="metronome",
    channel=16,
    set_defaults=False,
    scale=Scale.chromatic,
    oct=3,
    config={"root": 0},
    midi_map="stdrum",
)

# Channel 1

kit808 = create_instruc(
    track_name="kit808",
    channel=1,
    scale=Scale.chromatic,
    oct=3,
    config={"root": 0},
    midi_map="stdrum",
    dur=1 / 2,
)

kicker = create_instruc(
    track_name="kicker",
    channel=1,
    config={"root": 0},
    scale=Scale.chromatic,
    oct=1.6,
    midi_map="threesquare",
    dur=1,
)

kitdatai = create_instruc(
    track_name="kitdatai",
    channel=1,
    config={"root": 0},
    scale=Scale.chromatic,
    oct=4.4,
    midi_map="stdrum",
    dur=1 / 2,
)

# Channel 2

kitcuba = create_instruc(
    track_name="channel_2",
    channel=2,
    grouping=True,
    oct=3,
    dur=1 / 2,
    midi_map="stdrum",
    config={
        "root": 0,
        "kitcuba_vol": 1,
        "jazzkit_vol": 0,
        "reaktorkit_vol": 0,
        "harshkit_vol": 0,
    },
    scale=Scale.chromatic,
)

jazzkit = create_instruc(
    track_name="channel_2",
    channel=2,
    grouping=True,
    oct=3,
    dur=1 / 2,
    midi_map="stdrum",
    config={
        "root": 0,
        "kitcuba_vol": 0,
        "jazzkit_vol": 1,
        "reaktorkit_vol": 0,
        "harshkit_vol": 0,
    },
    scale=Scale.chromatic,
)

reaktorkit = create_instruc(
    track_name="channel_2",
    channel=2,
    grouping=True,
    oct=3,
    dur=1 / 2,
    midi_map="stdrum",
    config={
        "root": 0,
        "kitcuba_vol": 0,
        "jazzkit_vol": 0,
        "reaktorkit_vol": 1,
        "harshkit_vol": 0,
    },
    scale=Scale.chromatic,
)

harshkit = create_instruc(
    track_name="channel_2",
    channel=2,
    grouping=True,
    oct=3,
    dur=1 / 2,
    midi_map="stdrum",
    config={
        "root": 0,
        "kitcuba_vol": 0,
        "jazzkit_vol": 0,
        "reaktorkit_vol": 0,
        "harshkit_vol": 1,
    },
    scale=Scale.chromatic,
)

# Channel 6

crubass = create_instruc(
    track_name="channel_6",
    channel=6,
    grouping=True,
    oct=3,
    # sus=1/2, #the sustain bug disappeared
    config={
        "ubass_vol": 0,
        "crubass_vol": 1,
        "tb303_vol": 0,
    }
    | rndp(crubassp, 12),
    # scale=Scale.minor,
)

tb303 = create_instruc(
    track_name="channel_6",
    channel=6,
    grouping=True,
    oct=4,
    # sus=1/2,
    config={
        "ubass_vol": 0,
        "crubass_vol": 0,
        "tb303_vol": 0.9,
    },
    # scale=Scale.minor,
)

ubass = create_instruc(
    track_name="channel_6",
    channel=6,
    grouping=True,
    oct=4,
    config={
        "ubass_vol": 0.9,
        "crubass_vol": 0,
        "tb303_vol": 0,
    },
    # scale=Scale.minor,
)

# Channel 7

crubass_2 = create_instruc(
    track_name="channel_7",
    channel=7,
    grouping=True,
    oct=4,
    config={
        "ubass_vol": 0,
        "crubass_vol": 1,
        "tb303_vol": 0,
    }
    | rndp(crubassp, 12),
    # scale=Scale.minor,
)

tb303_2 = create_instruc(
    track_name="channel_7",
    channel=7,
    grouping=True,
    oct=4,
    config={
        "ubass_vol": 0,
        "crubass_vol": 0,
        "tb303_vol": 0.9,
    },
    # scale=Scale.minor,
)

# Channel 8

piano = create_instruc(
    track_name="channel_8",
    channel=8,
    grouping=True,
    oct=5,
    config={
        "piano_vol": 1,
        "danceorg_vol": 0,
    },
    # scale=Scale.minor,
)

danceorg = create_instruc(
    track_name="channel_8",
    channel=8,
    grouping=True,
    oct=5,
    config={
        "piano_vol": 0,
        "danceorg_vol": 1,
    },
    # scale=Scale.minor,
)

kora = create_instruc(
    track_name="channel_4",
    channel=4,
    grouping=True,
    oct=5,
    config={
        "kora_vol": 1,
    },
    # scale=Scale.major,
)

strings = create_instruc(
    track_name="channel_9",
    channel=9,
    grouping=True,
    oct=5,
    config={
        "strings_vol": 1,
        "owstr_vol": 0,
    },
    # scale=Scale.major,
)

owstr = create_instruc(
    track_name="channel_9",
    channel=9,
    grouping=True,
    oct=5,
    config={
        "strings_vol": 0,
        "owstr_vol": 1,
    },
    # scale=Scale.major,
)

balafon = create_instruc(
    track_name="channel_10",
    channel=10,
    grouping=True,
    oct=5,
    config={
        "balafon_vol": 1,
        "bells_vol": 0,
    },
    # scale=Scale.major,
)

bells = create_instruc(
    track_name="channel_10",
    channel=10,
    grouping=True,
    oct=5,
    config={
        "balafon_vol": 0,
        "bells_vol": 1,
    },
    # scale=Scale.major,
)
