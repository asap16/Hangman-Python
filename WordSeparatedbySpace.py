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
