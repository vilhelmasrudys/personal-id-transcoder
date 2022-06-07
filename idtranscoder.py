personal_code=input("Please enter your personal number in format 12345678900 :  ")
def creating_var():
    global a,b,c,d,e,f,g,h,i,j,k
    a,b,c,d,e,f,g,h,i,j,k  = [int(i) for i in list(personal_code)]
# iš pateikto personal_code kiekvieno nari prilyginame  variable nuo a iki k , taipogi kiekvieną kintąmąjį padarome integeriu
# ir su global kiekviena kintamaji a-k padaro global kintamuoju
def control_number_generator():
    variables = [a, b, c, d, e, f, g, h, i, j]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    list3 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    control_number_1 = (sum([a * b for a, b in zip(variables, list2)])) % 11
    control_number_2 = (sum([a * b for a, b in zip(variables, list3)])) % 11
# list2 ir list 3 yra daugikliai , kuriuos reikia sudauginti is kintamuju,
# gautas reiksmes susumuojam ir suskaiciuojam liekana padalinus is 11
    if control_number_1 == 10:
        if control_number_2 == 10:
            return 0
        else:
            return control_number_2
    else:
        return control_number_1
def code_validator():
    if (a >= 1 or a <=6 or a ==9 ) and (d == 0,1 ) and (sum([d + e ]) <= 12) and (f == 0,1,2,3 )  and (sum([f + g ]) <= 31) and (control_number_generator() == k):
        print(f"This: {personal_code} Personal code is valid")
    else:
        print(f"This: {personal_code} Personal code is not valid")
if (len(personal_code)) == 11 and personal_code.isdigit():
        creating_var()
        control_number_generator()
        code_validator()
else:
    print(f"This: {personal_code}  identification number is in wrong format")