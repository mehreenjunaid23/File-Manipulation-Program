import os
#this is the main function that will be called to run the program
def main():
    #ask the user to enter a file name
    file_name = input("enter the name of the file")
    #call the write_file function with the filename as a parameter
    write_file(file_name)
    # call the read_lines function with the filename as a parameter
    read_lines(file_name)
    #ask the user if they want to see the options available
    option = input("do you want to see your options? y=yes")
    #print an empty line for neatness
    print()
    #make a loop for the options so the user can try multiple options
    while option=="y" or option=="Y":
        #get the input of the letter which refers to the option they want to use
        question=input( "If you want to add a word enter 'A'"+ "\n"
                        "If you want to remove a word enter 'R'"+ "\n"
                        "If you want to sort the list enter 'S'"+ "\n"
                        "If you want to add a line after every word in the list enter 'AL'"+ "\n"                                          
                        "If you want to replace a word in the list enter 'WR'" +"\n"
                        "If you want to remove the occurrence of a word in the list enter 'RO'" +"\n"                                                        
                        "If you want to reverse the list enter'RL'"+"\n")
        # print an empty line for neatness
        print()
        #create an if funtion to call the function the user wants to use
        if question=="a" or question=="A":
            add_word(file_name)
            write_list(file_name)
            print()
        elif question=="r" or question=="R":
            remove_word(file_name)
            print()
        elif question=="wr" or question=="WR":
            word_replace(file_name)
            write_list(file_name)
            print()
        elif question=="rl" or question=="RL":
            write_list(file_name)
            reverse_list(file_name)
            print()
        elif question=="s" or question=="S":
            #ask user which order they want the list to be sorted
            ask=input("do want ascending or descending order? enter 'a' for acsending and 'd' for descending:")
            print()
            #this if function calls the funtion the user wants. Either ascending or descending
            if ask=="a" or ask=="A":
                sort_list(file_name)
                print()
            elif ask=="d" or ask=="D":
                sort_list_desc(file_name)
                print()
        elif question=="AL" or question=="al":
            add_new_line(file_name)
            print()
        elif question=="ro" or question=="RO":
            remove_occurrence(file_name)
            print()
        option = input("do you want to try another option? y=yes")
        print()
    #incase the user doesn't wan't to continue, end the program with this if function
    if option != "y":
        print("THANK YOU FOR USING THIS PROGRAM :) ")
        print("Goodbye :) ")


#define the write_file function
def write_file(name):
    #create an empty list
    new_list = []
    #open the file in the read mode
    infile = open(name, 'r')
    #create a counter variable
    count = 0
    #make a loop to read all lines
    while True:
        count += 1
        #make a variable that refers to reading a line
        line = infile.readline()
        #add a stop if there are no more words in the file
        if not line:
            break
        #seperate all the words
        new_line = line.split()
        #a
        new_list.extend(new_line)
    return (new_list)


#define the read_lines function
def read_lines(folder):
    #open the file and assign a variable to it
    infile=open(folder, 'r')
    #read the file and add to to content variable
    file_contents=infile.read()
    #display file content
    print("The content of your file is")
    print(file_contents)
    #close the file
    infile.close()


#define write_list function
def write_list(name):
    #open file in read mode
    f = open(name, 'r')
    #list the content of the file
    myList = [line.strip() for line in f]
    #close file
    f.close()
    #display list
    print("your list is:")
    print(myList)
    print()
    return myList


#define add_word function
def add_word(word_list):
    #open file in mode 'a'
    my_file = open(word_list, 'a')
    #create a variable to control the loop
    choice="y"
    #make a loop to add words to the list
    while choice == 'y' or choice == 'Y':
        print('Enter the word you want to add', sep='')
        Word = input('word : ')
        #write the words inputted into the file
        my_file.write(Word + '\n')
        print('Do you want to add another word?')
        choice = input('Y = yes, anything else = no: ')
    #close file
    my_file.close()
    print('Data appended to your file')
    print()


#define add_new_line function
def add_new_line(list):
    #make a list for the content by using the write_file function
    new_list= write_file(list)
    #make an empty list
    final_list = []
    #add an empty line after every word
    for i in new_list:
        final_list.append(i)
        final_list.append('')
    #display final list
    print(final_list[:-1])

#define reverse_list function
def reverse_list(name):
    # make a list for the content by using the write_file function
    myList = write_file(name)
    #reverse the list
    myList.reverse()
    print()
    #display the list
    print("your reversed list is:")
    print(myList)


#define word_replace function
def word_replace(name):
    #ask user for the word they want to replace
    word=input("enter the word u want to replace")
    #ask user for the new word
    change=input("enter the new word")
    #open the file and read it
    f = open(name, 'r')
    linelist = f.readlines()
    #then close the file
    f.close()

    # Re-open file here
    f2 = open(name, 'w')
    #and locate the word the user wants to change and add the new word in that position
    for line in linelist:
        line = line.replace(word, change)
        #write the changes on the file
        f2.write(line)
    #close the file
    f2.close()


#define sort_list funtion
def sort_list(name):
    #make a list by using write_file function
    myList = write_file(name)
    print("your sorted list in ascending order is:")
    #sort that list
    myList.sort()
    #display sorted list
    print(myList)
    print()


#define sort_list_desc
def sort_list_desc(name):
    # make a list by using write_file function
    myList = write_file(name)
    #sort the list
    myList.sort()
    #reverse the sorting to get it in descending order
    myList.reverse()
    print()
    #display sorted list
    print("your sorted list in descending order is:")
    print(myList)


#defining remove function
def remove_word(word_list):
    # ask user to enter the word they want to remove
    print('Enter the word you want to remove:')
    # input the word here
    Word=input('word:')
    #make a new list by using write_file function
    new_list = write_file(word_list)
    #locate and remove the desired word
    for i in range(len(new_list)):
        if Word == new_list[i]:
            new_list.remove(Word)
            break
    #display updated list
    print('Your updated list is:')
    print(new_list)


#defining remove occurrence function
def remove_occurrence(word_list):
    # open file with read method
    f=open(word_list,'r')
    print('Enter the word for which you want to remove the occurrence:')
    # input the word you would like to remove
    Word=input('word:')
    #locate the positions for whenever the word appears in the list and remove it
    myList=[line.strip() for line in f]
    myList=[i for i in myList if i!=Word]
    print()
    # disply new list
    print('Your updated list is:')
    print(myList)
    #close file
    f.close()

main()