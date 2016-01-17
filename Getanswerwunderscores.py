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
