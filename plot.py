import matplotlib.pyplot as plt
import numpy as np
from brainflow.data_filter import (
    DataFilter,
    FilterTypes,
    WindowOperations
)

with open("data.csv") as f:
    data = f.readlines()
    channel2_data = [float(i.split("\t")[2]) for i in data]
    plt.figure("raw")
    plt.plot(channel2_data)

    sampling_rate = 256
    lowcut = 8
    highcut = 12
    order = 4

    channel2_data = np.array(channel2_data)
    DataFilter.perform_bandpass(
        channel2_data,
        sampling_rate,
        lowcut,
        highcut,
        order,
        FilterTypes.BUTTERWORTH.value,
        0.5
    )
    fft_data = DataFilter.perform_fft(channel2_data, WindowOperations.HAMMING.value)
    plt.figure("fft")
    plt.plot(fft_data)
    plt.show()
    # channel2_data = [i.split("\t")[2] for i in data]

    # with open("channel2_raw.txt", "w") as f:
    #     f.write(" ".join(channel2_data))
