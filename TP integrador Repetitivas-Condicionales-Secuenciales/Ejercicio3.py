lunes1 = ''
lunes2 = ''
lunes3 = ''
lunes4 = ''
turnos_ocupados_lunes = 0

martes1 = ''
martes2 = ''
martes3 = ''
turnos_ocupados_martes = 0

nombre_operador = input('Nombre del operador: ')

while not nombre_operador.isalpha():
    print('Error: el nombre debe contener letras solamente.')
    nombre_operador = input('Nombre del operador: ')

opcion = 0

while opcion != 5:
    print('1) Reservar turno 2) Cancelar turno (por nombre) 3) Ver agenda del día 4) Ver resumen general 5) Cerrar sistema ')
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        print('Reservar turno')
        dia = 0

        while dia != '1' and dia != '2':
            dia = input('Seleccione un día: 1)Lunes 2) Martes ')
            if dia == '1':
                paciente = input('Ingrese el nombre del paciente: ')

                while not paciente.isalpha():
                    print('Error: el nombre debe contener letras solamente.')
                    paciente = input('Ingrese el nombre del paciente: ')

                if lunes1 == paciente or lunes2 == paciente or lunes3 == paciente or lunes4 == paciente:
                    print('Error: El paciente ya tiene turno este día.')
                    break

                if lunes1 == '':
                    lunes1 = paciente
                    turnos_ocupados_lunes += 1
                    print('Turno 1 del lunes reservado para el paciente.')
                elif lunes2 == '':
                    lunes2 = paciente
                    turnos_ocupados_lunes += 1
                    print('Turno 2 del lunes reservado para el paciente.')
                elif lunes3 == '':
                    lunes3 = paciente
                    turnos_ocupados_lunes += 1
                    print('Turno 3 del lunes reservado para el paciente.')
                elif lunes4 == '':
                    lunes4 = paciente
                    turnos_ocupados_lunes += 1
                    print('Turno 4 del lunes reservado para el paciente.')
                else:
                    print('Error: No hay turnos disponibles para este día.')

            elif dia == '2':
                paciente = input('Ingrese el nombre del paciente: ')

                while not paciente.isalpha():
                    print('Error: el nombre debe contener letras solamente.')
                    paciente = input('Ingrese el nombre del paciente: ')

                if martes1 == paciente or martes2 == paciente or martes3 == paciente:
                    print('Error: El paciente ya tiene turno este día.')
                    break

                if martes1 == '':
                    martes1 = paciente
                    turnos_ocupados_martes += 1
                    print('Turno 1 del martes reservado para el paciente.')
                elif martes2 == '':
                    martes2 = paciente
                    turnos_ocupados_martes += 1
                    print('Turno 2 del martes reservado para el paciente.')
                elif martes3 == '':
                    martes3 = paciente
                    turnos_ocupados_martes += 1
                    print('Turno 3 del martes reservado para el paciente.')
                else:
                    print('Error: No hay turnos disponibles para este día.')

            else:
                print('Error: seleccione un día correcto.')

    elif opcion == '2':
        print('Cancelar turno')
        dia = 0

        while dia != '1' and dia != '2':
            dia = input('Seleccione un día: 1)Lunes 2) Martes ')

            if dia == '1':
                paciente = input('Ingrese el nombre del paciente: ')

                while not paciente.isalpha():
                    print('Error: el nombre debe contener letras solamente.')
                    paciente = input('Ingrese el nombre del paciente: ')

                if lunes1 == paciente:
                    lunes1 = ''
                    turnos_ocupados_lunes -= 1
                    print('Turno 1 del lunes cancelado exitosamente.')
                elif lunes2 == paciente:
                    lunes2 = ''
                    turnos_ocupados_lunes -= 1
                    print('Turno 2 del lunes cancelado exitosamente.')
                elif lunes3 == paciente:
                    lunes3 = ''
                    turnos_ocupados_lunes -= 1
                    print('Turno 3 del lunes cancelado exitosamente.')
                elif lunes4 == paciente:
                    lunes4 = ''
                    turnos_ocupados_lunes -= 1
                    print('Turno 4 del lunes cancelado exitosamente.')
                else:
                    print('Error: No hay turnos reservados del paciente para este día.')

                break

            elif dia == '2':
                paciente = input('Ingrese el nombre del paciente: ')

                while not paciente.isalpha():
                    print('Error: el nombre debe contener letras solamente.')
                    paciente = input('Ingrese el nombre del paciente: ')

                if martes1 == paciente:
                    martes1 = ''
                    turnos_ocupados_martes -= 1
                    print('Turno 1 del martes cancelado exitosamente.')
                elif martes2 == paciente:
                    martes2 = ''
                    turnos_ocupados_martes -= 1
                    print('Turno 2 del martes cancelado exitosamente.')
                elif martes3 == paciente:
                    martes3 = ''
                    turnos_ocupados_martes -= 1
                    print('Turno 3 del martes cancelado exitosamente.')
                else:
                    print('Error: No hay turnos reservados del paciente para este día.')

                break

            else:
                print('Error: seleccione un día correcto.')

    elif opcion == '3':
        dia = 0

        while dia != '1' and dia != '2':
            dia = input('Seleccione un día: 1)Lunes 2) Martes ')
            if dia == '1':
                if lunes1 == '':
                    print('Lunes turno 1: Libre')
                else:
                    print(f'Lunes turno 1: {lunes1}')

                if lunes2 == '':
                    print('Lunes turno 2: Libre')
                else:
                    print(f'Lunes turno 2: {lunes2}')

                if lunes3 == '':
                    print('Lunes turno 3: Libre')
                else:
                    print(f'Lunes turno 3: {lunes3}')

                if lunes4 == '':
                    print('Lunes turno 4: Libre')
                else:
                    print(f'Lunes turno 4: {lunes4}')

                break

            elif dia == '2':
                if martes1 == '':
                    print('Martes turno 1: Libre')
                else:
                    print(f'Martes turno 1: {martes1}')

                if martes2 == '':
                    print('Martes turno 2: Libre')
                else:
                    print(f'Martes turno 2: {martes2}')

                if martes3 == '':
                    print('Martes turno 3: Libre')
                else:
                    print(f'Martes turno 3: {martes3}')

                break

            else:
                print('Error: seleccione un día correcto.')

    elif opcion == '4':
        print('Resumen general:')

        if lunes1 == '':
            print('Lunes turno 1: Libre')
        else:
            print(f'Lunes turno 1: {lunes1}')

        if lunes2 == '':
            print('Lunes turno 2: Libre')
        else:
            print(f'Lunes turno 2: {lunes2}')

        if lunes3 == '':
            print('Lunes turno 3: Libre')
        else:
            print(f'Lunes turno 3: {lunes3}')

        if lunes4 == '':
            print('Lunes turno 4: Libre')
        else:
            print(f'Lunes turno 4: {lunes4}')

        if martes1 == '':
            print('Martes turno 1: Libre')
        else:
            print(f'Martes turno 1: {martes1}')

        if martes2 == '':
            print('Martes turno 2: Libre')
        else:
            print(f'Martes turno 2: {martes2}')

        if martes3 == '':
            print('Martes turno 3: Libre')
        else:
            print(f'Martes turno 3: {martes3}')

        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print('Día con más turnos ocupados: Lunes')
        elif turnos_ocupados_lunes < turnos_ocupados_martes:
            print('Día con más turnos ocupados: Martes')
        else:
            print('Día con más turnos ocupados: Empate')

    elif opcion == '5':
        print('Saliendo del sistema.')
        break
    else:
        print('Error: opción fuera de rango.')