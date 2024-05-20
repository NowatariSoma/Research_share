import os

# 定数定義
value = 32767
sec = 4096
t_total = 3000  # µs

# Value関数
def Value(kaisu):
    out = []
    cut_num = kaisu * 2 - 1
    for i in range(cut_num):
        if i % 2 == 0:
            out.append(1)
        else:
            out.append(0)
    return out

# write関数
def write(i):
    utu = []
    out = Value(i)
    single_section = sec * (3/5) / len(out)

    for i in range(sec):
        if i <= sec//5 or sec//5*4 <= i:
            utu.append(0)
        else:
            inscope_val = i - sec//5
            if out[int(inscope_val//single_section)] == 1:
                utu.append(value)
            else:
                utu.append(0)
    return utu

# 結果を格納するフォルダの作成
folder_name = 'write_results'
os.makedirs(folder_name, exist_ok=True)

# expの各要素ごとにファイルを作成し、結果を書き込む
exp = [1, 2, 3, 5, 7, 9, 10]
for i in exp:
    result = write(i)
    file_path = os.path.join(folder_name, f'results_{i}.txt')
    with open(file_path, 'w') as file:
        file.write(','.join(map(str, result)) + '\n')

print(f"Results have been written to the folder '{folder_name}'")
