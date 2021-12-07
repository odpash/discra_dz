import json
from calculate import calculator, znak_2_base, invertor, plus, normalize_digit, change_zn


materials = json.loads(open('materials.json', 'r', encoding="UTF-8").read())


def question_one():  # flag principle
    return materials['q1']


def question_two(a, b):   # сложение
    CF, SF, ZF, AF, PF, OF = '', '', '0', '', '', '1'
    comments = {"a": {'znak': ''}, "b": {"znak": ''}, 'bzn': ''}
    a_2, b_2 = calculator('10', '2', str(a)), calculator('10', '2', str(b))
    zn_a, zn_b = znak_2_base(a_2), znak_2_base(b_2)
    a_2 = a_2.replace('-', '')
    b_2 = b_2.replace('-', '')
    a_2 = zn_a + normalize_digit(a_2)
    b_2 = zn_b + normalize_digit(b_2)
    a_inverted_2 = invertor(a_2)
    b_inverted_2 = invertor(b_2)
    a_inverted_2, _, _ = plus(a_inverted_2, (len(a_inverted_2) - 1) * '0' + '1')
    b_inverted_2, _, _ = plus(b_inverted_2, (len(b_inverted_2) - 1) * '0' + '1')
    if zn_a == '1':
        a_sch = a_inverted_2
        comments['a']['znak'] = "Так как знак равен 1, то используется дополнительный код числа A."
    else:
        comments['a']['znak'] = "Так как знак равен 0, то используется число A."
        a_sch = a_2
    if zn_b == '1':
        b_sch = b_inverted_2
        comments['b']['znak'] = "Так как знак равен 1, то используется дополнительный код числа B."
    else:
        b_sch = b_2
        comments['b']['znak'] = "Так как знак равен 0, то используется число B."
    a_bz, b_bz = int(calculator("2", "10", a_sch)), int(calculator("2", "10", b_sch))
    rez_bz = a_bz + b_bz
    if rez_bz > 256:
        rez_bz = str(rez_bz % 256) + " ?"
        comments['bzn'] = "\nДля БзИ результат неверен вследствие возникающего переноса из старшего разряда."
    rez, CF, AF = plus(a_sch, b_sch)
    if rez.count('1') % 2 == 0:
        PF = '1'
    else:
        PF = '0'
    if (int(a) + int(b)) >= 0 and rez[0] == '0' or (int(a) + int(b) < 0 and rez[0] == '1'):
        OF = '0'
    SF = rez[0]
    a_2 = a_2[:1] + '|' + a_2[1::]
    b_2 = b_2[:1] + '|' + b_2[1::]
    a_sch = a_sch[:1] + '|' + ' '.join(a_sch[1::])
    b_sch = b_sch[:1] + '|' + ' '.join(b_sch[1::])
    rez = rez[:1] + '|' + ' '.join(rez[1::])
    a_inverted_2 = a_inverted_2[:1] + '|' + a_inverted_2[1::]
    b_inverted_2 = b_inverted_2[:1] + '|' + b_inverted_2[1::]
    answer = f"A (10): {a}\nB (10): {b}\n"
    answer += f"A: {a_2}; [-A]: {a_inverted_2}\n"
    answer += f"B: {b_2}; [-B]: {b_inverted_2}\nКомментарии:\n{comments['a']['znak']}\n{comments['b']['znak']}\nРезультат вычислений:\n{a_sch}\n{b_sch}\n{'-' * 2 * len(rez)}\n{rez}"
    answer += f"\nЗнаковая интерпретация: {a} + {b} = {a + b}\nБеззнаковая интерпретация: {a_bz} + {b_bz} = {rez_bz}{comments['bzn']}\n"
    answer += f'CF: {CF}, SF: {SF}, ZF: {ZF}, AF: {AF}, PF: {PF}, OF: {OF}\n'
    return answer


def question_three():
    pass


def question_five_1(a, b, a_2, b_2, a_inverted_2, b_inverted_2, mnsh, zn_a, zn_b, from_mnsh, from_mnsh_2):
    answer = f"A: {a_2}; [-A]: {a_inverted_2}\n"
    answer += f"B: {b_2}; [-B]: {b_inverted_2}\n"
    schp = '00000000'
    answer += f'\n#{0}, SCHP: {schp}, MNSH: {mnsh}'
    schp = mnsh
    mnsh = schp[-1] + mnsh[:-1]
    schp = zn_a + from_mnsh[:-1]

    answer += f'\n#{1}, SCHP: {schp}, MNSH: {mnsh}'
    for i in range(2, 9):
        prev_operation = mnsh[-1]
        if prev_operation == '1':
            schp, _, _ = plus(schp, from_mnsh)
        mnsh = schp[-1] + mnsh[:-1]
        schp = zn_a + schp[:-1]
        answer += f'\n#{i}, SCHP: {schp}, MNSH: {mnsh}'
    if zn_b == '1':
        if zn_a == "0":
            from_mnsh_2 = '1' + from_mnsh_2[1::]
        else:
            from_mnsh_2 = '0' + from_mnsh_2[1::]
        schp, _, _ = plus(schp, from_mnsh_2)
        answer += f'\n#{9}, SCHP: {schp}, MNSH: {mnsh}'
    res = schp + mnsh
    res_10 = calculator('10', '2', str(abs(a) * abs(b)))
    point = len(res) - len(res_10) - 1
    answer += f'\n{res} (2) = {a * b} (10)'
    return answer


