def palindrome(s):  # 좌우 대칭
    s = s.lower()
    s = s.replace(' ', '')
    return s[:] == s[::-1]

if __name__ == '__main__':
    for x in ['anna', 'banana', 'Anna', 'My gym', 'teet', 'test']:
        if palindrome(x):
            print(f"'{x}' is a palindrome")
        else:
            print(f"'{x}' is not a palindrome")
