import librosa
import numpy as np

# audio_path:オーディオファイルのパス("~~~~~.wav","~~~~~.mp3"など)
# fs:サンプリング周波数(Hz)
# hop_length:
def get_freqs_from_audio(audio_path, fs=44100, hop_length=512):
    y, sr = librosa.load(audio_path, sr=fs)
    pitches, magnitudes = librosa.piptrack(y=y, sr=fs, hop_length=hop_length)

    freqs = []
    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        freq = pitches[index, i]
        freqs.append(freq if freq > 0 else 0.0)

    return np.array(freqs)
# Example usage:
# audio_path = "path/to/your/audio.wav"
mopemope_preview_freqs = get_freqs_from_audio("/Users/karen/forBMS/LeaF/[clover]LeaF_mopemope/_preview.wav",fs=44100, hop_length=512)
print(mopemope_preview_freqs)