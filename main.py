def main():
    path = "books/frankenstein.txt"
    text = open_text(path)
    words = word_count(text)
    chars = char_count(text)
    print(f"--Begin the report with {path}--")
    print(f"{words} words found in the document")
    for char in chars:
        print(f'the {char} character was found {chars[char]} times ')
    
    print("--End report--")
        
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = {}
    lowering = text.lower()
    words = list(lowering)
    for word in abc:
        count[word] = words.count(word)

    return count


def open_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents



main()