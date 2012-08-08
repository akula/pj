def checkio_index(str1, str2):
    result = []
    for i in range(len(str1)):
        if ((str2[i]) and (str1[i] == str2[i])):
            result.append(i)
    return result

if __name__ == '__main__':
    checkio_index('abcabcefg' , 'abckfghefggg')
    
