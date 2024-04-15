
def num_of_sentences(file_name):
    alph_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_letter=""
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter==(".") or letter==("?") or letter==("!") and last_letter in alph_string):
             count+=1
             last_letter = letter
    return count

def num_of_characters(file_name):
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if letter!=" " and letter!="\n":
                count+=1
    return count

def num_of_words(file_name):
    last_letter=""
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
                if letter==" " and last_letter!=":" and last_letter!=";":
                    count+=1
                last_letter=letter
    if (count>1):
        if (num_of_paragraphs(file_name)>1):
            count+=num_of_paragraphs(file_name)
        else:
            count+=1
    return count

def num_of_paragraphs(file_name):
    count = 1
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if letter=="\n":
                count+=1
    return count


def sentences_per_paragraph(file_name):
    array = []
    count=0
    alph_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_letter=""
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter=="\n"):
                array.append(count)
            elif (letter==(".") or letter==("?") or letter==("!")and last_letter in alph_string):
                count+=1
                last_letter=letter
    array.append(count)
    sum = 0
    for val in array:
        sum=sum+val
    return (sum/(len(array)))

def words_per_sentence(file_name):
    array = []
    alph_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_letter=""
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter=="\n"):
                count=1
            if (letter==(".") or letter==("?") or letter==("!")and last_letter in alph_string):
                array.append(count)
                count=0
            elif letter==" " and last_letter!=":" and last_letter!=";":
                count+=1
            last_letter=letter
   
    sum = 1
    for val in array:
        sum=sum+val
    return (round(sum/(len(array)),1))

def characters_per_word(file_name):
    array = []
    count = 0
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter=="\n"):
                count=0
            if (letter==(".") or letter==("?") or letter==("!")):
                array.append(count)
                count=-1
            if (letter==(" ") and count!=0):
                array.append(count)
                count=0
            else:
                if (letter!=","):
                    count+=1
    sum = 0
    for val in array:
        sum=sum+val
    return (round(sum/(len(array)),1))

def syllable_counter(file_name):
    pass

def flesch_reading_ease(file_name):
    pass
    # 206.835 - (1.015 * ASL) - (84.6 * ASW)
    # ASL - average sentence length (num of words/num of sentences)
    # ASW - average num of syllables per word (num of syllables / num of words)
    syll_sum = 0.0
    word = ""
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter==" " or letter=="\n" or letter==(".") or letter==("?") or letter==("!")):
                var = (syllable_counter(word))
                
                syll_sum +=(var)
                word=""
            else:
                word+=letter

    ASL = num_of_words(file_name) / num_of_sentences(file_name)
    ASW = syll_sum / num_of_words(file_name)
    return (206.835 - (1.015 * ASL) - (84.6 * ASW))

def fleschkincaid_grade_level(file_name):
    pass
    # 20(.39*ASL)+(11.8*ASW) - 15.59
    # ASL - average sentence length (num of words/num of sentences)
    # ASW - average num of syllables per word (num of syllables / num of words)
    syll_sum = 0
    word = ""
    var = open(file_name, "r")
    for line in var:
        for letter in line:
            if (letter==" " or letter=="\n" or letter==(".") or letter==("?") or letter==("!")):
                syll_sum = syll_sum + syllable_counter(word)
                word=""
            else:
                word+letter

    ASL = num_of_words(file_name) / num_of_sentences(file_name)
    ASW = syll_sum / num_of_words(file_name)
    return (.39*ASL)+(11.8*ASW) - 15.59

def passive_sentences():
    pass


def document_reader(file_name):
    print("Words: " ,num_of_words(file_name))
    print("Characters: ", num_of_characters(file_name))
    print("Paragraphs: ",num_of_paragraphs(file_name))
    print("Sentences: ",num_of_sentences(file_name))
    print("Sentences per Paragraph: ",sentences_per_paragraph(file_name))
    print("words per Sentence: ",words_per_sentence(file_name))
    print("Characters per Word: ",characters_per_word(file_name))
    #print("flesch_reading_ease: ",flesch_reading_ease(file_name))
    #print("fleschkincaid_grade_level: ",fleschkincaid_grade_level(file_name))

document_reader("testFile.txt")