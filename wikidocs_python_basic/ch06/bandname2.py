from random import choice

"""
cp949 인코딩이 파일의 내용을 제대로 해석 안되 Error > 인코딩 설정 필요
color = open('color.txt').read().split()
food = open('food.txt').read().split()
"""

color = open('ch06/color.txt', encoding='utf-8').read().split()
food = open('ch06/food.txt', encoding='utf-8').read().split()

print(choice(color) + ' ' + choice(food))

