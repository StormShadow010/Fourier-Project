import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import sk_dsp_comm.sigsys as ss

#Onda Cuadrada
def onda_duadrada(A,T,harmonics):
    #Espacio de graficación
    t = np.linspace(-T*2, T*2, 1000, endpoint=False)
    #Funciones por cada armónico con referencia al espacio de graficación
    functions=[]
    [functions.append((1/(2*i-1))*np.sin((2*i-1)*(2*np.pi*1/T)*t)) for i in range(1,harmonics+1,1)]
    #Señal tren de pulsos rectangular
    signal_o=A*signal.square((2 * np.pi/T) * t)
    #Gráfica 1 Señal Original y Serie de Fourier
    fig,axs = plt.subplots(2)
    axs[0].set_title('Onda Cuadrada')
    axs[0].plot(t,signal_o,t,(4*A/np.pi)*np.sum(functions,axis=0))
    axs[0].legend(["Señal original","Serie de Fourier"], loc ="upper right")
    #Gráfica 2 Armónicos
    axs[1].set_title('Armónicos')
    [axs[1].plot(t,functions[i]) for i in range(0,len(functions),1)]  
    legends=[]
    [legends.append(f"Armónico {i}") for i in range(1,harmonics+1,1)]
    axs[1].legend(legends, loc ="upper right")  
    #Ajustes gráficas en general
    plt.subplots_adjust(hspace=0.5)
    [ax.set(xlabel='t', ylabel='f(t)') for ax in axs.flat]
    [ax.label_outer() for ax in axs.flat]
    [axs[i].grid(True) for i in range(0,2,1)]
    plt.show()

#Tren de pulsos rectangular
def tren_de_pulsos_rectangular(A,T,harmonics,duration):
    #Duración del pulso
    tao=(T*duration/100)
    #Espacio de graficación
    t = np.linspace(-T*2, T*2, 1000, endpoint=False)
    #Funciones por cada armónico con referencia al espacio de graficación
    functions=[]
    [functions.append((2*A/(i*np.pi))*np.sin(i*np.pi*tao/T)*np.cos(i*(2*np.pi*1/T)*t)) for i in range(1,harmonics+1,1)]
    #Señal tren de pulsos rectangular
    signal_o=A*ss.rect(np.mod(t+T/2,T)-T/2,(duration)/(100/T))
    #Dejar solo la parte positiva
    for i in range(0,len(signal_o),1):
        if signal_o[i]<0:signal_o[i]=0 
    #Gráfica 1 Señal Original y Serie de Fourier
    fig,axs = plt.subplots(2)
    axs[0].set_title('Tren de pulsos rectangular')
    axs[0].plot(t,signal_o,t,(A*tao/T)+np.sum(functions,axis=0))
    axs[0].legend(["Señal original","Serie de Fourier"], loc ="upper right")
    #Gráfica 2 Armónicos
    axs[1].set_title('Armónicos')
    [axs[1].plot(t,functions[i]) for i in range(0,len(functions),1)]  
    legends=[]
    [legends.append(f"Armónico {i}") for i in range(1,harmonics+1,1)]
    axs[1].legend(legends, loc ="upper right")  
    #Ajustes gráficas en general
    plt.subplots_adjust(hspace=0.5)
    [ax.set(xlabel='t', ylabel='f(t)') for ax in axs.flat]
    [ax.label_outer() for ax in axs.flat]
    [axs[i].grid(True) for i in range(0,2,1)]
    plt.show()

#Onda diente de Sierra
def onda_diente_de_sierra(A,T,harmonics):
    #Espacio de graficación
    t = np.linspace(-T*2, T*2, 1000, endpoint=False)
    #Funciones por cada armónico con referencia al espacio de graficación
    functions=[]
    [functions.append(np.sin(i*2*np.pi*(1/T)*t)/i) for i in range(1,harmonics+1,1)]
    #Onda diente de Sierra
    signal_o=A/2+A/2*signal.sawtooth(2 * np.pi * (1/T) * t)  
    #Gráfica 1 Señal Original y Serie de Fourier
    fig,axs = plt.subplots(2)
    axs[0].set_title('Onda diente de Sierra')
    axs[0].plot(t,signal_o,t,A/2-(A/np.pi)*np.sum(functions,axis=0))
    axs[0].legend(["Señal original","Serie de Fourier"], loc ="upper right")
    #Gráfica 2 Armónicos
    axs[1].set_title('Armónicos')
    [axs[1].plot(t,functions[i]) for i in range(0,len(functions),1)]  
    legends=[]
    [legends.append(f"Armónico {i}") for i in range(1,harmonics+1,1)]
    axs[1].legend(legends, loc ="upper right")  
    #Ajustes gráficas en general
    plt.subplots_adjust(hspace=0.5)
    [ax.set(xlabel='t', ylabel='f(t)') for ax in axs.flat]
    [ax.label_outer() for ax in axs.flat]
    [axs[i].grid(True) for i in range(0,2,1)]
    plt.show()

