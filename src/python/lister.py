import os
import json

#Builds a feature list for e.g. https://www.jasondavies.com/wordcloud/

DATA_FOLDER = "../../data"
OUTPUT_FILE = DATA_FOLDER + "/../featurelist.txt"


def main():
    print("Finding feature occurrences")
    words = build_list_of_words()
    words.sort()
    output_file = open(OUTPUT_FILE, "w")
    print ("Writing words to: " + output_file.name)
    for word in words:
        output_file.write(word)
    shutdown(output_file)


def shutdown(output_file):
    output_file.flush()
    output_file.close()
    print("We're done here.")

def build_list_of_words():
    words = []
    for dirname, dirnames, filenames in os.walk(DATA_FOLDER):
        #print("Processing files in: " + dirname)
        for filename in filenames:
            # print(filename)
            content = readfile(dirname, filename)
            obj = parseJSON(content, filename)
            if obj is not None:
                # print (obj)
                for label in obj:
                    #print(label["name"])
                    words.append(label["name"] + "\n")
    return words


def parseJSON(content, filename):
    try:
        json_obj = json.loads(content)
    except:
        print("ERROR: " + filename + " is not a happy json file")
    else:
        return json_obj["labels"]


def readfile(dirname, filename):
    file = open(os.path.join(dirname, filename), "r")
    content = file.read()
    file.close()
    return content


if __name__ == "__main__":
    main()


