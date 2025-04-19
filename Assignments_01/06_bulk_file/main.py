import os

def main():
    i = 0
    path = "E:/eg-image/"
    for fileName in os.listdir(path):
        my_dest = "image-" + str(i) + ".jpg"
        my_source = path + fileName  # The file name
        my_dest = path + my_dest  # Destination file name
        os.rename(my_source, my_dest)  # Rename the file
        i += 1 
        

if __name__ == '__main__':
    main()