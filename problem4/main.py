def muncul_sekali(angka):
    count_dict = {}
    for digit in angka:
        if digit in count_dict:
            count_dict[digit] += 1
        else:
            count_dict[digit] = 1
    unique_digits = [int(digit) for digit, count in count_dict.items() if count == 1]

    return unique_digits

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]