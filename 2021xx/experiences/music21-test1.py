from music21 import *

us = environment.UserSettings()
us['lilypondPath'] = '/usr/bin/lilypond'
us['musescoreDirectPNGPath'] = '/usr/bin/musescore'
us['musicxmlPath'] = '/usr/bin/musescore'

d7 = chord.Chord(['D4', 'F4', 'A4', 'C5'])
d7.duration.type = 'half'
d7.show('vexflow')


help(d7.show)