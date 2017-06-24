"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
""" Then plot the graph """

import pyaudio
import wave
import sys
import scipy.io.wavfile
import numpy
import pylab

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "record_and_plot.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

#end of recording codes
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

filename = "record_and_plot.wav"
sampling_rate , waveform = scipy.io.wavfile.read ( "record_and_plot.wav" )
waveform = waveform / 32768.0 # assume 16 - bit integer
plot_waveform ( waveform , sampling_rate )
#end of plotting code