#Onda triangular
def onda_triangular(A,T,harmonics):
    #Espacio de graficación
    t = np.linspace(-T*2, T*2, 1000, endpoint=False)
    #Funciones por cada armónico con referencia al espacio de graficación
    functions=[]
    [functions.append((1/(2*i-1)**2)*np.cos((2*i-1)*(2*np.pi*(1/T))*t)) for i in range(1,harmonics+1,1)]
    #Onda diente de Sierra
    signal_o = A/2+A/2*signal.sawtooth(2 * np.pi * 1/T * t, 0.50)
    #Gráfica 1 Señal Original y Serie de Fourier
    fig,axs = plt.subplots(2)
    axs[0].set_title('Onda triangular')
    axs[0].plot(t,signal_o,t,A/2-(4*A/np.pi**2)*np.sum(functions,axis=0))
    axs[0].legend(["Señal original","Serie de Fourier"], loc ="upper right")
    #Gráfica 2 Armónicos
    axs[1].set_title('Armónicos')
    [axs[1].plot(t,functions[i]) for i in range(0,len(functions),1)]  
    legends=[]
    [legends.append(f"Armónico {i}") for i in range(1,harmonics+1,1)]
    axs[1].legend(legends, loc ="upper right")  
    #Ajustes gráficas en general
    plt.subplots_adjust(hspace=0.5)
    [ax.set(xlabel='t', ylabel='f(t)') for ax in axs.flat]
    [ax.label_outer() for ax in axs.flat]
    [axs[i].grid(True) for i in range(0,2,1)]
    plt.show()

#Función seno rectificado de media onda #Storm Shadow 010
def funcion_seno_rectificado_de_media_onda(A,T,harmonics):
    #Espacio de graficación
    t = np.linspace(-T*2, T*2, 1000, endpoint=False)
    #Funciones por cada armónico con referencia al espacio de graficación
    functions=[]
    [functions.append((1/(4*i**2-1))*np.cos(2*i*2*np.pi*(1/T)*t)) for i in range(1,harmonics+1,1)] 
    #Función seno rectificado de media onda
    signal_o =A*np.sin(2*np.pi*(1/T)*t)
    for i in range(0,len(signal_o),1):
        if signal_o[i]<0: signal_o[i]=0
    #Gráfica 1 Señal Original y Serie de Fourier
    fig,axs = plt.subplots(2)
    axs[0].set_title('Función seno rectificado de media onda')
    axs[0].plot(t,signal_o,t,(A/np.pi)+(A/2)*np.sin(2*np.pi*(1/T)*t)-(2*A/np.pi)*np.sum(functions,axis=0))
    axs[0].legend(["Señal original","Serie de Fourier"], loc ="upper right")
    #Gráfica 2 Armónicos
    axs[1].set_title('Armónicos')
    [axs[1].plot(t,functions[i]) for i in range(0,len(functions),1)]  
    legends=[]
    [legends.append(f"Armónico {i}") for i in range(1,harmonics+1,1)]
    axs[1].legend(legends, loc ="upper right")  
    #Ajustes gráficas en general
    plt.subplots_adjust(hspace=0.5)
    [ax.set(xlabel='t', ylabel='f(t)') for ax in axs.flat]
    [ax.label_outer() for ax in axs.flat]
    [axs[i].grid(True) for i in range(0,2,1)]
    plt.show()  

#Función seno rectificado de onda completa
def funcion_seno_rectificado_de_onda_completa(A,T,harmonics):
    #Espacio de graficación
    t = np.linspace(-T*2, T*2, 1000, endpoint=False)
    #Funciones por cada armónico con referencia al espacio de graficación
    functions=[]
    [functions.append((1/(4*i**2-1))*np.cos(2*i*2*np.pi*(1/T)*t)) for i in range(1,harmonics+1,1)]    
    #Función seno rectificado de onda completa
    signal_o =abs(A*np.sin(2*np.pi*(1/T)*t))
    #Gráfica 1 Señal Original y Serie de Fourier
    fig,axs = plt.subplots(2)
    axs[0].set_title('Función seno rectificado de onda completa')
    axs[0].plot(t,signal_o,t,(2*A/np.pi)-(4*A/np.pi)*np.sum(functions,axis=0))
    axs[0].legend(["Señal original","Serie de Fourier"], loc ="upper right")
    #Gráfica 2 Armónicos
    axs[1].set_title('Armónicos')
    [axs[1].plot(t,functions[i]) for i in range(0,len(functions),1)]  
    legends=[]
    [legends.append(f"Armónico {i}") for i in range(1,harmonics+1,1)]
    axs[1].legend(legends, loc ="upper right")  
    #Ajustes gráficas en general
    plt.subplots_adjust(hspace=0.5)
    [ax.set(xlabel='t', ylabel='f(t)') for ax in axs.flat]
    [ax.label_outer() for ax in axs.flat]
    [axs[i].grid(True) for i in range(0,2,1)]
    plt.show()  
#Storm Shadow 010
