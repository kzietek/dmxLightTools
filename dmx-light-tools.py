#!/usr/bin/env python
# 
# https://docs.python.org/dev/library/argparse.html

import argparse
from input.PulseAudioInput import PulseAudioInput

def inputSound():
	pulseIn = PulseAudioInput()
	pulseIn.run()

parser = argparse.ArgumentParser(description='Control DMX lights.')
parser.add_argument("--input-sound-test", nargs='?', const='ON', default='OFF')
args = parser.parse_args()

if args.input_sound_test != 'OFF':
    inputSound()
