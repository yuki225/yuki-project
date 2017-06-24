# -*- coding: utf-8 -*-
import pyaudio
import wave
import time
import numpy as np
import matplotlib.pyplot as plt

def recode():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1        #モノラル
    RATE = 44100        #サンプルレート
    CHUNK = 2**11       #データ点数
    RECORD_SECONDS = 10 #録音する時間の長さ
    WAVE_OUTPUT_FILENAME = "human_voice.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        input_device_index=13,   #デバイスのインデックス番号
                        frames_per_buffer=CHUNK)

    print ("recording...")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording!!")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def main():
    wf = wave.open("human_voice.wav" , "r" )
    buf = wf.readframes(wf.getnframes())
    # バイナリデータを16bit整数に変換
    data = np.frombuffer(buf, dtype="int16")
    plt.plot(data)
    plt.show()          # グラフ表示

if __name__ == '__main__':
    recode()
    time.sleep(1.0)
    main()
