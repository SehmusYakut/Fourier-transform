import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

# Functions to generate and plot signals for the first question
def generate_signals_v1():
    try:
        A1 = float(entry_A1_v1.get())
        f1 = float(entry_f1_v1.get())
        theta1 = float(entry_theta1_v1.get())

        A2 = float(entry_A2_v1.get())
        f2 = float(entry_f2_v1.get())
        theta2 = float(entry_theta2_v1.get())

        A3 = float(entry_A3_v1.get())
        f3 = float(entry_f3_v1.get())
        theta3 = float(entry_theta3_v1.get())

        t = np.linspace(0, 1, 1000)

        sin1 = A1 * np.sin(2 * np.pi * f1 * t + np.radians(theta1))
        cos1 = A1 * np.cos(2 * np.pi * f1 * t + np.radians(theta1))

        sin2 = A2 * np.sin(2 * np.pi * f2 * t + np.radians(theta2))
        cos2 = A2 * np.cos(2 * np.pi * f2 * t + np.radians(theta2))

        sin3 = A3 * np.sin(2 * np.pi * f3 * t + np.radians(theta3))
        cos3 = A3 * np.cos(2 * np.pi * f3 * t + np.radians(theta3))

        sin_synthesis = sin1 + sin2 + sin3
        cos_synthesis = cos1 + cos2 + cos3

        plot_signals_v1(t, sin1, cos1, sin2, cos2, sin3, cos3, sin_synthesis, cos_synthesis)
    except ValueError:
        print("Please enter all values correctly.")

def plot_signals_v1(t, sin1, cos1, sin2, cos2, sin3, cos3, sin_synthesis, cos_synthesis):
    fig, axs = plt.subplots(4, 1, figsize=(10, 8))

    axs[0].plot(t, sin1, label='Sin1')
    axs[0].plot(t, cos1, label='Cos1')
    axs[0].legend()
    axs[0].set_title('Sin1 and Cos1')

    axs[1].plot(t, sin2, label='Sin2')
    axs[1].plot(t, cos2, label='Cos2')
    axs[1].legend()
    axs[1].set_title('Sin2 and Cos2')

    axs[2].plot(t, sin3, label='Sin3')
    axs[2].plot(t, cos3, label='Cos3')
    axs[2].legend()
    axs[2].set_title('Sin3 and Cos3')

    axs[3].plot(t, sin_synthesis, label='Sin Synthesis')
    axs[3].plot(t, cos_synthesis, label='Cos Synthesis')
    axs[3].legend()
    axs[3].set_title('Synthesized Signal')

    for ax in axs:
        ax.grid(True)

    plt.tight_layout()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fig.savefig(f"sinusoidal_signals_v1_{timestamp}.png")
    canvas = FigureCanvasTkAgg(fig, master=frame_v1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=6)

# Functions to generate and plot signals for the second question
def generate_signals_v2():
    try:
        a0_1 = float(entry_a0_1_v2.get())
        a1_1 = float(entry_a1_1_v2.get())
        b1_1 = float(entry_b1_1_v2.get())
        w1 = float(entry_w1_v2.get())
        T1 = float(entry_T1_v2.get())

        a0_2 = float(entry_a0_2_v2.get())
        a1_2 = float(entry_a1_2_v2.get())
        b1_2 = float(entry_b1_2_v2.get())
        w2 = float(entry_w2_v2.get())
        T2 = float(entry_T2_v2.get())

        a0_3 = float(entry_a0_3_v2.get())
        a1_3 = float(entry_a1_3_v2.get())
        b1_3 = float(entry_b1_3_v2.get())
        w3 = float(entry_w3_v2.get())
        T3 = float(entry_T3_v2.get())

        t1 = np.linspace(0, T1, 1000)
        t2 = np.linspace(0, T2, 1000)
        t3 = np.linspace(0, T3, 1000)

        sin1 = a0_1 + a1_1 * np.sin(1 * w1 * t1) + b1_1 * np.cos(1 * w1 * t1)
        sin2 = a0_2 + a1_2 * np.sin(2 * w2 * t2) + b1_2 * np.cos(2 * w2 * t2)
        sin3 = a0_3 + a1_3 * np.sin(3 * w3 * t3) + b1_3 * np.cos(3 * w3 * t3)

        sin_synthesis = sin1 + sin2 + sin3

        plot_signals_v2(t1, t2, t3, sin1, sin2, sin3, sin_synthesis)
    except ValueError:
        print("Please enter all values correctly.")

def plot_signals_v2(t1, t2, t3, sin1, sin2, sin3, sin_synthesis):
    fig, axs = plt.subplots(4, 1, figsize=(10, 8))

    axs[0].plot(t1, sin1, label='Sin1 and Cos1')
    axs[0].legend()
    axs[0].set_title('Sin1 and Cos1')

    axs[1].plot(t2, sin2, label='Sin2 and Cos2')
    axs[1].legend()
    axs[1].set_title('Sin2 and Cos2')

    axs[2].plot(t3, sin3, label='Sin3 and Cos3')
    axs[2].legend()
    axs[2].set_title('Sin3 and Cos3')

    axs[3].plot(np.linspace(0, max(max(t1), max(t2), max(t3)), 1000), sin_synthesis, label='Synthesized Signal')
    axs[3].legend()
    axs[3].set_title('Synthesized Signal')

    for ax in axs:
        ax.grid(True)

    plt.tight_layout()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fig.savefig(f"sinusoidal_signals_v2_{timestamp}.png")
    canvas = FigureCanvasTkAgg(fig, master=frame_v2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=11, column=0, columnspan=6)

