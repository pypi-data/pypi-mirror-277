from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow.data_filter import DataFilter
import time 

board_id = BoardIds.MUSE_S_BOARD.value
preset = BrainFlowPresets.ANCILLARY_PRESET
board = BoardShim(board_id, BrainFlowInputParams())
BoardShim.disable_board_logger()

### PREPARE SESSION AND START STREAM ###
board.prepare_session()
board.config_board("p52") #or p50 - both give the same result for some reason - need further exploration.
sampling_rate = board.get_sampling_rate(board_id)
board.start_stream()
time.sleep(200)
data = board.get_board_data()

#### PPGs ####
ppg_channels = board.get_ppg_channels(board_id, preset)
# Seems that ppg_ir and ppg_red are respectively 1 and 0
ppg_ir = data[ppg_channels[1]]
ppg_red = data[ppg_channels[0]] 
print("PPGs:", ppg_ir, ppg_red)

#### OXYGEN LEVEL ####
oxygen_level = DataFilter.get_oxygen_level(ppg_ir, ppg_red, sampling_rate)
print("oxygen_level:", oxygen_level)

#### HEART RATE ####
heart_rate = DataFilter.get_heart_rate(ppg_ir, ppg_red, sampling_rate, 8192) 
print("heart_rate:", heart_rate)

board.release_session()
