# coding: utf-8
import numpy as np
from jisyo import Token_Name_table, Token_Frequency_table, Token_MIDI_table

###################################  1つのID(104など)を音階名('C3'など)やMIDI番号(45など)に変換する関数  ######################################

# ID -> 音階pi名
def Name_fromID(token_id, default):
    return Token_Name_table.get(token_id, default)

# ID -> 周波数
def Freq_fromID(token_id, default):
    return Token_Frequency_table.get(token_id, default)

# ID -> MIDI番号
def MIDInum_fromID(token_id, default):
    return Token_MIDI_table.get(token_id, default)



############## ID列([104,102,503,...]など)を音階名列(['C3','D2','A5',....]など)やMIDI番号列([45,52,30,....]など)に変換する関数  #################

# ID列 -> 音階名列
def Names_fromIDs(token_ids, default='UNK'):
    return [Name_fromID(tid, default) for tid in token_ids]

# ID列 -> 周波数列
def Freqs_fromIDs(token_ids, default=0.0):
    return [Freq_fromID(tid, default) for tid in token_ids]

# ID列 -> MIDI番号列
def MIDInums_fromIDs(token_ids, default=-1):
    return [MIDInum_fromID(tid, default) for tid in token_ids]


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

print(Names_fromIDs([104, 102, 503, 911])) 
print(Freqs_fromIDs([104, 102, 503, 911]))
print(MIDInums_fromIDs([104, 102, 503, 911]))


      