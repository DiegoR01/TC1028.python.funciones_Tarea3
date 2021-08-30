
def main():
    #escribe tu código abajo de esta línea
    year=float(input("inserta el año:"))


if year % 4 == 0 and (year % 100 != 0 or año % 400 == 0):
    print ("true")
else: 
    print ("false")
    pass

if __name__=='__main__':
    main()
