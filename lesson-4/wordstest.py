"""THIS PROGRAM TESTS THAT WORDS WHICH CLIENT INPUTS IS EQAUAL TO THEIR READING ON THE CONTRARY"""


from multiprocessing.dummy.connection import Client


client = input('Please, enter your name:')

word = input(f'Dear {client}, please type a word: ')

word2 = word[::-1]

if word2.lower() == word.lower():
    print('Yes, it is right word')
else:
    print('No, it is wrong word')