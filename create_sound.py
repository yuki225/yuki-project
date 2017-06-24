import wave 
import struct
import numpy as np 
from pylab import *

def createSineWave (A, f0, fs, length):
    """ Creates and returns a sine wave with amplitude A, fundamental frequency f0, sampling frequency fs, length in seconds """
    data =[]
    #Create a wave with a decimal value of [-1.0, 1.0]
    #arange method in numpy: generates a array(vector) of numbers with equal differences between them. eg: np.arrage(3) = array([1, 2, 3])
    for n in arange(length * fs):   # n is index of sample (the sample number)
        s = A * np.sin ( 2 * np.pi * f0 * n / fs)
        # Clip when amplitude is large 
        if s > 1.0 : s = 1.0 
        if s < -1.0 : s = -1.0
        data.append (s)
    #Convert to integer value of [-32768, 32767] 
    data = [int(x * 32767.0) for x in data]
    # plot (data [0: 100]); show () 
    # Convert to binary 
    data = struct.pack("h" * len(data), *data)   # Add an asterisk to * list to expand the argument 
    return data

def play (data, fs, bit):
    import pyaudio
    # Open stream
    p = pyaudio.PyAudio ()
    stream = p.open (format = pyaudio.paInt16,
                     channels = 1,
                     rate = int(fs),
                     output = True )
    # Output to stream on chunk and play back sound 
    chunk = 1024 
    sp = 0   # Playback position pointer 
    buffer = data [sp: sp + chunk]
    while buffer != '':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data [sp: sp + chunk]
    stream.close ()
    p.terminate ()

if __name__ == "__main__":
    freqList = [ 262 , 294 , 330 , 349 , 392 , 440 , 494 , 523 ]   # Dorifa Soraside 
    for f in freqList:
        data = createSineWave ( 1.0, f, 8000.0, 2.0 )
        play (data, 8000, 16)