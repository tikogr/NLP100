def cipher(s):
    r = ''

    for c in s:
        if c.islower():
            r += chr(219-ord(c))
        else:
            r += c

    return r

s = input()

# 暗号化
r1 = cipher(s)
print('暗号化：' + r1)

# 復号化
r2 = cipher(r1)
print('復号化：' + r2)
