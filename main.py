import requests
from calculate import calculator

def to_base_2(x):
    k = ''
    while x > 1:
        x, k = x // 2, str(x % 2) + k
    return str(x) + k



def to_base_16(x):
    alphabet = '0123456789ABCDEF'
    return alphabet[int(x, 2)]


def normalize_digit(a):
    return '0' * ((4 - (len(a) % 4)) % 4) + a


def add_point_by_four(a):
    a = a[::-1]
    new_a = ''
    count = 0
    for i in a:
        if i.isdigit():
            count += 1
        new_a += i
        if count == 4:
            count = 0
            new_a += '.'
    if new_a[-1] == '.':
        new_a = new_a[:-1]
    new_a = new_a[::-1]
    return new_a


def task_one(a):
    bcd_format, ascii_format = [], ""
    for i in a:
        i = normalize_digit(to_base_2(int(i)))
        bcd_format.append(i)
        ascii_format += f'0011.{i} '
    if len(bcd_format) % 2 != 0:
        bcd_format.insert(0, '0000')
    bcd_format = '.'.join(bcd_format)
    answer = f'1. Заданное число А представить в двоично-кодированной форме:'
    answer += f'\nа) в упакованном формате (BCD): {bcd_format}'
    answer += f'\nб) в неупакованном формате (ASCII): {ascii_format}'
    return answer


def task_two(a):
    base_to_digit = to_base_2(int(a))
    answer = f'2. Заданные число А и число –A представить в виде целого числа в форме с фиксированной запятой в' \
             f' формате WORD (16-битный формат).\nA = {a} (10) = {base_to_digit} (2)'
    a_16 = '0' * (16 - len(base_to_digit)) + base_to_digit
    a_rev_16 = ""
    for i in a_16:
        if i == '1':
            a_rev_16 += '0'
        else:
            a_rev_16 += '1'
    a_dop_16 = to_base_2(int(a_rev_16, 2) + 1)
    answer += f"\nA = {'0|' + add_point_by_four(a_16)[1::]}"
    answer += f"\nОтрицательные:\n[A] прям. = {'1.' + add_point_by_four(a_16)[1::]}"
    answer += f'\n[-A] обр. = {"1." + add_point_by_four(a_rev_16)[1::]}'
    answer += f'\n[-A] доп. = {"1." + add_point_by_four(a_dop_16)[1::]}'
    return answer


def task_three(a, b):
    answer = "3. Заданные числа A и B представить в форме с плавающей запятой в формате Ф1."
    if int(a) >= 0:
        zn = "0"
    else:
        zn = "1"
    if float(b) >= 0:
        zn_b = '0'
    else:
        zn_b = '1'
    a_2 = add_point_by_four(normalize_digit(to_base_2(int(a)))).split('.')
    a_16 = ''.join([to_base_16(i) for i in a_2])
    b_16 = calculatori('10', '16', b)
    do_znaka = 0
    for i in b_16.split('.')[1]:
        if i != '0':
            break
        do_znaka += 1
    b_16_upd = b_16[4::]
    predst_b = ""
    count = 0
    for i in b_16_upd:
        count += 1
        predst_b += normalize_digit(calculatori('16', '2', i))
        if count == 6:
            break
    answer += f'\nA = {a} (10) = {a_16} (16) = {zn},{a_16} (16) * 16 ^ {len(a) - 1}'
    answer += f'\nПорядок (P) = {len(a) - 1}, Мантисса = {zn},{a_16}\nХарактеристика числа A: X = P + 64 = ' \
              f'{64 + len(a) - 1} (10) = {to_base_2(64 + len(a) - 1)} (2)\n{zn}.{to_base_2(64 + len(a) - 1)}.' \
              f'{add_point_by_four("".join(a_2) + "0" * (24 - len("".join(a_2))))}\n'
    answer += f'B = {b} (10) = {b_16} (16) = {zn_b},{b_16_upd} (16) * 16 ^ {-do_znaka}'
    answer += f'\nПорядок (P) = {-do_znaka}, Мантисса = {zn_b},{b_16_upd}\nХарактеристика числа A: X = P + 64 = '
    answer += f'{64 + -do_znaka} (10) = 0{to_base_2(64 + -do_znaka)} (2)\n{zn_b}.0{to_base_2(64 + -do_znaka)}.'
    answer += f'{add_point_by_four(predst_b + "0" * (24 - len(predst_b)))}\n'
    return answer


def task_four(a, b):
    zn_A = '0'
    zn_B = '0'
    a_2 = to_base_2(int(a))
    a_mnt = a_2
    while a_mnt[-1] == '0':
        a_mnt = a_mnt[:-1]
    while a_mnt[0] == '0':
        a_mnt = a_mnt[1::]
    answer = '4. Заданные числа A и B представить в форме с плавающей запятой в формате Ф2.'
    answer += f'\nA = {a} (10) = {add_point_by_four(a_2)} (2) = {zn_A},{a_mnt} (2) * 2 ^ {len(a_2)}'
    answer += f'\nПорядок (P) = {len(a_2)}, Мантисса = {zn_A},{a_mnt}\nХарактеристика числа A: X = P + 128 = ' \
              f'{128 + len(a_2)} (10) = {to_base_2(128 + len(a_2))} (2)\n{zn_A}.{to_base_2(128 + len(a_2))}.' \
              f'{add_point_by_four(a_2[1::] + "0" * (24 - len(a_2[1::])))}\n'
    b_16 = calculatori("10", "16", b)[:10]
    b_2 = ''
    for i in b_16[2::]:
        b_2 += normalize_digit(calculatori("16", "2", i))
    b_mnt = b_2
    while b_mnt[-1] == '0':
        b_mnt = b_mnt[:-1]
    while b_mnt[0] == '0':
        b_mnt = b_mnt[1::]
    answer += f'\nB = {b} (10) = {b_16} (16) = {add_point_by_four(b_2)} (2) = {zn_B},{b_mnt} (2) * 2 ^ -{len(b_16) - 2}'
    answer += f'\nПорядок (P) = -{len(b_16) - 2}, Мантисса = {zn_B},{b_mnt}\nХарактеристика числа A: X = P + 128 = ' \
              f'{128 + -(len(b_16) - 2)} (10) = {normalize_digit(to_base_2(128 + -(len(b_16) - 2)))} (2)\n{zn_B}.{normalize_digit(to_base_2(128 + -(len(b_16) - 2)))}.' \
              f'{add_point_by_four(b_mnt[1:] + "0")}\n'
    return answer


A = "1600"
B = "0.03"
R = "41C0D300"
S = "BEA80000"
print(6.025756835937510 * 4)
exit(0)
for i in R:
    print(normalize_digit(calculator("16", "2", i)), end='.')


"""
A = 1600 (10) = 640 (16) = 11001000000 (2) = 1,1001 ^ 5
X = P + 127 = 132 = 10000100
0.10000100.110.0100.0000.0000.0000.0000
B = 0.03 (10) = 0.07AE147A (16) = 0,0000.0111.1010.1110.0001.0100.0111.1010 (2) = 1,1110101110000101000111101 * 2 ^ -9
X = P + 127 = 118 = 01110110 (2)
0.01110110.1110.1011.1000.0101.0001.1110

"""


# print(task_three(A, B))

#print(task_one(A))
#print(task_two(A))
#print(task_three(A, B))
#print(task_four(A, B))
