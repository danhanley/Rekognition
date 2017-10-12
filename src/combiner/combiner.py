import os
import json

DATA_FOLDER = "../../data"

def main():
    print "Establishing dimensionality of this universe"
    for dirname, dirnames, filenames in os.walk(DATA_FOLDER):
        print "Processing files in: " + dirname
        for filename in filenames:
            print(filename)
            content = readfile(dirname, filename)
            obj = parseJSON(content, filename)
            if obj is not None:
                print obj



def parseJSON(content, filename):
    try:
        json_obj = json.loads(content)
    except:
        print "ERROR: " + filename + " is not a happy json file"
    else:
        return json_obj["labels"]


def readfile(dirname, filename):
    file = open(os.path.join(dirname, filename), "r")
    content = file.read()
    file.close()
    return content


if __name__== "__main__":
    main()

print "Guru99"