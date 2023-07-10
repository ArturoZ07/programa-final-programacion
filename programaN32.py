print('programa- 32 programa que dice cual es mayor o menor o igual')
def programa_32():
 word = '12345678910'
 for letter in word:
    if letter == '9' :
         break
    print(letter)
    for i in range (1, 11):
     if i > 5:
         print('mayor a 5')
     elif i < 5:
         print('menor a 5')
     else:
         print('es igual a 5')
     if i == 9:
         break
programa_32()
