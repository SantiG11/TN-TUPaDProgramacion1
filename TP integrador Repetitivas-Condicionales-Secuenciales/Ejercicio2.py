usuario_correcto = 'alumno'
clave_correcta = 'python123'
intentos = 3
intento = 0
acceso_concedido = False

while intento < intentos:
    print(f'Intento {intento + 1}/{intentos}')
    usuario_ingresado = input('Ingrese su nombre de usuario: ')
    clave_ingresada = input('Ingrese su clave: ')
    intento += 1

    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print('Acceso concedido.')
        acceso_concedido = True
        opcion = ''

        while opcion != '4':
            print('1) Ver estado de inscripción 2) Cambiar clave 3) Mensaje 4) Salir')
            opcion = input('Seleccione una opción: ')

            while not opcion.isdigit() or opcion not in ('1', '2', '3', '4'):
                print('Error: opción inválida.')
                opcion = input('Seleccione una opción: ')

            if opcion == '1':
                print('Inscripto.')

            elif opcion == '2':
                clave_cambiada = False

                while not clave_cambiada:
                    nueva_clave = input('Ingrese la nueva clave: ')

                    if len(nueva_clave) < 6:
                        print('Error: ingrese una clave con al menos 6 caracteres.')
                    else:
                        confirmacion_clave = input('Confirme la nueva clave: ')

                        if nueva_clave == confirmacion_clave:
                            print('Clave cambiada con éxito.')
                            clave_correcta = nueva_clave
                            clave_cambiada = True
                        else:
                            print('Error: la nueva clave y la confirmación no coinciden. Intente de nuevo.')

            elif opcion == '3':
                print('El esfuerzo de hoy es el primer paso hacia tus metas.')

            elif opcion == '4':
                print('Saliendo.')

        break

    else:
        print('Credenciales inválidas.')

if not acceso_concedido and intento >= intentos:
    print('Cuenta bloqueada.')