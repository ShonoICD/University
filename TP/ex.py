# написать функцию для рекурсивного обращения строки
def reverse(string):
    if len(string) <=1:
        return string
    
    return reverse(string[1:]) + string[0]



orig = "123456789"
neorig = reverse(orig)
print(orig)
print(neorig)


    # a[0] b[1] c[2]
    # c[2] b[1] a[0]