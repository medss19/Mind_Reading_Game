from time import sleep
import sys

l = ['aster' , 'lotus' , 'rose' , 'daffodils' , 'lily' , 'lavatera' , 'popy' , 'glogzinia' , 'iris' ,
     'sunflower' , 'jasmine' , 'hibiscus' , 'bluebell' , 'morning glory' , 'marigold' , 'waterlily' ,
     'raffelisia' , 'mangnolia' , 'touch me not' , 'gulmohar' , 'tulsi']

a = ['aster' , 'lotus' , 'lavatera' , 'rose' , 'daffodils' , 'popy' , 'lily']
b = ['iris' , 'hibiscus' , 'aster'  , 'glogzinia' , 'bluebell' , 'sunflower' , 'jasmine']
c = ['waterlily' , 'morning glory' , 'mangnolia' , 'marigold' , 'lotus' , 'raffelesia' , 'glogzinia']
d = ['rose' , 'iris' , 'morning glory' , 'touch me not' , 'tulsi']
e = ['peepal' , 'daffodils' , 'gulmohar' , 'sunflower' , 'hibiscus' , 'touch me not' , 'marigold']
f = ['waterlily' , 'gulmohar' , 'lily' , 'tulsi' , 'jasmine']
g = ['morning glory' , 'hibiscus' , 'peepal' , 'raffelisia' , 'lavatera' , 'gulmohar']
h = ['mangnolia' , 'popy' , 'rose' , 'bluebell' , 'sunflower']


dd = {'ab' : 'aster' , 'ac' : 'lotus' , 'ad' : 'rose' , 'ae' : 'daffodils' , 'af' : 'lily' , 'ag' : 'lavatera' , 'ah' : 'popy' , 'bc' : 'glogzinia' ,
      'bd' : 'iris' , 'be' : 'sunflower' , 'bf' : 'jasmine' , 'bg' : 'hibiscus' , 'bh' : 'bluebell' , 'cd' : 'morning glory' , 'ce' : 'marigold' ,
      'cf' : 'waterlily' , 'cg' : 'raffelisia' , 'ch' : 'mangnolia' , 'de' : 'touch me not' , 'df' : 'tulsi' , 'dg' : 'morning glory' , 'dh' : 'rose' ,
      'ef' : 'gulmohar' , 'eg' : 'gulmohar' , 'eh' : 'sunflower'}

print("WELCOME TO MIND READING GAME\n")
name = input("enter your name: ").upper()
print("\nHello" , name , ". Let's start...\n")

def play():
    global al, ind, yes
    ind, yes = 0, 0
    al, diff = [], []
    combine = [] 
    while True:
        al = iter([a , b , c , d , e , f , g , h])
        diff = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h']
        print("Choose any flower from the given list and keep it in your mind\n")
        print(*l , sep = "\n")
        print("\nNow tell us whether the word you've chosen is present in the following lists or not.\n")
        for i in al:
            print(i)
            ans = input("Y/N : ").upper()
            if ans == 'N':
                ind += 1
                continue
            elif ans == 'Y':
                combine.append(diff[ind])
                ind += 1
                yes += 1
                if yes == 2:
                    com = combine[0] + combine[1]
                    print("\nSO THE WORD THAT YOU HAD CHOSEN IS : ")
                    sleep(0.8)
                    print(dd.get(str(com)))
                    again()
                    sys.exit()
            else:
                print("please enter Y or N")

def again():
    z = input("\nDo you wanna test us again? Y/N : ").upper()
    if z == 'Y':
        play()
    else:
        print("BYEEE" , name)
        sys.exit()
    
play()    



        
    
