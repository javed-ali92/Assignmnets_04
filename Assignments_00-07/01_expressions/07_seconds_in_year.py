DAYS_IN_YEAR= 365
HOURS_IN_ONE_DAY =24
MIN_PER_HOUR =60
SECONDS_IN_MIN =60

# Calulatte the number of second in a years

def main():
        
    total_seconds = DAYS_IN_YEAR * HOURS_IN_ONE_DAY * MIN_PER_HOUR * SECONDS_IN_MIN
    print(f"Total seconds in a years is: {total_seconds}")

if __name__ == '__main__':
    main()