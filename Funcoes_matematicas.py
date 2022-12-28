def eh_primo(num):
    for n in range(2,num):
        if num % n == 0:
            return print("O número",num,"não é Primo")
    return print("O número",num,"é Primo")

def fatorial(num):
    fatorial = num
    for n in range(1,num):
        fatorial *= n 
    return fatorial