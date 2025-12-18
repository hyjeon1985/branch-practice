def fizzbuzz(start: int=1, end: int=15):
    for i in range(start, end + 1):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()
