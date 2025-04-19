def main():
    #Get the temperature in Fahrenheit from user
    fahrenheit = input("\033[1;3mEnter temperature in Fahrenheit:\033[0m")
    fahrenheit = float(fahrenheit)

    #Convert the temperature to Celsius
    celsius = (fahrenheit - 32) * 5/9
    print("\nThe temperature in Celsius is:", celsius)
if __name__ == '__main__':
    main()