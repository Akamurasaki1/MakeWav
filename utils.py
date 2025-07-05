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

# 2列のnp.array形式(np.array([~,~,~,....,~],[~,~,...,~]) で出力（小数対応）
def format_np_array(array, float_fmt=".3f"):
    # Check if the array is 1D and wrap it in a list if necessary
    if array.ndim == 1:
        array = [array]

    rows = []
    for row in array:
        row_str = ', '.join(f"{x:{float_fmt}}" if isinstance(x, float) else str(x) for x in row)
        rows.append(f" [{row_str}]")
    return "np.array([\n"+',\n'.join(rows) + "\n])"