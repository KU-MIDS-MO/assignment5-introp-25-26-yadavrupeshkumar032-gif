import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    diff = np.diff(signal)

    turning_points = np.where(diff[1:] * diff[:-1] < 0)[0] + 1

    plt.plot(signal)
    plt.scatter(turning_points, signal[turning_points], color='red')
    plt.xlabel("Index")
    plt.ylabel("Signal")
    plt.title("Turning Points")
    
    plt.savefig(filename)
    plt.show()
    
    return turning_points