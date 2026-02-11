# 1
txt = open("postcard.txt", "r").read()
print("*** 1. Full Text ***\n" + txt + '\n')

# 2 tuple : List와 유사 (수정,변경,삽입,삭제시 List변환후 튜플로 변환)
head, body, tail = tuple(txt.split('\n\n'))
print("*** 2. Body ***\n" + body + '\n')

# 3
import re
s = re.sub('[:,\.]', '', body)
print("*** 3. Text without Punctuation ***\n" + s + '\n')
"""
# re.sub(pattern, repl, string):
pattern: 찾고자 하는 정규 표현식 패턴. 여기서는 [:,\.]
repl: 패턴이 일치하는 부분을 대체할 문자열. 여기서는 빈 문자열 ''로 설정.
string: 대체 작업을 수행할 원본 문자열. 여기서는 body.
"""

# 4
s = s.upper()
print("*** 4. Uppercase ***\n" + s + '\n')

# 5
secret_words = []
for line in s.split('\n'):              # Line 기준으로 Split
    secret_words += line.split()[:2]    # 각 라인 ' ' 기준 Split + Index 0,1([:2]) 로 조합

"""
# 튜플의 슬라이싱 : 튜플명[start:end:step] 형식. start는 시작 인덱스, end는 끝 인덱스, step은 슬라이싱 간격
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[1:3]) # (2, 3)
print(tuple1[:3]) # (1, 2, 3)
print(tuple1[1:]) # (2, 3, 4, 5)
print(tuple1[::-1]) # (5, 4, 3, 2, 1)
"""

message = ' '.join(secret_words)
print("*** 5. Secret Message ***\n" + message)