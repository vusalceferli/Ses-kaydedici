import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frekans = 44100

müddət = 5

qeydiyyat = sd.rec(int(müddət * frekans),
                   samplerate=frekans, channels=2)

sd.wait()


write("sesyazı.wav", frekans, qeydiyyat)

wv.write("sesyazı1.wav", qeydiyyat, frekans, sampwidth=2)
