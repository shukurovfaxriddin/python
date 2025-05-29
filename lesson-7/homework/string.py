# 1

def is_prime(n):
    nums = []
    if n < 2:
        return f'{n}\nNatija:\nFalse\n(Izoh: {n} soni tub emas.)'
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            nums.append(str(i))
    if len(nums) > 0:
        return f'{n}\nNatija:\nFalse\n(Izoh: {n} soni tub emas, chunki u {','.join(nums)} ga bo\'linadi.)'
            
    else:
        return f'{n}\nNatija:\nTrue\n(Izoh: {n} soni faqat 1 va o\'ziga bo\'linadi, ya\'ni tub son.)'


print(is_prime(5000)) 


# 2
def digit_sum(n):
    return sum(int(ch) for ch in str(n))

def digit_sum(n):
    return sum(map(int, str(n)))

print(digit_sum(1115))

#3
def daraja(n):
    k = 1
    while 2 ** k <= n:
        print(2 ** k, end=' ')
        k += 1

daraja(200)
