def in_range(n, low, high):
    if n >= low and n <= high:
	    return True
    
    return False

def main():
    print(in_range(2,1,5))
    print(in_range(5,1,5))
    print(in_range(4,7,10))

if __name__ == '__main__':
    main()