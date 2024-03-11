"Hallo"
import datetime


class Implante:
    def __init__(self) -> None:
        self.__fecha_implantacion = None
        self.__medico = None
        self.__estado = None
        self.__fecha_revision = None
        self.__fecha_mantenimiento = None
        self.__id_implante = None

    def ver_fecha_implantacion(self):
        return self.__fecha_implantacion

    def ver_medico(self):
        return self.__medico

    def ver_estado(self):
        return self.__estado

    def ver_fecha_revision(self):
        return self.__fecha_revision

    def ver_fecha_mantenimiento(self):
        return self.__fecha_mantenimiento
    
    def ver_id_implante(self):
        return self.__id_implante

    def set_fecha_implantacion(self, fecha):
        self.__fecha_implantacion = fecha

    def set_medico(self, medico):
        self.__medico = medico

    def set_estado(self, estado):
        self.__estado = estado

    def set_fecha_revision(self, fecha):
        self.__fecha_revision = fecha

    def set_fecha_mantenimiento(self, fecha):
        self.__fecha_mantenimiento = fecha

    def set_id_implante(self, id):
        self.__id_implante = id


class Paciente:
    def __init__(self) -> None:
        self.__id = None
        self.__implantes = dict()

    def ver_id(self):
        return self.__id

    def ver_implantes(self):
        return self.__implantes

    def set_id(self, id):
        self.__id = id

    def agregar_implante(self, implante):
        if not self.verificar_implante(implante):
            # self.__implantes.add(implante)
            self.__implantes[implante.ver_id_implante()] = implante
            return True
        return False

    def eliminar_implante(self, implante):
        if self.verificar_implante(implante):
            self.__implantes.pop(implante.ver_id_implante())
            return True
        return False

    def verificar_implante(self, implante):
        if implante.ver_id_implante() in self.__implantes:
            return True
        return False


class Marcapasos(Implante):
    def __init__(self) -> None:
        super().__init__()
        self.__num_electrodos = None
        self.__es_inalambrico = None
        self.__frecuencia_estimulacion = None

    def ver_num_eletrodos(self):
        return self.__num_electrodos

    def ver_es_alambrico(self):
        return self.__es_inalambrico

    def ver_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion

    def set_num_eletrodos(self, num):
        self.__num_electrodos = num

    def set_es_alambrico(self, es):
        self.__es_inalambrico = es

    def set_frecuencia_estimulacion(self, frecuencia):
        self.__frecuencia_estimulacion = frecuencia


class StentCoronario(Implante):
    def __init__(self) -> None:
        super().__init__()
        self.__longitud = None
        self.__diametro = None
        self.__material = None

    def ver_longitud(self):
        return self.__longitud

    def ver_diametro(self):
        return self.__diametro

    def ver_material(self):
        return self.__material

    def set_longitud(self, longitud):
        self.__longitud = longitud

    def set_diametro(self, diametro):
        self.__diametro = diametro

    def set_material(self, material):
        self.__material = material


class ImplanteDental(Implante):
    def __init__(self) -> None:
        super().__init__()
        self.__forma = None
        self.__sistema_fijacion = None
        self.__material = None

    def ver_forma(self):
        return self.__forma

    def ver_sistema_fijacion(self):
        return self.__sistema_fijacion

    def ver_material(self):
        return self.__material

    def set_forma(self, forma):
        self.__forma = forma

    def set_sistema_fijacion(self, fijacion):
        self.__sistema_fijacion = fijacion

    def set_material(self, material):
        self.__material = material


class ImplanteCadera(Implante):
    def __init__(self) -> None:
        super().__init__()
        self.__forma = None
        self.__sistema_fijacion = None
        self.__material = None

    def ver_forma(self):
        return self.__forma

    def ver_sistema_fijacion(self):
        return self.__sistema_fijacion

    def ver_material(self):
        return self.__material

    def set_forma(self, forma):
        self.__forma = forma

    def set_sistema_fijacion(self, fijacion):
        self.__sistema_fijacion = fijacion

    def set_material(self, material):
        self.__material = material


class ImplanteRodilla(Implante):
    def __init__(self) -> None:
        super().__init__()
        self.__material = None
        self.__tipo_fijacion = None
        self.__tamaño = None

    def ver_material(self):
        return self.__material

    def ver_tipo_fijacion(self):
        return self.__tipo_fijacion

    def ver_tamaño(self):
        return self.__tamaño

    def set_material(self, material):
        self.__material = material

    def set_tipo_fijacion(self, tipo):
        self.__tipo_fijacion = tipo

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño


class Sistema:
    def __init__(self) -> None:
        self.__inventario = dict()

    def verificar_paciente(self, paciente):
        if paciente in self.__inventario:
            return True
        return False

    def verificar_implante(self, id_implante):
        for paciente in self.__inventario.values():
            for implante in paciente.ver_implantes().values():
                if implante.ver_id_implante() == id_implante:
                    return True
        return False

    def añadir_paciente(self, paciente):
        if not self.verificar_paciente(paciente):
            self.__inventario[paciente] = paciente.ver_implantes()

    def eliminar_paciente(self, paciente):
        if self.verificar_paciente(paciente):
            self.__inventario.pop(paciente)

    def ver_inventario(self):
        lista_implantes = [
            implante for implantes in self.__inventario.values() for implante in implantes.values()
            ]
        return lista_implantes
        # lista_implantes = []
        # for implantes in conjuntos_implantes:
        #     for implante in implantes:
        #         lista_implantes.append(implante)

