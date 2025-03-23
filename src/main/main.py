class Functions:
    def multiple_by_two(input):
        return input * 2
    
    def half(input):
        return input / 2


def main():
    print("testing Functions class works")

    functions  = Functions

    multiple = functions.multiple_by_two(5)

    print(multiple)

if __name__ == "__main__":
    main()
