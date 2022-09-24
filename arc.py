maior_ate_agora = -1
n = int(input())
print('antes', maior_ate_agora)
while n > 0:
    n = n - 1
    num = int(input())
    if num > maior_ate_agora:
        maior_ate_agora = num
    print('ate agora:', maior_ate_agora)

print ('depois', maior_ate_agora)