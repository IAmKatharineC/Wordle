def append_wordle_to_file(wordle_input, filename):
    with open(filename, 'a') as file:
        file.write(wordle_input + '\n')
        
def main():
    wordle_input = input("Enter the Wordle of the day: ")
    if wordle_input:
        append_wordle_to_file(wordle_input, 'wordlehistory.txt')
        print("Wordle successfully added to the history!")

if __name__ == "__main__":
    main()
