def giaithua(n):
    if n == 0:
        return 1
    else:
        return (n * giaithua(n-1))

# print(giaithua(3))

def tohop(k,n):
    if n < k:
        return print("Lỗi nhập lại")
    else:
        return (giaithua(n) / (giaithua(k)*giaithua(n-k)))

# print(int(tohop(8,10)))

def hienthi(n):
    for i in range(n):
        for e in range(10 - i - 1):
            print("    ", end='')
        for j in range(i + 1):
            print(int(tohop(j, i)), "     ", end=' ')
        print("")
        i = i + 1


hienthi(10)