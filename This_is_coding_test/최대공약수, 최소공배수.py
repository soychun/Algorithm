최대공약수
유클리드 호제법 x,y의 최대공약수는 y,r의 최대공약수와 같다는 원리를 이용하는 것

def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x
print(x)