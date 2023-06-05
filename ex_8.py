def count_word_occurrences(filename):
    word_count = {}
    
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.strip().split()
            
            # Count the occurrences of each word
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    # Print the words and their counts
    for word, count in word_count.items():
        print(f'{word}: {count}')

# Usage example
filename = 'sample.txt'  # Replace with the path to your text file
count_word_occurrences(filename)
