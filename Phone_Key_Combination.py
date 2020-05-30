mapping = ['', '', 'ABC', 'DEF', 'GHI','JKL','MNO','PQRS','TUV','WXYZ']

def combination(key):
    result = []
    temp = [0] * len(key)
    
    def backtrack(letter_index):
        if letter_index == len(key):
            result.append(('').join(temp))
        else:
            for i in mapping[key[letter_index]]:
                temp[let_index] = i
                backtrack(letter_index + 1)
                
    backtrack(0)
    print(len(result))
    return result

print(combination([2,3]))