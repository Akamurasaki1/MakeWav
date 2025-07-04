import os
# utils.py
#  ファイル名が既に存在する場合は `-1`, `-2`, ... をつけて上書きを回避。
# 例: "output.wav" → "output-1.wav" → "output-2.wav"
def avoid_overwrite(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}-{counter}{ext}"
        counter += 1
    return new_filename