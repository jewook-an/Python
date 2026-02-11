# 윤년 판단 함수
def is_leap_year(year):
    if year % 4 != 0:       #연도가 4로 나누어 떨어지지 않으면 윤년 XX
        return False
    elif year % 100 != 0:   #연도가 100으로 나누어 떨어지지 않으면 윤년 OO
        return True
    elif year % 400 != 0:   #연도가 400으로 나누어 떨어지지 않으면 윤년 XX
        return False
    else:
        return True
