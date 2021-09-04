n = int(input('Введите число:'))
i = 1
print(n, end='    ')
while i ** 2 <= n:
    print(i ** 2, end=' ')
    i += 1
