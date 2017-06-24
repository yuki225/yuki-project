# -*- coding : utf -8 -*-
import sys
import scipy.io.wavfile
import numpy
import pylab

def plot_waveform ( waveform , sampling_rate ):
    sampling_interval = 1.0 / sampling_rate
    times = numpy.arange ( len ( waveform )) * sampling_interval
    pylab.plot ( times , waveform ) # pair of two x - and y - coordinate lists / arrays
    pylab.title ( ' Waveform ' )
    pylab.xlabel ( ' Time [ sec ] ' )
    pylab.ylabel ( ' Amplitude ' )
    pylab.xlim ([0 , len ( waveform ) * sampling_interval ])
    pylab.ylim ([ -1 , 1])
    pylab.show ()

# main function of Python programs
argv = sys.argv
if len ( argv ) == 1:
    print ' no input files . '
    exit

filename = "output.wav"
sampling_rate , waveform = scipy.io.wavfile.read ( "output.wav" )
waveform = waveform / 32768.0 # assume 16 - bit integer
plot_waveform ( waveform , sampling_rate )