import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf

audio_path = r'C:\Users\Asus\Documents\python_cookies\alpha\voics_intro\audio.wav'
signal, sr = librosa.load(audio_path, sr=None)

plt.figure(figsize=(12,4))
librosa.display.waveshow(signal, sr=sr, alpha = 0.5)
plt.title('Wave representation of the audio')
plt.xlabel('Time (sec)')
plt.ylabel('amplitude')
plt.grid()
plt.show()

plt.figure(figsize=(12,4))
D = librosa.amplitude_to_db(np.abs(librosa.stft(signal)), ref=np.max)
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram of the audio")
plt.xlabel("Time (sec)")
plt.ylabel("Frequency (HHz)")
plt.show()