def main():
    sistemita = Sistema()
    while True:
        menu = int(input(
                """\nIngrese una opción: 
                       \n1- Ingresar implante 
                       \n2- Eliminar implante 
                       \n3- Editar implante 
                       \n4- Visualizar inventario
                       \n5- Salir 
                       \nUsted ingresó la opción: """))
        if menu == 1:
            paciente = Paciente()
            id_paciente = int(input("ID del paciente: "))
            paciente.set_id(id_paciente)
            que_tipo_implante = int(input(
                """\nElija el tipo de implante:
                        \n1- Marcapasos
                        \n2- Stent coronario
                        \n3- Implante de rodilla
                        \n4- Implante dental
                        \n5- Implante de cadera
                        \nOpción: """))
            fecha_implantacion = input("Fecha de implantación: ")
            medico = input("Médico: ")
            estado = input("Estado del implante: ")
            fecha_revision = input("Fecha de revisión: ")
            fecha_mantenimiento = input("Fecha de mantenimiento: ")
            if que_tipo_implante == 1:
                num_electrodos = int(input("Número de electrodos: "))
                es_alambrico = int(input("1- Alámbrico\n0- Inalámbrico\nElija una opción: "))
                frecuencia_estimulacion = float(input("Frecuencia de estimulación: "))
                marcapasos = Marcapasos()
                marcapasos.set_fecha_implantacion(fecha_implantacion)
                marcapasos.set_medico(medico)
                marcapasos.set_estado(estado)
                marcapasos.set_fecha_revision(fecha_revision)
                marcapasos.set_fecha_mantenimiento(fecha_mantenimiento)
                marcapasos.set_num_eletrodos(num_electrodos)
                marcapasos.set_es_alambrico(es_alambrico)
                marcapasos.set_frecuencia_estimulacion(frecuencia_estimulacion)
                paciente.agregar_implante(marcapasos)
                sistemita.añadir_paciente(paciente)
            elif que_tipo_implante == 2:
                longitud = float(input("Longitud: "))
                diametro = float(input("Diámetro: "))
                material = input("Material: ")
                stent_coronario = StentCoronario()
                stent_coronario.set_fecha_implantacion(fecha_implantacion)
                stent_coronario.set_medico(medico)
                stent_coronario.set_estado(estado)
                stent_coronario.set_fecha_revision(fecha_revision)
                stent_coronario.set_fecha_mantenimiento(fecha_mantenimiento)
                stent_coronario.set_longitud(longitud)
                stent_coronario.set_diametro(diametro)
                stent_coronario.set_material(material)
                paciente.agregar_implante(stent_coronario)
                sistemita.añadir_paciente(paciente)
            elif que_tipo_implante == 3:
                material = input("Material: ")
                tipo_fijacion = input("Tipo de fijación: ")
                tamaño = float(input("Tamaño: "))
                implante_rodilla = ImplanteRodilla()
                implante_rodilla.set_fecha_implantacion(fecha_implantacion)
                implante_rodilla.set_medico(medico)
                implante_rodilla.set_estado(estado)
                implante_rodilla.set_fecha_revision(fecha_revision)
                implante_rodilla.set_fecha_mantenimiento(fecha_mantenimiento)
                implante_rodilla.set_tipo_fijacion(tipo_fijacion)
                implante_rodilla.set_tamaño(tamaño)
                paciente.agregar_implante(implante_rodilla)
                sistemita.añadir_paciente(paciente)
            elif que_tipo_implante == 4 or que_tipo_implante == 5:
                forma = input("Forma: ")
                sistema_fijacion = input("Sistema de fijación: ")
                material = input("Material: ")
                if que_tipo_implante == 4:
                    implante_dental = ImplanteDental()
                    implante_dental.set_fecha_implantacion(fecha_implantacion)
                    implante_dental.set_medico(medico)
                    implante_dental.set_estado(estado)
                    implante_dental.set_fecha_revision(fecha_revision)
                    implante_dental.set_fecha_mantenimiento(fecha_mantenimiento)
                    implante_dental.set_forma(forma)
                    implante_dental.set_sistema_fijacion(sistema_fijacion)
                    implante_dental.set_material(material)
                    paciente.agregar_implante(implante_dental)
                    sistemita.añadir_paciente(paciente)
                else:
                    implante_cadera = ImplanteCadera()
                    implante_cadera.set_fecha_implantacion(fecha_implantacion)
                    implante_cadera.set_medico(medico)
                    implante_cadera.set_estado(estado)
                    implante_cadera.set_fecha_revision(fecha_revision)
                    implante_cadera.set_fecha_mantenimiento(fecha_mantenimiento)
                    implante_dental.set_forma(forma)
                    implante_dental.set_sistema_fijacion(sistema_fijacion)
                    implante_dental.set_material(material)
                    paciente.agregar_implante(implante_dental)
                    sistemita.añadir_paciente(paciente)
            else:
                print("Opción no válida")
                continue
        elif menu == 2:
            id_implante = int(input("ID del implante: "))
            if sistemita.verificar_implante(id_implante):
                pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo")


if __name__ == "__main__":
    main()
