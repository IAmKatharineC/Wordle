def append_wordle_to_file(wordle_input, filename):
    with open(filename, 'a') as file:
        file.write(wordle_input + '\n')

def sort_wordle_history(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines.sort()
    with open(filename, 'w') as file:
        file.writelines(lines)
        
wordle_input = input("Enter the Wordle of the day: ")
if wordle_input:
    append_wordle_to_file(wordle_input, 'wordlehistory.txt')
    sort_wordle_history('wordlehistory.txt')
    print("Wordle successfully added to the history!")

