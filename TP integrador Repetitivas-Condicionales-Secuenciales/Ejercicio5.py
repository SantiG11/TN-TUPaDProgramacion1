nombre = input('Ingrese el nombre del Gladiador: ')

while not nombre.isalpha():
    print('Error: Solo se permiten letras.')
    nombre = input('Ingrese el nombre del Gladiador: ')

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_gladiador = 15
ataque_enemigo = 12
turno_gladiador = True
ronda = 1

while vida_gladiador > 0 and vida_enemigo > 0:
    
    if turno_gladiador:
        print(f'Ronda: {ronda} | {nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}')
        print(f'Turno del Gladiador {nombre}')
        print('Elige acción: \n1)Ataque pesado \n2)Ráfaga veloz \n3)Curar')

        opcion = input('Seleccione una opción: ')

        while not opcion.isdigit() or opcion not in ("1", "2", "3"):
            print('Error: opción inválida.')
            opcion = input('Seleccione una opción: ')

        opcion = int(opcion)

        if opcion == 1:
            if(vida_enemigo < 20):
                print('Golpe crítico')
                vida_enemigo -= ataque_gladiador * 1.5
                print(f'¡Atacaste al enemigo por {ataque_gladiador * 1.5} puntos de daño!')
            else:
                print(f'Ataque Pesado')
                vida_enemigo -= ataque_gladiador
                print(f'¡Atacaste al enemigo por {ataque_gladiador} puntos de daño!')
        elif opcion == 2:
             print('Ráfaga veloz')
             for i in range(3):
                 vida_enemigo -= 5
                 print('> Golpe conectado por 5 de daño')
        elif opcion == 3:
            print('Curar')
            if(pociones > 0):
                vida_gladiador += 30
                pociones -= 1
                print('¡Te curaste por 30 HP!')
            else:
                print('¡No quedan pociones!')
        
        turno_gladiador = False

    elif not turno_gladiador:
        vida_gladiador -= ataque_enemigo
        print('¡El enemigo te atacó por 12 puntos de daño!')
        turno_gladiador = True
        ronda +=1

    

if vida_gladiador > 0:
    print(f'¡VICTORIA! {nombre} ha ganado la batalla.')
else:
    print(f'DERROTA. Has caído en combate.')
