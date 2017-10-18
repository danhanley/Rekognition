import os
import json

DATA_FOLDER = "../../data"
OUTPUT_FILE = DATA_FOLDER + "/../universe.csv"


def main():
    print("Establishing dimensionality of this universe")
    universe_of_labels = calculate_dimensionality()
    print("There are " + str(len(universe_of_labels)) + " dimensions in this universe.")
    #print(universe_of_labels)
    output_file = open(OUTPUT_FILE, "w")
    print ("Writing universe to: " + output_file.name)
    write_header(output_file, universe_of_labels)
    build_universe(output_file, universe_of_labels)
    shutdown(output_file)


def shutdown(output_file):
    output_file.flush()
    output_file.close()
    print("We're done here.")


def write_header(output_file, universe_of_labels):
    output_file.write("File Name")
    for universal_label in universe_of_labels:
        output_file.write("," + universal_label)
    output_file.write("\n")




def build_universe(output_file, universe_of_labels):
    #TODO extract directory walk to partial function
    for dirname, dirnames, filenames in os.walk(DATA_FOLDER):
        #print("Processing files in: " + dirname)
        for filename in filenames:
            # print(filename)
            content = readfile(dirname, filename)
            obj = parseJSON(content, filename)
            if obj is not None:
                output_file.write(filename)
                for universal_label in universe_of_labels:
                    val = 0
                    for object_label in obj:
                        if object_label["name"] == universal_label:
                            val = object_label["confidence"]
                    output_file.write("," + str(val))
                output_file.write("\n")


def calculate_dimensionality():
    universe_of_labels = set()
    for dirname, dirnames, filenames in os.walk(DATA_FOLDER):
        #print("Processing files in: " + dirname)
        for filename in filenames:
            # print(filename)
            content = readfile(dirname, filename)
            obj = parseJSON(content, filename)
            if obj is not None:
                # print (obj)
                for label in obj:
                    universe_of_labels.add(label["name"])
    return universe_of_labels


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


