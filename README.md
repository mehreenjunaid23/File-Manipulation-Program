# File-Manipulation-Program
This is a simple file manipulation program that allows you to perform various functions on a text file. The program is written in Python and can be executed by running the main function in the program.

# How to use:
Run the main function to start the program.
You will be prompted to enter the name of the file you wish to manipulate.
The program will then read the file, displaying its contents and prompting you to perform various manipulations on the data.
Once you are done, the program will exit.
Functions

# The following functions are available in the program:

# write_file(name):
Opens the specified file in read mode and reads all lines.
Separates all words and stores them in a list.
Returns the list of words.

# read_lines(folder)
Opens the specified file in read mode and reads its contents.
Prints the contents of the file to the console.

# write_list(name)
Opens the specified file in read mode and lists its contents.
Returns a list of the file contents.

# add_word(word_list)
Opens the specified file in append mode.
Prompts the user to enter words to add to the file.
Writes the words to the end of the file.

# add_new_line(list)
Uses the write_file function to read all lines in the specified file and store them in a list.
Adds a new line after every word in the list.
Writes the modified list back to the file.

# remove_word(file_name)
Prompts the user to enter a word to remove from the file.
Removes the specified word from the file.

# word_replace(file_name)
Prompts the user to enter a word to replace and the word to replace it with.
Replaces all occurrences of the first word with the second word in the file.

# remove_occurrence(file_name)
Prompts the user to enter a word to remove all occurrences of.
Removes all occurrences of the specified word from the file.

# sort_list(name)
Opens the specified file in read mode, lists its contents, and sorts them in ascending order.
Writes the sorted list back to the file.

# sort_list_desc(name)
Opens the specified file in read mode, lists its contents, and sorts them in descending order.
Writes the sorted list back to the file.

# reverse_list(name)
Opens the specified file in read mode, lists its contents, and reverses the order of the list.
Writes the reversed list back to the file.

