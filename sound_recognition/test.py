import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io import wavfile
#fs, data = wavfile.read('./output/audio.wav')

fs = 44100
duration = 5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait(ignore_errors=True)
print(myrecording)
print(len(myrecording))
sd.playrec(myrecording, fs, channels=1)
plt.figure(figsize=(15,15))
plt.plot(myrecording)
plt.savefig('voice.png', quality=100)