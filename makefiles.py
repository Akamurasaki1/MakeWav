from utils import avoid_overwrite , format_np_array
from jisyo import Token_Name_table, Token_Frequency_table, Token_MIDI_table
from converter import Name_fromID, Freq_fromID, MIDInum_fromID, Names_fromIDs, Freqs_fromIDs, MIDInums_fromIDs   
import numpy as np
import os
from scipy.io import wavfile
# makefiles.py


# freq_array:周波数列
# filename:出力ファイルの名前
# fs:サンプリング周波数
# Dso:1ノーツ(音符)あたりの長さ(秒)
# volume:音量(0~1)
def gen_1part_wav(freqs_array, output_filename="output.wav", fs=44100, Dso=0.25, volume=0.5):
    f=freqs_array
    T=len(freqs_array)*Dso
    slength=int(fs*T)
    signal= np.zeros(slength)

    for i in range(len(freqs_array)):
        for j in range(int(fs*Dso)):
            tn=j/fs
            signal[int(i*fs*Dso)+j]=volume*np.sin(2*np.pi*f[i]*tn)

    signal=32768*signal
    signal=signal.astype(np.int16)
    output_filename=avoid_overwrite(output_filename)
    wavfile.write(output_filename, fs, signal)
    print(f"WAV saved: {output_filename}")

# Example usage:
gen_1part_wav([391.995,0,0,0,659.225,0,587.330,523.251,587.330,0,783.991,0,739.989,0,369.994,0,0,391.995,0,0,0,659.225,0,587.330,523.251,587.330,0,523.251,0,500.000,0,391.995],output_filename="./outputs/example_marenol.wav", fs=44100, Dso=0.25, volume=0.5)