def question_five_2(a, b, a_2, b_2, a_inverted_2, b_inverted_2, mnsh, zn_a, zn_b, from_mnsh, from_mnsh_2, mnsh_2):
    if zn_a == '0':
        from_mnsh_2 = '1' + from_mnsh_2[1::]

    answer = f"A: {a_2}; [-A]: {a_inverted_2}\n"
    answer += f"B: {b_2}; [-B]: {b_inverted_2}\n"
    schp = '00000000'
    answer += f'\n#{0}, SCHP: {schp}, MNSH: {mnsh}'
    time_a_zn = zn_a
    print(mnsh)
    if mnsh[-1] == '0':
        if zn_a == '1':
            schp = '0' + from_mnsh[1::]
        else:
            schp = from_mnsh
    else:
        if zn_a == '1':
            schp = '0' + from_mnsh_2[1::]
        else:
            schp = from_mnsh_2
        time_a_zn = change_zn(time_a_zn)
    print(schp)
    prev_prev_act = mnsh[-1]
    mnsh = schp[-1] + mnsh[:-1]
    schp = time_a_zn + schp[:-1]
    prev_operation = prev_prev_act
    answer += f'\n#{1}, SCHP: {schp}, MNSH: {mnsh}, {prev_prev_act} -> {prev_operation}'
    for i in range(2, 9):
        if zn_a == '0' and zn_b == '1' or zn_a == '1' and zn_b == '0' or zn_a == "1" and zn_b == "1":
            time_a_zn = change_zn(zn_a)
        else:
            time_a_zn = zn_a
        prev_operation = mnsh[-1]
        if prev_prev_act == '1' and prev_operation == '0':
            schp, _, _ = plus(schp, from_mnsh)
            if zn_a == '0' and zn_b == '1' or zn_a == '1' and zn_b == '0':
                time_a_zn = change_zn(time_a_zn)
        elif prev_prev_act == '0' and prev_operation == '1':
            schp, _, _ = plus(schp, from_mnsh_2)
            time_a_zn = change_zn(zn_a)
        mnsh = schp[-1] + mnsh[:-1]
        schp = time_a_zn + schp[:-1]
        answer += f'\n#{i}, SCHP: {schp}, MNSH: {mnsh}, {prev_prev_act} -> {prev_operation}'
        prev_prev_act = prev_operation
    res = schp + mnsh
    res_10 = calculator('10', '2', str(abs(a) * abs(b)))
    point = len(res) - len(res_10) - 1
    answer += f'\n{res} (2) = {a * b} (10) = {calculator("10", "2", str(a * b))} (10)'
    return answer


def question_five(a, b):  # Умножение
    a_2, b_2 = calculator('10', '2', str(a)), calculator('10', '2', str(b))
    zn_a, zn_b = znak_2_base(a_2), znak_2_base(b_2)
    a_2 = a_2.replace('-', '')
    b_2 = b_2.replace('-', '')
    a_2 = zn_a + normalize_digit(a_2)
    b_2 = zn_b + normalize_digit(b_2)
    a_inverted_2 = invertor(a_2)
    b_inverted_2 = invertor(b_2)
    a_inverted_2, _, _ = plus(a_inverted_2, (len(a_inverted_2) - 1) * '0' + '1')
    b_inverted_2, _, _ = plus(b_inverted_2, (len(b_inverted_2) - 1) * '0' + '1')

    if zn_b == '0':
        mnsh = b_2
        mnsh_2 = b_inverted_2
    else:
        mnsh = b_inverted_2
        mnsh_2 = b_2
    if zn_a == '0':
        from_mnsh = a_2
        from_mnsh_2 = a_inverted_2
    else:
        from_mnsh = a_inverted_2
        from_mnsh_2 = a_2

    res = question_five_2(a, b, a_2, b_2, a_inverted_2, b_inverted_2, mnsh, zn_a, zn_b, from_mnsh, from_mnsh_2, mnsh_2)
    return res
print(question_five(113, -41))