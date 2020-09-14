#even and odd number

n = int(input())  

if (n%2)==1:
    print("Weird")
elif (n%2)==0 and n>2 and n<5:
    print("Not Weird")
elif (n%2)==0 and n>6 and n<20:
    print("Weird")
elif (n%2)==0 and n>=20:
    print("Not Weird")


#squares till integer n
n = int(input())
i = 0
while i < n:
    print(i*i)
    i += 1


#cube with range
if __name__ == '__main__':
    n = int(input())
for i in range(0, n):
    print(i*i*i)

#define a leap year
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    
    return False

year = int(input())
print(is_leap(year))