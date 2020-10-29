import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)
X=[2,1.5,1,0.5]

def dcsin():
    y1=np.sin(np.pi*x+2)
    plt.title('sin(n)')
    plt.grid(True)
    plt.stem(x,y1)
    plt.show()

def dcex():
    y4=2*0.5**x1
    plt.grid(True)
    plt.title('e^x(n)')
    plt.stem(x1,y4)
    plt.show()

def dcsf():
    def dcs(t):
        r=np.where(t>=0.0,1.0,0.0)
        return r
    n=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('u(n)')
    plt.grid(True)
    plt.stem(n,dcs(n))
    plt.show()

def dcif():
    def dci(temp):
        r=np.where(temp==0.0,1.0,0.0)
        return r
    m=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('δ(n)')
    plt.grid(True)
    plt.stem(m,dci(m))
    plt.show()


from tkinter import *
root = Tk()
root.title("离散信号图像")

Button(root,text="离散sin",command=dcsin).pack(side=LEFT)
Button(root,text="离散e^x",command=dcex).pack(side=LEFT)
Button(root,text="离散阶跃",command=dcsf).pack(side=LEFT)
Button(root,text="离散冲击",command=dcif).pack(side=RIGHT)

root.mainloop()