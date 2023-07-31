def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2**i
    return num


if __name__ == '__main__':
    print(bin_to_decimal('100'))
    print(bin_to_decimal('101'))
    print(bin_to_decimal('1001'))
