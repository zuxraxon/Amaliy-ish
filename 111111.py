# 5.	m massa kilogrammlarda berilgan. Uning tonnalardagi qiymati topilsin.
import math
mkg=int(input("Massani kiriting : "))
mt=mkg/1000
print("Massa tonnalarrdagi qiymati : ", mt)


# 5.	Doiraning yuzasi S berilgan. Uning diametri d va doirani chegaralab turuvchi aylana uzunligi hisoblansin. =3,14 ga teng deb olinsin.
s=float(input("doirani yuzini kiriting : "))
d=(4*s/3.14)**1/2
l=d*3.14
print("Diametri=",d)
print("Aylanani uzunligi=",l)


#5. Uchburchаkning uchtа uchi koordinаtаlаri berilgаn: (x1,y1), (x2,y2), (x3,y3).
# Uning perimetrini vа mаydonini toring. Uchburchаkning mаydonini topishdа Geron formulаsidаn foydаlаning 					 .
# Bu erdа а, b, s - uchburchаk tomonlаri,  p=(а+b+s)/2 – yarim perimetr.

print("x1=",end=" ")
x1=int(input())
print("y1=",end=" ")
y1=int(input())
print("x2=",end=" ")
x2=int(input())
print("y2=",end=" ")
y2=int(input())
print("x3=",end=" ")
x3=int(input())
print("y3=",end=" ")
y3=int(input())
a=((x2-x1)**2+(y2-y1)**2)**(1/2)
b=((x3-x2)**2+(y3-y2)**2)**(1/2)
c=((x3-x1)**2+(y3-y1)**2)**(1/2)
p=(a+b+c)/2
s=(p*(p-a)* (p-b)* (p-c))**(1/2)
print("Uchburchak perimetr=",2*p)
print("Uchburchak yuzasi=",s)

# 5.1


a = int(input("a - qiymatini kiriting: "))
b = int(input("b - qiymatini kiriting: "))
p = 2 * (a + b)
s = a * b
print(f'togri tortburchak perimetri={p}')
print(f'togri tortburchak yuzi={s}')

# 5.2

# A=int(input("kichik sonni kiriting: A="))
# B=int(input("katta sonni kiriting: B="))
# n=B-A+1
# for i in range(0,n):
#     print(B-i)

# son = int(input())
# son1 = int(input())
# son2 = int(input())
# musbat = 0
# manfiy = 0
# nol = 0
# if son=0:
#     nol += 1
# elif son > 0:
#     musbat +=1
# else:
#     manfiy+=1

# if son2=0:
#     nol += 1
# elif son2 > 0:
#     musbat +=1
# else:
#     manfiy+=1

# if son1=0:
#     nol += 1
# elif son1 > 0:
#     musbat +=1
# else:
#     manfiy+=1


# 5.1
import math

x = float(input())
y = float(input())
z = float(input())
gamma = 5 * math.atan(x) - (1 / 4) * math.acos(x) * (x + 3 * math.fabs(x - y) + x ** 2) / (
            math.fabs(x - y) * z + x ** 2)
print(gamma)

# 5.2
import math

x = float(input('0<x<1  x='))
n = int(input('n='))
s = 0
if (0 < x and x < 1):
    for i in range(1, n):
        s = s + (math.pow(-1, i) * math.pow(x, (2 * i + 1))) / (2 * i + 1)
print(s)


