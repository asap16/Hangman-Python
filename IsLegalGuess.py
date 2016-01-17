def IsLegalGuess(current_guess, letters_guessed):
    if current_guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        print("Input is not a valid string i.e english alphabets")
        return False
    else:
        if len(current_guess) == 1:
            if current_guess not in letters_guessed.lower():
                return True
            else:
                print("Input already exists")
                return False
        else:
            print("Input is not a single character")
            return False
    


answer = IsLegalGuess('g', '')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('g', 'rstle')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('bb', 'cat')
print('IsLegalGuess #1: expected False, got', answer)
answer = IsLegalGuess('p', 'yzpr')
print('IsLegalGuess #1: expected False, got', answer)
