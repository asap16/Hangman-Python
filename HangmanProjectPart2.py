
import random


def GetAnswerWithUnderscores(answer, letters_guessed):
    result = ''
    for char in answer:
        if char in letters_guessed:
            result += char
        else:
            result += '_'
    return result


def GetWordSeparatedBySpaces(word):
    result = ""
    for index in range(len(word)):
        if index == (len(word)-1):
            result += word[index]
        else:
            result += word[index] + " "
    return result 
    

def IsWinner(answer, letters_guessed):
    c = 0
    for char in answer:
        for index in range(len(letters_guessed)):
            if char == letters_guessed[index]:
                c += 1
                
    if c == len(answer):
        return True
    return False



def IsLegalGuess(current_guess, letters_guessed):
    if not current_guess.lower().isalpha():
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


def GetLegalGuess(letters_guessed):
    input_guessed = input('Input your guess')
    while not IsLegalGuess(input_guessed, letters_guessed):
        input_guessed = input('Input your guess')
    return input_guessed
        

def IsGuessRevealing(answer, legal_letter_guess):
    if legal_letter_guess in answer:
        return True
    else:
        return False


def GetAllEnglishWords():
    find_words = open('hangman_english_words.txt')
    list_of = []
    item = find_words.readline()
    for item in find_words:
        char = item.strip()
        list_of.append(char)
    find_words.close()
    return list_of


def GetRandomWord(words):
    return words[random.randint(0,len(words)-1)]


'''def Play(answer):
    letters_guessed = ''
    strikes = 0
    print('You have', strikes, 'strikes.')
    print(GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed)))
    while strikes < 5:
            current_guess = GetLegalGuess(letters_guessed)
            if IsGuessRevealing(answer, current_guess) == False:
                    strikes += 1                                   
                    print('You have', strikes, 'strikes.')
                    letters_guessed += current_guess
                    print(GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed)))
            else:
                    letters_guessed += current_guess
                    print(GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed)))
                    if IsWinner(answer, letters_guessed) == True:
                        print("You Won")
                        return True
                    print('Continue. Keep the guesses coming.')
    print ('The answer is', answer)
    print ("You lost")'''
        

def StartupandPlay():
    words = GetAllEnglishWords()
    answer = GetRandomWord(words)
    Play(answer)
    user_input = Input('Do you want to Continue (y/n)')
    if user_input.lower() == 'y':
        StartupandPlay()


def GetPlayRecord():
    opening_doc = open('hangman_play_record.txt')
    get_record = opening_doc.readline()
    delimiter = ','
    get_record = get_record.split(delimiter)
    record_list = []
    for item in get_record:
        item = int(item)
        record_list.append(item)
    opening_doc.close()
    return record_list
    
ans = GetPlayRecord()
print(ans)


def RecordPlay(win):
    get_list = GetPlayRecord()
    write_doc = open('hangman_play_record.txt', 'w')
    if win == True:
        get_list[0] = get_list[0] + 1
        get_list[1] = get_list[1] + 1
    else:
        get_list[1] = get_list[1] + 1
    record_value = str(get_list[0]) + ',' + str(get_list[1])
    write_doc.write(record_value)
    write_doc.close()


def StartupAndPlayVersion2():
    call_list = GetPlayRecord()
    win_times = call_list[0]
    played_times = call_list[1]
    words = GetAllEnglishWords()
    answer = GetRandomWord(words)
    print('You have won', win_times, 'times')
    print('You have played', played_times, 'times')
    value_return = Play(answer)
    if value_return == True:
        RecordPlay(value_return)
    else:
        RecordPlay(None)
    user_input = input('Do you want to Continue (y/n)')
    if user_input.lower() == "y":
        StartupAndPlayVersion2()
    else:
         call_list = GetPlayRecord()
         win_times = call_list[0]
         played_times = call_list[1]
         print('You have won', win_times, 'times')
         print('You have played', played_times, 'times')

def main():
    StartupAndPlayVersion2()

if __name__ == '__main__':
    main()

        
    
    
        
    





    


            
            
            
            






