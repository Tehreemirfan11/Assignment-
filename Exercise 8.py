Sentence= input("Enter a String ")
vowel_count= 0
vowel= "aeiou"
for i in Sentence:
    if i in vowel:
        vowel_count=vowel_count+1
print("Total vowel count:" , vowel_count)        