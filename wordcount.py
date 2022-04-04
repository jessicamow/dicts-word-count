"""Count words in file."""

# letter_counts = {}

#     for letter in phrase:
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

#     return letter_counts

# put your code here.
def word_count(filename):
    file1 = open(filename)
    word_count = {}
    for line in file1:
        words = line.split(' ')
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    
    for word, count in word_count.items():
        print(word, count)
 