# Main window and tab control
root = tk.Tk()
root.title("Signal Plotting Interface")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='GENERATE SIGNALS')
tabControl.add(tab2, text='FOURIER SYNTHESIS')
tabControl.pack(expand=1, fill="both")

# UI for the first question
frame_v1 = ttk.Frame(tab1, padding="10")
frame_v1.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame_v1, text="Amplitude A1 (V):").grid(row=0, column=0)
entry_A1_v1 = ttk.Entry(frame_v1)
entry_A1_v1.grid(row=0, column=1)

ttk.Label(frame_v1, text="Frequency f1 (Hz):").grid(row=1, column=0)
entry_f1_v1 = ttk.Entry(frame_v1)
entry_f1_v1.grid(row=1, column=1)

ttk.Label(frame_v1, text="Phase θ1 (°):").grid(row=2, column=0)
entry_theta1_v1 = ttk.Entry(frame_v1)
entry_theta1_v1.grid(row=2, column=1)

ttk.Label(frame_v1, text="Amplitude A2 (V):").grid(row=0, column=2)
entry_A2_v1 = ttk.Entry(frame_v1)
entry_A2_v1.grid(row=0, column=3)

ttk.Label(frame_v1, text="Frequency f2 (Hz):").grid(row=1, column=2)
entry_f2_v1 = ttk.Entry(frame_v1)
entry_f2_v1.grid(row=1, column=3)

ttk.Label(frame_v1, text="Phase θ2 (°):").grid(row=2, column=2)
entry_theta2_v1 = ttk.Entry(frame_v1)
entry_theta2_v1.grid(row=2, column=3)

ttk.Label(frame_v1, text="Amplitude A3 (V):").grid(row=0, column=4)
entry_A3_v1 = ttk.Entry(frame_v1)
entry_A3_v1.grid(row=0, column=5)

ttk.Label(frame_v1, text="Frequency f3 (Hz):").grid(row=1, column=4)
entry_f3_v1 = ttk.Entry(frame_v1)
entry_f3_v1.grid(row=1, column=5)

ttk.Label(frame_v1, text="Phase θ3 (°):").grid(row=2, column=4)
entry_theta3_v1 = ttk.Entry(frame_v1)
entry_theta3_v1.grid(row=2, column=5)

ttk.Button(frame_v1, text="Plot", command=generate_signals_v1).grid(row=3, column=0, columnspan=6)

# UI for the second question
frame_v2 = ttk.Frame(tab2, padding="10")
frame_v2.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame_v2, text="a0 (Signal 1):").grid(row=0, column=0)
entry_a0_1_v2 = ttk.Entry(frame_v2)
entry_a0_1_v2.grid(row=0, column=1)

ttk.Label(frame_v2, text="a1 (Signal 1):").grid(row=1, column=0)
entry_a1_1_v2 = ttk.Entry(frame_v2)
entry_a1_1_v2.grid(row=1, column=1)

ttk.Label(frame_v2, text="b1 (Signal 1):").grid(row=2, column=0)
entry_b1_1_v2 = ttk.Entry(frame_v2)
entry_b1_1_v2.grid(row=2, column=1)

ttk.Label(frame_v2, text="ω1 (rad/s):").grid(row=3, column=0)
entry_w1_v2 = ttk.Entry(frame_v2)
entry_w1_v2.grid(row=3, column=1)

ttk.Label(frame_v2, text="T1 (s):").grid(row=4, column=0)
entry_T1_v2 = ttk.Entry(frame_v2)
entry_T1_v2.grid(row=4, column=1)

ttk.Label(frame_v2, text="a0 (Signal 2):").grid(row=0, column=2)
entry_a0_2_v2 = ttk.Entry(frame_v2)
entry_a0_2_v2.grid(row=0, column=3)

ttk.Label(frame_v2, text="a1 (Signal 2):").grid(row=1, column=2)
entry_a1_2_v2 = ttk.Entry(frame_v2)
entry_a1_2_v2.grid(row=1, column=3)

ttk.Label(frame_v2, text="b1 (Signal 2):").grid(row=2, column=2)
entry_b1_2_v2 = ttk.Entry(frame_v2)
entry_b1_2_v2.grid(row=2, column=3)

ttk.Label(frame_v2, text="ω2 (rad/s):").grid(row=3, column=2)
entry_w2_v2 = ttk.Entry(frame_v2)
entry_w2_v2.grid(row=3, column=3)

ttk.Label(frame_v2, text="T2 (s):").grid(row=4, column=2)
entry_T2_v2 = ttk.Entry(frame_v2)
entry_T2_v2.grid(row=4, column=3)

ttk.Label(frame_v2, text="a0 (Signal 3):").grid(row=0, column=4)
entry_a0_3_v2 = ttk.Entry(frame_v2)
entry_a0_3_v2.grid(row=0, column=5)

ttk.Label(frame_v2, text="a1 (Signal 3):").grid(row=1, column=4)
entry_a1_3_v2 = ttk.Entry(frame_v2)
entry_a1_3_v2.grid(row=1, column=5)

ttk.Label(frame_v2, text="b1 (Signal 3):").grid(row=2, column=4)
entry_b1_3_v2 = ttk.Entry(frame_v2)
entry_b1_3_v2.grid(row=2, column=5)

ttk.Label(frame_v2, text="ω3 (rad/s):").grid(row=3, column=4)
entry_w3_v2 = ttk.Entry(frame_v2)
entry_w3_v2.grid(row=3, column=5)

ttk.Label(frame_v2, text="T3 (s):").grid(row=4, column=4)
entry_T3_v2 = ttk.Entry(frame_v2)
entry_T3_v2.grid(row=4, column=5)

ttk.Button(frame_v2, text="Plot", command=generate_signals_v2).grid(row=5, column=0, columnspan=6)

root.mainloop()
