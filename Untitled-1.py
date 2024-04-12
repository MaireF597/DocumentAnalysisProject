


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




def words_per_sentence(file_name):
    array = []
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter=="\n"):
                count=-1
            if (letter==(".") or letter==("?") or letter==("!")):
                array.append(count+1)
                count=0
            elif letter==" ":
                count+=1
    sum = 0
    for val in array:
        sum=sum+val
    return (sum/(len(array)))



def characters_per_word(file_name):
    array = []
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter==(" ")):
                array.append(count+1)
                count=0
            else:
                count+=1
    sum = 0
    for val in array:
        sum=sum+val
    return (sum/(len(array)))

def flesch_reading_ease():
    pass

def fleschkincaid_grade_level():
    pass

def sentences_per_paragraph():
    pass

def passive_sentences():
    pass

#print(num_of_sentences("testFile.txt"))
#print(num_of_characters("testFile.txt"))
#print(num_of_words("testFile.txt"))
#print(num_of_paragraphs("testFile.txt"))
print(words_per_sentence("testFile.txt"))