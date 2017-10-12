import os

DATA_FOLDER = "../../data"

def main():
    print "Hello World!!"
    for dirname, dirnames, filenames in os.walk(DATA_FOLDER):
        print dirname
        for filename in filenames:
            print(os.path.join(dirname, filename))

if __name__== "__main__":
    main()

print "Guru99"