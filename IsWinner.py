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
