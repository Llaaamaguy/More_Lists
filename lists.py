def sum_of_odd_nums(n):
    n = n * 2
    numbers = [i for i in range(1,n) if i%2 == 1]
    return sum(numbers)

def caesar_cipher(message, key):
    ciphernumbers = [ord(i)+key for i in message]
    decoded = bytes(ciphernumbers).decode("ascii")
    return decoded

def fbhelper(n):
    if n%3 == 0 and n%5 == 0:
        return "fizzbuzz"
    elif n%3 == 0:
        return "fizz"
    elif n%5 == 0:
        return "buzz"
    else:
        return n


def fizzbuzz(n):
    numlist = [fbhelper(i) for i in range(1,n)]
    return numlist

def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(1,11):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "Frpsxwhu#Vflhqfh#lv#qr#pruh#derxw#frpsxwhuv#wkdq#dvwurqrp|#lv#derxw#whohvfrshv1"
    print(caesar_cipher(ciphertext, -3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()