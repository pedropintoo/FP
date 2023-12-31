import math

def floatInput(prompt,min=-math.inf,max=math.inf):
    res = float(input(prompt))
    assert min<max,f"ERROR: {min} should be lower than {max}"
    assert min<=res<=max, f"ERROR: Value should be in [{min},{max}]"
    return res


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    while True:
        try:
            v = floatInput("Value? ",)
        except ValueError:
            print("ERROR: Not a float")
        else:
            break
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    while True:
        try:
            h = floatInput("Humidity (%)? ", 0, 100)
        except ValueError:
            print("ERROR: Not a float")
        except AssertionError:
            pass
        else:
            break
            

    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    # d) What happens if you uncomment this?
    # impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    main()
