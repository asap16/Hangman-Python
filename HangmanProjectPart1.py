def GetAnswerWithUnderscores(answer, letters_guessed):
    result = ''
    for char in answer:
        if char in letters_guessed:
            result += char
        else:
            result += '_'
    return result


answer = GetAnswerWithUnderscores('welcome', 'mel')
print('GetAnswerWithUnderscores #1: expected _el__me, got', answer)
answer = GetAnswerWithUnderscores('quick', 'rstlne')
print('GetAnswerWithUnderscores #2: expected _____, got', answer)


def GetWordSeparatedBySpaces(word):
    result = ""
    for index in range(len(word)):
        if index == (len(word)-1):
            result += word[index]
        else:
            result += word[index] + " "
    return result 


answer = GetWordSeparatedBySpaces('plane')
print('GetWordSeparatedBySpaces #1: expected p l a n e, got', answer)
answer = GetWordSeparatedBySpaces('to')
# Don't worry about the hasattr function, the if statement, or what they
# do: it's not required for this Hangman assignment.
if hasattr(answer, 'strip') and answer.strip() == answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetWordSeparatedBySpaces #2: expected no spaces at the beginning or end,', text)
    

def IsWinner(answer, letters_guessed):
    c = 0
    for char in answer:
        for index in range(len(letters_guessed)):
            if char == letters_guessed[index]:
                c += 1
                
    if c == len(answer):
        return True
    return False

        
answer = IsWinner('plane', 'anelp')
print('IsWinner #1: expected True, got', answer)
answer = IsWinner('plane', 'plan')
print('IsWinner #2: expected False, got', answer)


def IsLegalGuess(current_guess, letters_guessed):
    
    if current_guess.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        print('Input is not a valid string i.e english alphabets')
        return False
    else:
        if len(current_guess) == 1:
            if current_guess not in letters_guessed.lower():
                return True
            else:
                print('Input already exists')
                return False
        else:
            print('Input is not a single character')
            return False


answer = IsLegalGuess('g', '')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('g', 'rstle')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('bb', 'cat')
print('IsLegalGuess #1: expected False, got', answer)
answer = IsLegalGuess('p', 'yzpr')
print('IsLegalGuess #1: expected False, got', answer)


def GetLegalGuess(letters_guessed):
    input_guessed = input('Input your guess')
    while not IsLegalGuess(input_guessed, letters_guessed):
        input_guessed = input('Input your guess')
    return input_guessed
        

print(GetLegalGuess('abc'))


def IsGuessRevealing(answer, legal_letter_guess):
    if legal_letter_guess in answer:
        return True
    else:
        return False


answer = IsGuessRevealing('welcome', 'c')
print('IsGuessRevealing #1: expected True, got', answer)
answer = IsGuessRevealing('quick', 'z')
print('IsGuessRevealing #1: expected False, got', answer)



