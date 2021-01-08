def isAlienSorted(words, order):
    # iterate through the words list
    flag = False
    for i in range(len(words) - 1):
        # compare current word with the next one char by char 
        for idx in range(len(words[i])):
            current_char_index = order.index(words[i][idx])
            # if the next word is shorter - return False
            try:
                next_char_index = order.index(words[i + 1][idx])
            except:
                flag = False
                return flag
            # if current and next chars are equal
            if current_char_index == next_char_index:
                flag = True
                continue
            else:
                if current_char_index < next_char_index:
                    flag = True
                    if i + 1 == len(words) - 1:
                        break
                else:
                    flag = False
                    return flag
        if flag is True: return True
    # return flag


print(isAlienSorted(["hello","leetcode"],'hlabcdefgijkmnopqrstuvwxyz'))
print(isAlienSorted(["word","world","row"],'worldabcefghijkmnpqstuvxyz'))
print(isAlienSorted(["world","wor"],'rowldabcefghijkmnpqstuvxyz'))
print(isAlienSorted(["hello","hello"],'abcdefghijklmnopqrstuvwxyz'))
print(isAlienSorted(["apple","app"],'abcdefghijklmnopqrstuvwxyz'))