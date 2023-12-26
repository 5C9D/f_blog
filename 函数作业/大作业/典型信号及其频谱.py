# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 生成正弦波信号
fs = 1000  # 采样频率
t = np.arange(0, 1, 1/fs)  # 时间序列
n = np.linspace(0,1,100)   # 离散采样及时间
f = 10  # 信号频率

y1 = np.cos(2*np.pi*f*t)  # 余弦波信号（连续）
y2 = np.sin(2*np.pi*f*t)  # 正弦波信号（连续）
y3 = np.cos(2*np.pi*f*n)  # 余弦波信号（离散）
y4 = np.sin(2*np.pi*f*n)  # 正弦波信号（离散）

# 计算频谱
X1 = np.fft.fft(y1)         # 余弦波信号频谱（连续）
X2 = np.fft.fft(y2)         # 正弦波信号频谱（连续）
X3 = np.fft.fft(y3)         # 余弦波信号频谱（离散）
X4 = np.fft.fft(y4)         # 正弦波信号频谱（离散）

freqs1 = np.fft.fftfreq(len(t), 1/fs)
freqs2 = np.fft.fftfreq(len(n), 1/fs)
def ctcos():
    plt.plot(t, y1)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB)')
    plt.title('Graph of the Signal')
    plt.show()

def ctcospp():
    plt.plot(freqs1, np.abs(X1))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Spectrum of the Signal')
    plt.show()

def ctsin():
    plt.plot(t, y2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB)')
    plt.title('Graph of the Signal')
    plt.show()

def ctsinpp():
    plt.plot(freqs1, np.abs(X2))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Spectrum of the Signal')
    plt.show()

def dccos():

    plt.title('cos(n)')
    plt.grid(True)
    plt.stem(n, y3)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB)')
    plt.title('Graph of the Signal')
    plt.show()

def dccospp():
    plt.stem(freqs2, np.abs(X3))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Spectrum of the Signal')
    plt.show()

def dcsin():
    plt.title('sin(n)')
    plt.grid(True)
    plt.stem(n, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB)')
    plt.title('Graph of the Signal')
    plt.show()

def dcsinpp():
    plt.stem(freqs2, np.abs(X4))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Spectrum of the Signal')
    plt.show()

from tkinter import *
root = Tk()
root.title("离散信号图像")
root.geometry("325x60+100+100")
btn01 = Button(root)
btn02 = Button(root)
btn03 = Button(root)
btn04 = Button(root)
btn05 = Button(root)
btn06 = Button(root)
btn07 = Button(root)
btn08 = Button(root)

btn01["text"] = "连续cos(t)"
btn02["text"] = "连续cos(t)频谱"
btn03["text"] = "连续sin(t)"
btn04["text"] = "连续sin(t)频谱"
btn05["text"] = "离散cos(n)"
btn06["text"] = "离散cos(n)频谱"
btn07["text"] = "离散sin(n)"
btn08["text"] = "离散sin(n)频谱"
btn01["command"] = ctcos
btn02["command"] = ctcospp
btn03["command"] = ctsin
btn04["command"] = ctsinpp
btn05["command"] = dccos
btn06["command"] = dccospp
btn07["command"] = dcsin
btn08["command"] = dcsinpp

btn01.grid(row=0, column=0)
btn02.grid(row=0, column=1)
btn03.grid(row=0, column=2)
btn04.grid(row=0, column=3)
btn05.grid(row=1, column=0)
btn06.grid(row=1, column=1)
btn07.grid(row=1, column=2)
btn08.grid(row=1, column=3)
root.mainloop()


