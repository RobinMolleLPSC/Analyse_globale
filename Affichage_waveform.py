import numpy as np
import os
import scipy
import Fichier_trc as fichier
import readTrc as rT
import matplotlib.pyplot as plt

Point = "PointC"
numero_point = "00"
adresse = "C:\\Users\\molle\\Documents\\LPSC_Stage\\ARRONAX\\ARRONAX_11_22\\Data\\SamEndommagement\\" + Point + "\\" + Point + "_" + numero_point + "\\"
nom_fichier_C1 = "C1--BasseIntensiteTroisRun--"
nom_fichier_C2 = "C2--" + Point + "_" + numero_point + "--"
nom_fichier_C3 = "C3--" + Point + "_" + numero_point + "--"
nom_fichier_C4 = "C4--BasseIntensiteTroisRun--"

data_forme = []
time_forme = []

# for file in [adresse]:
#     nombre_waveform = 2
#
#     C1 = [0.0 for i in range(2500002)]
#     C2 = [0.0 for i in range(2500002)]
#     C3 = [0.0 for i in range(2500002)]
#     C4 = [0.0 for i in range(2500002)]
#     #
#     # filename = nom_fichier_C1
#     # os.chdir(adresse)
#     # integrale_file = [];
#     # print("Ouverture de " + filename)
#
#     # for i in range(nombre_waveform,nombre_waveform+1):
#     #     waveform = str(i).zfill(5)
#     #     if(os.path.isfile(filename + str(waveform) + '.trc')):
#     #         time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
#     #
#     #         # print(len(time))
#     #         # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
#     #         # plt.xlabel("Time (ns)")
#     #         # plt.ylabel("Amplitude (mV)")
#     #         # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
#     #         for j in range(len(amplitude)):
#     #             C1[j] = (amplitude[j]+C1[j]*i)/(i+1)
#
#     filename = nom_fichier_C2
#     os.chdir(adresse)
#     integrale_file = []
#     print("Ouverture de " + filename)
#     for i in range(nombre_waveform):
#         waveform = str(i).zfill(5)
#         if(os.path.isfile(filename + str(waveform) + '.trc')):
#             time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
#             # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
#             # plt.xlabel("Time (ns)")
#             # plt.ylabel("Amplitude (mV)")
#             # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
#             for j in range(len(amplitude)):
#                 C2[j] = (amplitude[j]+C2[j]*i)/(i+1)
#             for j in range(len(amplitude)):
#                 if time[j]>48768*1E-9 and time[j]<48793*1E-9:
#                     data_forme.append(C2[j])
#                     time_forme.append(time[j])
#
#     filename = nom_fichier_C3
#     os.chdir(adresse)
#     integrale_file = [];
#     print("Ouverture de " + filename)
#     for i in range(nombre_waveform):
#         waveform = str(i).zfill(5)
#         if(os.path.isfile(filename + str(waveform) + '.trc')):
#             time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
#             # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
#             # plt.xlabel("Time (ns)")
#             # plt.ylabel("Amplitude (mV)")
#             # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
#             for j in range(len(amplitude)):
#                 C3[j] = (amplitude[j]+C3[j]*i)/(i+1)
#     #
#     # filename = nom_fichier_C4
#     # os.chdir(adresse)
#     # integrale_file = [];
#     # print("Ouverture de " + filename)
#     # for i in range(nombre_waveform):
#     #     waveform = str(i).zfill(5)
#     #     if(os.path.isfile(filename + str(waveform) + '.trc')):
#     #         time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
#     #         # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
#     #         # plt.xlabel("Time (ns)")
#     #         # plt.ylabel("Amplitude (mV)")
#     #         # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
#     #         for j in range(len(amplitude)):
#     #             C4[j] = (amplitude[j]+C4[j]*i)/(i+1)
#
# print(time_forme)
# print(data_forme)
# plt.figure()
# # plt.plot([time[k]*1E9 for k in range(len(time))],[C1[k]*1E3 for k in range(len(C1))],label="Gandalf Front - 150V - 1V/µm")
# plt.plot([time[k]*1E9 for k in range(len(time))],[C2[k] for k in range(len(C2))],label="Waveform point D fluence nulle : SAM")
# # plt.plot([time[k]*1E9 for k in range(len(time))],[C3[k] for k in range(len(C3))],label="PM")
# # plt.plot([time[k]*1E9 for k in range(len(time))],[C4[k]*1E3 for k in range(len(C4))],label="Sam Front - 0V - 0.55V/µm")
#
# plt.title("Waveform point A fluence nulle : SAM")
# plt.xlabel("Time (ns)")
# plt.ylabel("Amplitude (mV)")
# plt.legend()


Liste_point = ["PointA" , "PointB" , "PointC" , "PointD" , "PointE"]
numero_point = ["00" , "01" , "02" , "03" , "04", "05" , "06" , "07" , "08" , "09", "10"]
color_i = ["chartreuse","forestgreen","aquamarine","aqua","skyblue","steelblue","blue","rebeccapurple","violet","crimson",'maroon']

plt.figure()
for emplacement in  [Liste_point[4]]:
    for numero_pt in numero_point:
        Adresse_i = "C:\\Users\\molle\\Documents\\LPSC_Stage\\ARRONAX\\ARRONAX_11_22\\Data\\SamEndommagement\\" + emplacement + "\\" + emplacement + "_" + numero_pt + "\\"
        nom_fichier_C2_i = "C2--" + emplacement + "_" + numero_pt + "--"
        nombre_waveform = 30
        C2 = [0.0 for i in range(2500002)]

        filename = nom_fichier_C2_i
        os.chdir(Adresse_i)
        print("Ouverture de " + filename)
        # for i in range(nombre_waveform, nombre_waveform+1):
        for i in range(10,nombre_waveform + 1):
            waveform = str(i).zfill(5)
            if(os.path.isfile(filename + str(waveform) + '.trc')):
                time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
                # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
                # plt.xlabel("Time (ns)")
                # plt.ylabel("Amplitude (mV)")
                # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
                if numero_pt == "00":
                    for j in range(len(amplitude)):
                        C2[j] = (amplitude[j]/10.+C2[j]*i)/(i+1)
                else :
                    for j in range(len(amplitude)):
                        C2[j] = (amplitude[j]  + C2[j] * i) / (i + 1)
        legend_i = emplacement + " - " + numero_pt
        # amplitude = [C2[i] / 10000. for i in range(len(C2))]
        time =  [time[i]*1E6 for i in range(len(time))]
        plt.plot(time,C2,label = legend_i,color=color_i[numero_point.index(numero_pt)])

plt.xlabel("Time (µs)")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.title("Waveform Point E")

plt.show()


