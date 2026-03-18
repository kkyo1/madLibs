# Mad Libs
# The program reads an text file and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, or VERB that appears

from pathlib import Path

# file path
file_path = Path('C:/Users/.../Desktop/Teste Python/madLibs.txt')

print("Lets play a game!\nI'll give u a phrase and you complete it")

# reading
with file_path.open('r', encoding='utf-8') as file:
    text = file.read()

print(text)

print('Now you need to change the capitalized words, respectively\nLet\'s start')

# processing
words = text.split()

for i in range(len(words)):
    word = words[i]

    if word.startswith('ADJECTIVE'):
        replacement = input('Enter an adjective: ').lower()
        words[i] = replacement + word[len('ADJECTIVE'):]

    elif word.startswith('NOUN'):
        replacement = input('Enter a noun: ').lower()
        words[i] = replacement + word[len('NOUN'):]

    elif word.startswith('VERB'):
        replacement = input('Enter a verb: ').lower()
        words[i] = replacement + word[len('VERB'):]

# reconstruct
new_text = ' '.join(words)

print(new_text)

# writing
file_path.write_text(new_text, encoding='utf-8')
