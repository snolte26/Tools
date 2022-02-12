#Author: Alex Nolte
#Created: 1/28/2020

print("Welcome to the word counter, ")
print()


def Word_Count(file_for_counting):

    #opens the file in read mode and creates an empty list
    file = open(file_for_counting, "r+", encoding="utf-8-sig")
    wordcount=[]

    #for each word in the file, it adds it to the empty list
    for word in file.read().split():
        wordcount.append(word)
    #closes the file
    file.close();
    #print(wordcount)

    print()

    #prints the length of the list as the word count
    print("Word Count: " + str(len(wordcount)))
        


def main():
    #asks user for file name, then adds the extension
    file = input("Please type the name of the text document with no file extensions: ")
    file_name = file + ".txt"
    print()
    
    print(file_name)

    #sends the file name to the Word_Count function
    words = Word_Count(file_name)

#runs the main function
main()


input()
