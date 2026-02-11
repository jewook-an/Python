def korean_number(num):
    digits = {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    d, m = divmod(num, 10)  # divmod(a, b)는 2개의 숫자 a, b를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴한다.
    if 0 <= num < 10:
        return digits[m]
    elif num == 10:
        return '십'
    elif 10 < num < 20:
        return '십' + digits[m]
    elif 20 <= num < 100:
        _digits_copy = digits.copy()
        _digits_copy[0] = ''
        return digits[d] + '십' + _digits_copy[m]
    else:
        return '백'

