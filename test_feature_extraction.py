from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt

def run():
    [Fs, x] = audioBasicIO.readAudioFile("pyAudioAnalysis/data/count.wav");
    F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
    plt.subplot(3,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR'); 
    plt.subplot(3,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy');
    plt.show()

