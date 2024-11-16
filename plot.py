import matplotlib.pyplot as plt
import numpy as np
from brainflow.data_filter import (
    DataFilter,
    WindowOperations,
)

with open("data.csv") as f:
    data = f.readlines()
    channel2_data = [float(i.split("\t")[2]) for i in data]
    # plt.figure("raw")
    # plt.plot(channel2_data)

    channel2_data = np.array(channel2_data)
    channel2_data = channel2_data - np.mean(channel2_data)
    # DataFilter.remove_environmental_noise(channel2_data, 256, NoiseTypes.FIFTY.value)

    fft_data = DataFilter.perform_fft(channel2_data, WindowOperations.NO_WINDOW.value)

    N = len(fft_data)
    sr = 256
    time = N / sr
    n = np.arange(N)
    freq = n / time

    plt.figure("fft")
    plt.stem(freq, np.abs(fft_data), "b", markerfmt="", basefmt="b")
    # plt.xlim(0, 10)
    plt.show()
    # channel2_data = [i.split("\t")[2] for i in data]

    # with open("channel2_raw.txt", "w") as f:
    #     f.write(" ".join(channel2_data))
