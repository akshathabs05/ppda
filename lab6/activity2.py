# Function to count words and their frequency
def word_count(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Count the total number of words
    total_words = len(words)
    
    # Create a dictionary to store word frequencies
    word_freq = {}

    for word in words:
        word = word.lower()  # Convert to lowercase for case insensitivity
        word_freq[word] = word_freq.get(word, 0) + 1

    return total_words, word_freq

# Get input from user
sentence = input("Enter a sentence: ")

# Get the word count and frequency dictionary
total, frequency = word_count(sentence)

# Display results
print(f"\nTotal words: {total}")
print("Word Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
