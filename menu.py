from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion !=5:
        print('''
        1. Listar usuarios
        2. Agreagar usuarios
        3. Actualizar usuarios
        4. Eliminar usuarios
        5. Salir del programa
        ''')      
        opcion = int(input('Ingresa tu opcion (1-5): '))
        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios: 
                log.info(usuario)
        elif opcion == 2:
            usernameVar = input('Escribe el username: ')
            passwordVar = input('Escribe el password: ')
            usuario = Usuario(username=usernameVar, password=passwordVar)
            usuariosInsertados = UsuarioDAO.insertar(usuario)
            log.info(f'Usuarios insertados: {usuariosInsertados}')
        elif opcion ==3:
            id_usuario_var = int(input('Ingrese el Id de usurio a modificar: '))
            usernameVar = input('Escribe el nuevo Username: ')
            passwordVar = input('Escribe el nuevo password a modificar: ')
            usuario = Usuario(id_usuario_var, usernameVar, passwordVar)
            usuariosActualizados = UsuarioDAO.actualizar(usuario)
            log.info(f'Usuarios actualizados {usuariosActualizados}')
        elif opcion == 4:
            id_usuario_var= int(input('Ingrese el id de Usuario a eliminar: '))
            usuario = Usuario(id_usuario=id_usuario_var)
            usuariosEliminados = UsuarioDAO.eliminar(usuario)
            log.info(f'Usuario eliminado {usuariosEliminados}')
else:
    log.info('Salimos de la aplicación...')