def calculate_sum(a, b, c):
    result = a + b + c
    return result

def main():
    v = 3
    x = 5
    y = 10
    z = calculate_sum(x,y,v)

    numbers = [1,2,3,4,5,6]
    numbers_squared = [n**2 for n in numbers]

    print("xとyの合計:", z)
    print("二乗した数列:", numbers_squared)

if __name__ == '__main__':

    main()
