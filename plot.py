import matplotlib.pyplot as plt
import numpy as np
from brainflow.data_filter import (
    DataFilter,
    WaveletTypes,
    WaveletDenoisingTypes,
    WaveletExtensionTypes,
    ThresholdTypes,
    NoiseEstimationLevelTypes,
    WindowOperations,
)

with open("data.csv") as f:
    data = f.readlines()
    channel2_data = [float(i.split("\t")[2]) for i in data]
    plt.figure("raw")
    plt.plot(channel2_data)

    channel2_data = np.array(channel2_data)
    DataFilter.perform_wavelet_denoising(
        channel2_data,
        WaveletTypes.BIOR3_9,
        3,
        WaveletDenoisingTypes.SURESHRINK,
        ThresholdTypes.HARD,
        WaveletExtensionTypes.SYMMETRIC,
        NoiseEstimationLevelTypes.FIRST_LEVEL,
    )
    fft_data = DataFilter.perform_fft(channel2_data, WindowOperations.NO_WINDOW.value)
    plt.figure("fft")
    plt.plot(fft_data)
    plt.show()
    # channel2_data = [i.split("\t")[2] for i in data]

    # with open("channel2_raw.txt", "w") as f:
    #     f.write(" ".join(channel2_data))
