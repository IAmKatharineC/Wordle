from collections import Counter

def main():
    filename = 'wordlehistory.txt'
    try:
        with open(filename, 'r') as file:
            content = file.read()
            letter_counts = Counter(char.upper for char in content if char.isalpha())
            print("Letter Frequencies: ")
            for letter,count in letter_counts.items():
                print(f"{letter}: {count}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        
if __name__ == "__main__":
    main()
