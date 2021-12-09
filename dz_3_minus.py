import calculate

 # NOT WORKED AT DIGITS 77 and 51
def minus(a, b, a_c, b_c):
    incorrect_result = False
    CF, SF, ZF, AF, PF, OF = '0', '0', '0', '0', '0', '0'
    print("A:", a)
    print("B:", b)
    a = a[::-1]
    b = b[::-1]
    result = ""
    zaem = 0
    for i in range(len(a)):
        raz = int(a[i]) - int(b[i]) - zaem
        if raz >= 0:
            result += str(raz)
            zaem = 0
        else:
            if raz == -1:
                result += '1'
            if raz == -2:
                result += '0'
            zaem = 1
        if i == 3 and zaem == 1:
            AF = "1"
    if zaem == 1:
        CF = '1'
        incorrect_result = True
    result = result[::-1]
    print("  ", result)
    if result.count('1') % 2 == 0:
        PF = '1'
    SF = result[0]
    if a[-1] == '1':  # a - negative
        result = result[0] + calculate.invertor(calculate.normalize_digit(calculate.calculator('10', '2', int(calculate.calculator("2", '10', result[1::])) - 1)))
        print("  ", result)
    if len(result[1::]) * '0' == result[1::]:
        result_10 = 0
    else:
        result_10 = int(calculate.calculator('2', '10', result[1::]))
    if result[0] == '1':
        result_10 = -result_10
    a, b = a[::-1], b[::-1]
    a, b = calculate.calculator('2', '10', a), calculate.calculator('2', '10', b)
    if result_10 != a_c - b_c:
        print("ЗИ: Результат неправильный! Взятие из знакового разряда! Должно быть:")
        OF = '1'
    print(f"Знаковая интерпритация: {a_c} - {b_c} = {result_10}")
    if incorrect_result:
        print("БЗИ: Результат неправильный! Взятие из разряда за пределами формата! Должно быть:")
    print(f"Беззнаковая интерпритация: {a} - {b} = {int(a) - int(b)}")
    print(f'CF: {CF}, SF: {SF}, ZF: {ZF}, AF: {AF}, PF: {PF}, OF: {OF}')




def main(a, b):
    zn_rev_a, zn_rev_b = '0', '0'
    if a >= 0: zn_rev_a = '1'
    if b >= 0: zn_rev_b = '1'
    a, b = abs(a), abs(b)
    a_2, b_2 = calculate.normalize_digit(calculate.calculator("10", "2", str(a))), calculate.normalize_digit(calculate.calculator("10", "2", str(b)))
    a_b_mas = [["0" + a_2, "0" + b_2, a, b], ["0" + a_2, "1" + b_2, a, -b], ["1" + a_2, "0" + b_2, -a, b], ["1" + a_2, "1" + b_2, -a, -b]]
    znaks = [[">", ">"], [">", "<"], ["<", ">"], ["<", "<"]]
    a_inverted_2 = calculate.invertor(a_2)
    b_inverted_2 = calculate.invertor(b_2)
    a_inverted_2, _, _ = calculate.plus(a_inverted_2, (len(a_inverted_2) - 1) * '0' + '1')
    b_inverted_2, _, _ = calculate.plus(b_inverted_2, (len(b_inverted_2) - 1) * '0' + '1')
    a_inverted_2, b_inverted_2 = zn_rev_a + calculate.normalize_digit(a_inverted_2), zn_rev_b + calculate.normalize_digit(b_inverted_2)
    print(f"A (доп.) = {a_inverted_2}, B (доп.) = {b_inverted_2}")
    for i in range(len(a_b_mas)):
        print(f"A {znaks[i][0]} 0, B {znaks[i][1]} 0")
        if a_b_mas[i][0][0] == '1':  # a - negative
            a_b_mas[i][0] = a_inverted_2
        if a_b_mas[i][1][0] == '1':  # b - negative
            a_b_mas[i][1] = b_inverted_2
        minus(a_b_mas[i][0], a_b_mas[i][1], a_b_mas[i][2], a_b_mas[i][3])
        print("\n\n")

main(102, 19)