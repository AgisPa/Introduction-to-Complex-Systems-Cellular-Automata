
import matplotlib.pyplot as plt
import numpy as np
import diploid_ECA
import tkinter as tk
from tkinter import simpledialog

numfunc=10

def linetocircle(system):
    N=len(system)
    theta = np.linspace(0, N, N)
    pltfunc = [[0 for i in range(N)] for j in range(N)]
    for k in range(0, N):
        xcord = int(N * np.cos(theta[k] * 360 / N) / 2)
        ycord = int(N * np.sin(theta[k] * 360 / N) / 2)
        if int(system[k]) == 1 and abs(xcord) < N/2 and abs(ycord) < N/2:
            pltfunc[xcord + int(N/2)][ycord + int(N/2)] = 1
    return pltfunc



def plotting(system,wolfram_number,weight,T):
    N=len(system)
    ROOT = tk.Tk()
    ROOT.eval('tk::PlaceWindow . center')

    ROOT.withdraw()
    input = simpledialog.askstring(title="Plot Choice",
                                   prompt="Choose a type of plot Density, MultiDensity, Circle, Space-time, None")
    spacetime=[[0 for i in range(N)] for j in range(T)]
    rho=[0 for i in range(T)]
    rhol=[[0 for i in range(T)] for j in range(numfunc+2)]

    plt.figure(figsize=(8, 8))
    t=0
    while t in range(0,T):
        plt.clf()
        if input=="Circle":
            if len(system)<=1000:
                new_system = diploid_ECA.diploid_update_rule(system, wolfram_number, weight)
                plot=linetocircle(system)
                system=new_system
                plt.title("Circular chain plot")
                plt.contourf(plot, 10, cmap=plt.cm.bone)
                plt.pause(0.1)
                t=t+1
            else:
                print("System size too big for circle representation")
                t=t+1
        elif input=="Space-time":
            new_system=diploid_ECA.diploid_update_rule(system, wolfram_number, weight)
            spacetime[t][:]=new_system
            plot=spacetime
            system=new_system
            plt.title("Space-Time plot")
            plt.ylabel("Time steps")
            plt.xlabel("Cells")
            plt.contourf(plot, 10, cmap=plt.cm.bone)
            plt.pause(0.002)
            t=t+1
        elif input=="Density":
            rho[t]=np.mean(system)
            new_system=diploid_ECA.diploid_update_rule(system, wolfram_number, weight)
            system=new_system
            t=t+1
        elif input=="None":
            cellular_automaton_new = diploid_ECA.diploid_simulation(system, wolfram_number, weight, T)
            t=t+T
        elif input=="MultiDensity":
            t=t+T
        else:
            print("Invalid input")
            input = simpledialog.askstring(title="Plot Choice",
                                        prompt="Choose a type of plot: Density, Space-time or Circle")

    if input == "MultiDensity":
        init=[0 for i in range(N)]
        for i in range(0,N):
            init[i]=system[i]
        for l in range(1,numfunc+2):
            system=init
            for t in range(0, T):
                rhol[l][t] = np.mean(system)
                new_system = diploid_ECA.diploid_update_rule(system, wolfram_number, l/10)
                system = new_system
            plt.title("MultiDensity plot")
            plt.ylabel("Density")
            plt.xlabel("Time steps")
            a=[0.1,0.2,0.3,0.4,0.5, 0.6, 0.7, 0.8,0.9,1]
            plt.legend(a)
            plt.ylim(0, 1)
            plt.plot(np.linspace(0, T, T), rhol[:][l], color=(0.01*l,0.09*l,0.09*l),label=a , marker='o', linestyle='dashed', linewidth=1,
                     markersize=3)
    plt.show()

    if input=="Density":
        plt.title("Density plot")
        plt.ylabel("Density")
        plt.xlabel("Time steps")
        plt.ylim(0,1)
        plt.plot(np.linspace(0,T,T),rho, color='black', marker='o', linestyle='dashed',linewidth=3, markersize=7)
        plt.show()
    if input=="None":
        return cellular_automaton_new
    else:
        return "null"
