# Example Program 1
# This program will allow the user to compute simple and compound
# interest


def findSimpleInterest(principal: int, numYears: int, rate: float) -> float:
    # computes the simple interest rate given principal, time in years, and
    # current rate
    interest = principal * (1 * (rate * numYears))
    return interest


def findCompoundInterest(p: int, y: int, r: float) -> float:
    # computes compound interest given principal, time in years, and rate
    # interest is compounded once annually
    interest = p * ((1 + r) ** y)
    return interest


def main() -> None:
    principal = int(input("What is the principal? "))
    numYears = int(input("What is the number of years? "))
    rate = float(input("What is the rate? (in decimal) "))
    type = input("What is the type of investment (simple or compound)? ")

    if type == 'c':
        answer = findCompoundInterest(principal, numYears, rate)
        print("Compound interest: ", answer)
    elif type == 's':
        answer = findSimpleInterest(principal, numYears, rate)
        print("Simple interest: ", answer)
    else:
        print("Unknown command!")


if __name__ == "__main__":
    main()

