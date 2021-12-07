import requests


def calculator(from_base, to_base, chislo):
    from_base = from_base.replace('10', '4').replace('2', '1').replace('16', '5')
    to_base = to_base.replace('10', '4').replace('2', '1').replace('16', '5')

    data = {'raschet': '1',
            'chislo1': chislo,
            'ss': from_base,
            'triada_tetrada': '0',
            'ssdrugaya': '4',
            'ss1': to_base,
            'ss1drugaya': '4'}
    r = requests.post('https://calculatori.ru/perevod-chisel.html', data=data)
    return r.text.split('<FONT color="#ff0000" size="6">')[1].split('</')[0]


def znak_2_base(d: str):
    if float(d) >= 0:
        return '0'
    else:
        return '1'


def invertor(base_2: str):
    ans = ''
    for i in range(len(base_2)):
        if i == 0:
            ans += base_2[i]
            continue
        if base_2[i] == '1':
            ans += '0'
        else:
            ans += '1'
    return ans


def plus(a, b):
    a, b = a[::-1], b[::-1]
    zalog = 0
    answer = ''
    AF = "0"
    for i in range(len(a)):
        sum1 = int(a[i]) + int(b[i]) + zalog
        answer += str(sum1 % 2)
        if sum1 // 2 != 0:
            zalog = 1
        else:
            zalog = 0
        if i == 3 and zalog == 1:
            AF = "1"
    if zalog == 1:
        return answer[::-1], "1", AF
    return answer[::-1], "0", AF


def normalize_digit(a):
    return '0' * ((3 - (len(a) % 4)) % 4) + a
