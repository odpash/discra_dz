from calculate import calculator, plus, change_zn, znak_2_base, normalize_digit, invertor


def question_four_1(a, b, a_inverted_2, b_inverted_2, correction_fl, changes_fl):
    print(f"A: {a}; [-A]: {a_inverted_2}\nB: {b}; [-B]: {b_inverted_2}")
    schp = '00000000'
    print(f'#{0}, СЧП: {schp}, Множитель: {b}')
    b = a[-1] + b[:-1]
    schp = a[0] + a[:-1]
    print(f'#{1}, СЧП: {schp}, Множитель: {b}')
    for i in range(2, 9):
        prev_operation = b[-1]
        if prev_operation == '1':
            schp, _, _ = plus(schp, a)
        b = schp[-1] + b[:-1]
        schp = a[0] + schp[:-1]
        print(f'#{i}, СЧП: {schp}, Множитель: {b}')
    if correction_fl:
        dop_a = change_zn(a[0]) + a_inverted_2[1::]
        schp, _, _ = plus(schp, dop_a)
        print(f'#{9}, СЧП: {schp}, Множитель: {b}')
    print('\n')


def q_2_plus(schp, a):
    res, _, _ = plus(schp, a)
    return res, a[0]


def q_2_minus(schp, a_inverted):
    res, _, _ = plus(schp, a_inverted)
    return res, a_inverted[0]


def question_four_2(a, b, a_inverted, b_inverted, zn):
    if zn == '<':
        a_inverted = change_zn(a_inverted[0]) + a_inverted[1::]
    print(f"A: {a}; [-A]: {a_inverted}\nB: {b}; [-B]: {b_inverted}")

    schp = '00000000'
    print(f'#{0}, СЧП: {schp}, Множитель: {b}')
    if b[-1] == '1':
        schp, zn = q_2_minus(schp, a_inverted)
    else:
        schp, zn = q_2_plus(schp, a)
    last_mnsh = b[-1]
    b = a[-1] + b[:-1]
    schp = zn + schp[:-1]
    print(f'#{1}, СЧП: {schp}, Множитель: {b}')
    pre_last_mnsh = b[-1]

    for i in range(2, 9):
        if pre_last_mnsh == '1' and last_mnsh == '0':
            schp, zn = q_2_minus(schp, a_inverted)
        elif pre_last_mnsh == '0' and last_mnsh == '1':
            schp, zn = q_2_plus(schp, a)
        b = schp[-1] + b[:-1]
        schp = zn + schp[:-1]
        last_mnsh = pre_last_mnsh
        pre_last_mnsh = b[-1]
        print(f'#{i}, СЧП: {schp}, Множитель: {b}')
    if schp[0] == '1':
        inverted = invertor(schp + b)
        inverted, _, _ = plus(inverted, (len(inverted) - 1) * '0' + '1')
        print(f'RES: -{calculator("2", "10", inverted)}')
    else:
        print(f'RES: {calculator("2", "10", schp + b)}')
    print('\n\n')

def question_four(a, b):  # Умножение
    zn_rev_a, zn_rev_b = '0', '0'
    if a >= 0:
        zn_rev_a = '1'
    if b >= 0:
        zn_rev_b = '1'
    a, b = abs(a), abs(b)
    a_2, b_2 = normalize_digit(calculator("10", "2", str(a))), normalize_digit(calculator("10", "2", str(b)))
    znaks = [[">", ">"], [">", "<"], ["<", ">"], ["<", "<"]]
    a_inverted_2 = invertor(a_2)
    b_inverted_2 = invertor(b_2)
    a_inverted_2, _, _ = plus(a_inverted_2, (len(a_inverted_2) - 1) * '0' + '1')
    b_inverted_2, _, _ = plus(b_inverted_2, (len(b_inverted_2) - 1) * '0' + '1')
    a_inverted_2, b_inverted_2 = zn_rev_a + normalize_digit(a_inverted_2), zn_rev_b + normalize_digit(b_inverted_2)
    a_b_mas = [["0" + a_2, "0" + b_2, a_inverted_2, b_inverted_2, False],
               ["0" + a_2, "1" + b_2, a_inverted_2, b_inverted_2, False],
               ["1" + a_2, "0" + b_2, a_inverted_2, b_inverted_2, False],
               ["1" + a_2, "1" + b_2, a_inverted_2, b_inverted_2, False]]

    for i in range(len(a_b_mas)):
        part_9, changes_fl = False, False
        if a_b_mas[i][0][0] == '1':
            changes_fl = True
            a_b_mas[i][0], a_b_mas[i][2] = a_b_mas[i][2], a_b_mas[i][0]
        if a_b_mas[i][1][0] == '1':
            part_9 = True
            a_b_mas[i][1], a_b_mas[i][3] = a_b_mas[i][3], a_b_mas[i][1]
        print(f"A {znaks[i][0]} 0, B {znaks[i][1]} 0")
        question_four_1(a_b_mas[i][0], a_b_mas[i][1], a_b_mas[i][2], a_b_mas[i][3], part_9, changes_fl)
        question_four_2(a_b_mas[i][0], a_b_mas[i][1], a_b_mas[i][2], a_b_mas[i][3], znaks[i][0])


print(question_four(102, 19))
