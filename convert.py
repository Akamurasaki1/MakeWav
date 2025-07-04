import numpy as np
from jisyo import Token_Name_table, Token_Frequency_table, Token_MIDI_table

###################################  1つのID(104など)を音階名('C3'など)やMIDI番号(45など)に変換する関数  ######################################

# ID -> 音階名
def Name_fromID(token_id, default):
    return Token_Name_table.get(token_id, default)

# ID -> 周波数
def Freq_fromID(token_id, default):
    return Token_Frequency_table.get(token_id, default)

# ID -> MIDI番号
def MIDInum_fromID(token_id, default):
    return Token_MIDI_table.get(token_id, default)



############## ID列([104,102,503,...]など)を音階名列(['C3','D2','A5',....]など)やMIDI番号列([45,52,30,....]など)に変換する関数  #################

# ID列 -> (音階名列/周波数列/MIDI番号列）
def NameArray_fromTokens(token_list, default=0.0):
    if isinstance(token_list, np.ndarray) and token_list.ndim == 2:  # 2D numpy array
        return np.array([
            [c_attr(token, table, default) for token in row]
            for row in token_list.tolist() # Convert row to list for iteration
        ])
    elif isinstance(token_list, list) and all(isinstance(i, list) for i in token_list): # 2D list
         return np.array([
            [c_attr(token, table, default) for token in row]
            for row in token_list
        ])
    elif isinstance(token_list, (list, np.ndarray)):  # 1D list or numpy array
        return np.array([c_attr(token, table, default) for token in token_list])
    else:
        return np.array([]) # Return empty array for unhandled types


# np.array(...) 形式で出力（小数対応）
def format_np_array(array, float_fmt=".3f"):
    # Check if the array is 1D and wrap it in a list if necessary
    if array.ndim == 1:
        array = [array]

    rows = []
    for row in array:
        row_str = ', '.join(f"{x:{float_fmt}}" if isinstance(x, float) else str(x) for x in row)
        rows.append(f"    [{row_str}]")
    return "np.array([\n" + ',\n'.join(rows) + "\n])"

print("使用感のチェック")
token1=[[103,205,700,411],[0,801,302,111]]
# 音名列
print("Note names:")
print(c_attr_array(token1, Token_Name_table, default=""))

# 周波数列（数値＋整形）
freqs = c_attr_array(token1, Token_Frequency_table)
print("Frequencies:")
print(format_np_array(freqs))  # f = np.array([...]) 形式

# MIDI列（整数＋整形）
midi = c_attr_array(token1, Token_MIDI_table, default=0)
print("MIDI:")
print(format_np_array(midi, float_fmt="d"))  # 小数ではなく整数表示