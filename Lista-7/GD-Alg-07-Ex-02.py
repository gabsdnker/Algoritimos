#DIFERENÇA SIMÉTRICA

from re import X

def main():
    x = [2, 1, 3, 4, 1]
    y = [3, 4, 5]
    diff = list(set(x) ^ set(y))
 
    print(diff) 

if __name__ == '__main__':
    main()       
 