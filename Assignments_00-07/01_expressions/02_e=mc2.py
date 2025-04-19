def main():
    E = float(input("\033[1;3mEnter Kilos of mass:\033[0m"))
    C = 299792458
    Mass = E * C**2

    print(f"e = m * C^2...")
    print(f"m = {E} kg")
    print(f"c = {C} m/s")
    print(f"E = {Mass} Joules")

if __name__ == '__main__':
    main()