# Open file in read mode
file = open("Python", "r")
data = file.read()
words = data.split()
# To count number of words
print("Number of words in a file are: ", len(words))

# To count number of characters
No_of_char = len(data)
print("Number of characters i file: ", No_of_char)

# Get number of occurrences of the word
occurrences = data.count("file")  # Pass the word
print("Number of occurrences of word: ", occurrences)

# Close the file
file.close()