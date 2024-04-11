


def essay_reader(file_name):
    number = 0
    num_of_sentences(file_name)



def num_of_sentences(file_name):
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter==(".") or letter==("?") or letter==("!")):
             count+=1
    return count

def num_of_characters(file_name):
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if letter!=" ":
                count+=1
    return count

print(num_of_sentences("testFile.txt"))
print(num_of_characters("testFile.txt"))