def main():
    class Contacto():
        def __init__(self,nombre,telefono,email):
            self.nombre = nombre
            self.telefono = telefono
            self.email = email
        
        def mostrar_info(self):
            print(f"""
                Nombre del contacto = {self.nombre}  \n
                Telefono del contacto = {self.telefono} \n
                Email del contacto = {self.email}
                """)
            
        def actualizar_telefono(self,nuevo_telefono):
            self.telefono = nuevo_telefono
            
        def actualizar_email(self,nuevo_email):
            self.email = nuevo_email
            
    agenda = []

    def agregar_contacto():
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = int(input("Ingrese el numero del contacto: "))
        email = input("Ingrese el email del contacto: ")
        contacto = Contacto(nombre,telefono,email)
        agenda.append(contacto)
        
    def mostrar_contacto():
        if not agenda:
            print("Error, la agenda esta vacia")
        for i, contacto in enumerate(agenda):
            print(f"Contacto {i + 1}")
            contacto.mostrar_info()
            
    def actualizar_contacto():
        indiceAgenda = int(input("¿Que numero de contacto desea modificar?: ")) - 1
        if indiceAgenda >= 0 and indiceAgenda < len(agenda):
            opcActualizar = input("¿Que desea actualizar? (Telefono/Email): ").lower()
            if opcActualizar == "telefono":
                nuevo_telefono = int(input("Ingrese el nuevo telefono: "))
                agenda[indiceAgenda].actualizar_telefono(nuevo_telefono)
                print("Telefono actualizado")
            elif opcActualizar == "email":
                nuevo_email = input("Ingrese el nuevo email: ")
                agenda[indiceAgenda].actualizar_email(nuevo_email)
                print("Email actualizado")
            else:
                print("Opcion no valida")
        else:
            print("Error, no existe ese numero de contacto.")    
            
    def borrar_contacto():
        indiceAgenda = int(input("¿Que numero de contacto desea eliminar?: ")) - 1
        if indiceAgenda >= 0 and indiceAgenda < len(agenda):
            agenda.pop(indiceAgenda)
            print("Contacto eliminado")
        else:
            print("Error, no hay ningun contacto en ese numero")
        
    while True:
        
        print("\nAgenda de Contactos")
        print("1. Añadir nuevo contacto")
        print("2. Mostrar todos los contactos")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            mostrar_contacto()
        elif opcion == 3:
            actualizar_contacto()
        elif opcion == 4:
            borrar_contacto()
        elif opcion == 5:
            print("Saliendo de la agenda de contactos.")
            break
        else:
            print("Opcion no valida, por favor seleccione una opción del 1 al 5.")
        
if __name__ == "__main__":
    main()