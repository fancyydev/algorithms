#Encuentra la subcadena mas larga sin caracteres repetidos
def length_of_longest_substring(s):
    char_set = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        # Se eliminan del conjunto todas las letras desde left hasta donde se encuentre la repetida analizada en right
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        #Se agrega lo que se este enasliz
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
        print(char_set)

    return max_length

print(length_of_longest_substring('abfcbaccbfdgb'))