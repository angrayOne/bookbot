file_path = "books/frankenstein.txt"
def main():
    with open(file_path) as f:
        file_contents = f.read()
    print(file_contents)
    word_count = word_counter(file_contents)
    char_frequency = char_counter(file_contents)
    generate_report(file_path, word_count, char_frequency)
    
def word_counter(file_contents):
    words = file_contents.split()
    word_count = len(words)
    print(word_count)
    return word_count

def char_counter(file_contents):
    text_lower = file_contents.lower()
    frequency = {}
    for char in text_lower:
        if char.isalnum(): frequency[char] = frequency.get(char, 0) + 1
    print(frequency)
    return frequency
    
def generate_report(file_path, word_count, char_frequency):
    sorted_frequency = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report for {file_path} ---")
    print(f"Word count: {word_count} words found in the document\n")
    
    for char, count in sorted_frequency:
        print(f"The '{char}' was found {count} times")
        
    print("--- End report ---")
    

if __name__ =="__main__":
    main()