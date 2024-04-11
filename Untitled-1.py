


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

def num_of_words(file_name):
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if letter==" ":
                count+=1
    if (count>1):
        count+=1
    return count

def num_of_paragraphs(file_name):
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if letter=="\t":
                count+=1
    return count


def sentences_per_paragraph():
    pass

print(num_of_sentences("testFile.txt"))
print(num_of_characters("testFile.txt"))
print(num_of_words("testFile.txt"))
print(num_of_paragraphs("testFile.txt"))