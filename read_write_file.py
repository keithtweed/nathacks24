import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter


def main():
    BoardShim.enable_dev_board_logger()

    # use synthetic board for demo
    params = BrainFlowInputParams()
    params.serial_port = "COM3"
    params.mac_address = "00:55:DA:B7:F7:DD"
    board = BoardShim(BoardIds.MUSE_2_BLED_BOARD.value, params)
    board.prepare_session()
    for i in range(100):
        board.start_stream()
        BoardShim.log_message(LogLevels.LEVEL_INFO.value, "start sleeping in the main thread")
        time.sleep(6)
        data = board.get_board_data()
        board.stop_stream()

        # demo for data serialization using brainflow API, we recommend to use it instead pandas.to_csv()
        DataFilter.write_file(data, "ishaan1.csv", "a")  # use 'a' for append mode

    board.release_session()

    # demo how to convert it to pandas DF and plot data
    eeg_channels = BoardShim.get_eeg_channels(BoardIds.MUSE_2_BLED_BOARD.value)
    print(eeg_channels)

    


if __name__ == "__main__":
    main()
