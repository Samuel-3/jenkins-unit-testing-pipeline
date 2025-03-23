class Functions:
    def multiply_by_two(input):
        return input * 2
    
    def half(input):
        return input / 2


def main():
    functions  = Functions
    print(functions.multiple_by_two(10))
    print(functions.half(10))

if __name__ == "__main__":
    main()
