import numpy as np
import os
import scipy
import readTrc as rT
import matplotlib.pyplot as plt
import glob

print('\nName')
# for name in glob.glob('C:\\Users\\molle\\Documents\\LPSC_Stage\\ARRONAX\\ARRONAX_07_21\\Arronax_2021\\ARRONAX072021\\09072021\\acq-diam-pulsed800pAcontinuous\\C2*'):
#     print(name)


def integrale_train(file):
    dt = file.dt
    dit = file.dit
    path = file.adresse
    return


class Test():
    def __init__(self, name, dt, dit, adresse, nom_fichier,voie):
        self.nom = name
        self.adresse = adresse
        self.dt = dt
        self.nom_fichier = nom_fichier
        self.voie = voie
        return

file = Test(nom_fichier="ok",name = "ok",dt = 10, adresse ='C:\\Users\\molle\\Documents\\LPSC_Stage\\ARRONAX\\ARRONAX_07_21\\Arronax_2021\\ARRONAX072021\\09072021\\acq-diam-pulsed800pAcontinuous\\',voie= "C2--Trigger8m500;V--00000")


for waveform in glob.glob(file.adresse + file.voie + "*" ):
    time, amplitude, _ = rT.readTrc(waveform)
    plt.figure()
    plt.plot(time, amplitude)
    peaks, _=scipy.signal.find_peaks(x=amplitude, distance=30*1E-9/(time[1]-time[0]), width=30, height=0.003)
    time_peak = [time[i] for i in peaks]
    amplitude_peak = [amplitude[i] for i in peaks]
    plt.plot(time_peak, amplitude_peak, marker='*', linestyle='')
    plt.show()

