from clases.ejercicioa import *
from clases.ejerciciob import *
from clases.ejercicioc import *

def main():
    acabar=False
    while(acabar==False):
        seguir=str(input("¿Quiere seguir viendo ejercicios?: "))

        if seguir=="si" or seguir=="Si" or seguir=="SI":
            cual=str(input("¿Que ejercicio quiere hacer?: "))

            if cual=="a" or cual=="A":
                ny = newyork()
                del ny
            
            if cual=="b" or cual=="B":
                
                yin = yin()
                yang = yang()
                yin.yang = yang
                
                print(yang)
                print(yang is yin.yang)
                del(yang)

            if cual=="c" or cual=="C":

            else:
                print("no ha escogido ningun ejercicio: ")

        if seguir!="si" or seguir!="Si" or seguir!="SI":
            acabar==True
        
if __name__=='__main__':
    main()
