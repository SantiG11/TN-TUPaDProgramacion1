energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ''
cerraduras_forzadas = 0

nombre = input('Ingrese su nombre: ')

while not nombre.isalpha():
    print('Error: El nombre debe contener solo letras.')
    nombre = input('Ingrese su nombre: ')

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print('¡Alarma activada! El acceso ha sido denegado.')
        break

    print(f'Estado: \nEnergía: {energia} \nTiempo restante: {tiempo} \nCerraduras abiertas: {cerraduras_abiertas}/3')
    print('Menú: 1) Forzar cerradura 2) Hackear panel 3) Descansar')

    opcion = input('Seleccione una opción: ')

    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
         print('Error: opción inválida.')
         opcion = input('Seleccione una opción: ')

    opcion = int(opcion)
    
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        cerraduras_forzadas += 1

        
        if cerraduras_forzadas >= 3:
             alarma = True
             print('Alarma activada.')    
        elif energia < 40:
            print('Riesgo de alarma')
            
            num = input('Elija un número del 1 al 3: ')
            
            while  not num.isdigit() or num not in ('1', '2', '3'):
                    num = input('Error: Seleccione una opción correcta, un número del 1 al 3')

            num = int(num)

            if num == 3:
                 alarma = True
                 print('Alarma activada.')
                 
            
        if not alarma:
            print('Cerradura forzada correctamente.')
            cerraduras_abiertas += 1

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        cerraduras_forzadas = 0

        for i in range(4):
             codigo_parcial += 'A'
             print(f'Código parcial: {len(codigo_parcial)}/8')

        if len(codigo_parcial) >= 8:
            print('Código hackeado.')
            cerraduras_abiertas += 1
            codigo_parcial = ''
    
    elif opcion == 3:
        tiempo -= 1
        energia += 15
        cerraduras_forzadas = 0

        if alarma:
             energia -= 10

        if energia > 100:
             energia = 100     

         
         
if cerraduras_abiertas == 3:
    print('Victoria.')
elif energia <= 0 or tiempo <= 0 :
    print('Derrota.')
elif alarma :
    print('Bloqueado por alarma. Derrota.')