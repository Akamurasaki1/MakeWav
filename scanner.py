import librosa
import numpy as np

# audio_path:オーディオファイルのパス("~~~~~.wav","~~~~~.mp3"など)
# sr:サンプリングレート(Hz)
# hop_length:
def get_freqs_from_audio(audio_path, sr=44100, hop_length=512):
    y, sr = librosa.load(audio_path, sr=sr)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr, hop_length=hop_length)

    freqs = []
    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        freq = pitches[index, i]
        freqs.append(freq if freq > 0 else 0.0)

    return np.array(freqs)