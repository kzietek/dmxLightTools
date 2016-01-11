# Based on concept described here: http://freshfoo.com/blog/pulseaudio_monitoring
# Using https://github.com/Valodim/python-pulseaudio

# Not used but worth to remember: https://github.com/mk-fg/pulseaudio-mixer-cli
# Beat detector https://zolmeister.com/2012/10/back-light-music-leds.html

import PulsePeakMonitor
import sys
from PulsePeakMonitor import *

SINK_NAME = 'alsa_output.pci-0000_00_1b.0.iec958-stereo'  # edit to match your sink
METER_RATE = 344

class PulseAudioInput(object):
	def __init__(self):
		self.sinkName = SINK_NAME
		self.meterRate = METER_RATE
		print "Inited PulseAudioInput"

	def __del__(self):
		print "Destructed PulseAudioInput"

	def run(self):
		print "Running PulseAudioInput"
		monitor = PulsePeakMonitor(self.sinkName, self.meterRate)
		monitor.verbose = False
		for sample in monitor:
			print ' %3d\r' % (sample),
			sys.stdout.flush()
