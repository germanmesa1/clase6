import datetime

class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
        self.__medicamentos = []  # Lista para almacenar medicamentos
        
    # Métodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    def verMedicamentos(self):
        return self.__medicamentos 
    
    # Métodos set
    def asignarNombre(self, n):
        self.__nombre = n 
    def asignarCedula(self, c):
        self.__cedula = c 
    def asignarGenero(self, g):
        self.__genero = g 
    def asignarServicio(self, s):
        self.__servicio = s 
    
    def agregarMedicamento(self, medicamento):
        if medicamento in self.__medicamentos:
            print("Este medicamento ya está registrado.")
        else:
            self.__medicamentos.append(medicamento)
    
    def eliminarMedicamento(self, medicamento):
        if medicamento in self.__medicamentos:
            self.__medicamentos.remove(medicamento)
            print("Medicamento eliminado correctamente.")
        else:
            print("El medicamento no está en la lista.")
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        self.__caninos = {}
        self.__felinos = {}
        
    def verificarPaciente(self, cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False
    
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, c):
        if not self.verificarPaciente(c):
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 
    
    def validarFecha(self, fecha):
        try:
            datetime.datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            return False

def main():
    sis = Sistema() 
    while True:
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente, \n3 agregar medicamento, \n4 eliminar medicamento\n\t--> ")) 
        
        if opcion == 1:
            print("A continuación se solicitarán los datos ...") 
            cedula = int(input("Ingrese la cédula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cédula >>".upper()) 
            else:    
                pac = Paciente() 
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el género: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            c = int(input("Ingrese la cédula a buscar: ")) 
            p = sis.verDatosPaciente(c) 
            if p:
                print("Nombre: " + p.verNombre()) 
                print("Cédula: " + str(p.verCedula())) 
                print("Género: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
                print("Medicamentos: " + ", ".join(p.verMedicamentos()) if p.verMedicamentos() else "Sin medicamentos")
            else:
                print("No existe un paciente con esa cédula") 
        elif opcion == 3:
            c = int(input("Ingrese la cédula del paciente: "))
            p = sis.verDatosPaciente(c)
            if p:
                medicamento = input("Ingrese el nombre del medicamento: ")
                p.agregarMedicamento(medicamento)
            else:
                print("Paciente no encontrado.")
        elif opcion == 4:
            c = int(input("Ingrese la cédula del paciente: "))
            p = sis.verDatosPaciente(c)
            if p:
                medicamento = input("Ingrese el nombre del medicamento a eliminar: ")
                p.eliminarMedicamento(medicamento)
            else:
                print("Paciente no encontrado.")
        elif opcion != 0:
            continue 
        else:
            break 

if __name__ == "__main__":
    main()

        
        
        
        
        
        
        
