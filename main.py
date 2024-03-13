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

    def agregar_implante(self, implante_id):
        if not self.verificar_implante(implante_id):
            # self.__implantes.add(implante)
            self.__implantes[implante_id.ver_id_implante()] = implante_id
            return True
        return False

    def eliminar_implante(self, implante_id):
        if self.verificar_implante(implante_id):
            self.__implantes.pop(implante_id.ver_id_implante())
            return True
        return False

    def verificar_implante(self, implante_id):
        if implante_id in self.__implantes:
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

    def verificar_paciente(self, paciente_id):
        if paciente_id in self.__inventario:
            return True
        return False

    def verificar_implante(self, implante_id):
        for paciente in self.__inventario.values():
            if implante_id in paciente.ver_implantes():
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
            (paciente, implante)
            for paciente, implantes in self.__inventario.items()
            for implante in implantes.values()
        ]
        return lista_implantes
        # lista_implantes = []
        # for implantes in conjuntos_implantes:
        #     for implante in implantes:
        #         lista_implantes.append(implante)

def validacion(mensaje, tipo_dato):
    while True:
        entrada = input(mensaje)
        try:
            valor_validado = tipo_dato(entrada)
            return valor_validado
        except ValueError:
            print(f"Error: Por favor, ingresa un valor válido de tipo {tipo_dato.__name__}.")

def main():
    sistemita = Sistema()
    while True:
        menu = validacion(
            """\nIngrese una opción: 
                       \n1- Ingresar implante 
                       \n2- Eliminar implante 
                       \n3- Editar implante 
                       \n4- Visualizar inventario
                       \n5- Salir 
                       \nUsted ingresó la opción: """,
            int
        )
        if menu == 1:
            paciente = Paciente()
            id_paciente = validacion("ID del paciente: ", int)
            paciente.set_id(id_paciente)
            que_tipo_implante = validacion(
                """\nElija el tipo de implante:
                        \n1- Marcapasos
                        \n2- Stent coronario
                        \n3- Implante de rodilla
                        \n4- Implante dental
                        \n5- Implante de cadera
                        \nOpción: """,
                int
            )
            fecha_implantacion = input("Fecha de implantación: ")
            medico = input("Médico: ")
            estado = input("Estado del implante: ")
            fecha_revision = input("Fecha de revisión: ")
            fecha_mantenimiento = input("Fecha de mantenimiento: ")
            id_implante = int(input("ID del implante: "))
            if que_tipo_implante == 1:
                num_electrodos = validacion("Número de electrodos: ", int)
                es_alambrico = validacion(
                    "1- Alámbrico\n0- Inalámbrico\nElija una opción: ",
                    int
                )
                frecuencia_estimulacion = validacion("Frecuencia de estimulación: ", float)
                marcapasos = Marcapasos()
                marcapasos.set_fecha_implantacion(fecha_implantacion)
                marcapasos.set_medico(medico)
                marcapasos.set_estado(estado)
                marcapasos.set_fecha_revision(fecha_revision)
                marcapasos.set_fecha_mantenimiento(fecha_mantenimiento)
                marcapasos.set_id_implante(id_implante)
                marcapasos.set_num_eletrodos(num_electrodos)
                marcapasos.set_es_alambrico(es_alambrico)
                marcapasos.set_frecuencia_estimulacion(frecuencia_estimulacion)
                paciente.agregar_implante(marcapasos)
                sistemita.añadir_paciente(paciente)
            elif que_tipo_implante == 2:
                longitud = validacion("Longitud: ", float)
                diametro = validacion("Diámetro: ", float)
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
                tamaño = validacion("Tamaño: ", float)
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
                    implante_cadera.set_forma(forma)
                    implante_cadera.set_sistema_fijacion(sistema_fijacion)
                    implante_cadera.set_material(material)
                    paciente.agregar_implante(implante_dental)
                    sistemita.añadir_paciente(paciente)
            else:
                print("Opción no válida")
                continue
        elif menu == 2:
            id_implante = validacion("ID del implante: ", int)
            for paciente, implante in sistemita.ver_inventario():
                if implante.ver_id_implante() == id_implante:
                    if paciente.eliminar_implante(implante):
                        print("Implante eliminado exitosamente.")
                    else:
                        print("No se encontró tal implante.")
        elif menu == 3:
            id_implante = validacion("ID del implante: ", int)
            if sistemita.verificar_implante(id_implante):
                for paciente, implante in sistemita.ver_inventario():
                    if implante.ver_id_implante() == id_implante:
                        new_fecha_implantacion = input("Nueva fecha de implantación: ")
                        new_medico = input("Nuevo médico: ")
                        new_estado = input("Nuevo estado del implante: ")
                        new_fecha_revision = input("Nueva fecha de revisión: ")
                        new_fecha_mantenimiento = input(
                            "Nueva fecha de mantenimiento: "
                        )
                        #El ID del implante es no editable
                        implante.set_fecha_implantacion(new_fecha_implantacion)
                        implante.set_medico(new_medico)
                        implante.set_estado(new_estado)
                        implante.set_fecha_revision(new_fecha_revision)
                        implante.set_fecha_mantenimiento(new_fecha_mantenimiento)
                        if isinstance(implante, Marcapasos):
                            new_numero_electrodos = validacion("Nuevo número de electrodos: ", int)
                            new_es_alambrico = validacion("¿Es alámbrico? (1: Sí, 0: No): ", int)
                            new_frecuencia_estimulacion = validacion("Nueva frecuencia de estimulación: ", float)
                            implante.set_num_eletrodos(new_numero_electrodos)
                            implante.set_es_alambrico(new_es_alambrico)
                            implante.set_frecuencia_estimulacion(
                                new_frecuencia_estimulacion
                            )
                            print("Editado exitosamente.")
                        elif isinstance(implante, StentCoronario):
                            new_longitud = validacion("Nueva longitud: ", float)
                            new_diametro = validacion("Nuevo diametro: ", float)
                            new_material = input("Nuevo material: ")
                            implante.set_longitud(new_longitud)
                            implante.set_diametro(new_diametro)
                            implante.set_material(new_material)
                            print("Editado exitosamente.")
                        elif isinstance(implante, ImplanteRodilla):
                            new_material = input("Nuevo material: ")
                            new_tipo_fijacion = input("Nuevo tipo de fijación: ")
                            new_tamaño = validacion("Nuevo tamaño: ", float)
                            implante.set_material(new_material)
                            implante.set_tipo_fijacion(new_tipo_fijacion)
                            implante.set_tamaño(new_tamaño)
                            print("Editado exitosamente.")
                        elif isinstance(implante, ImplanteDental) or isinstance(
                            implante, ImplanteCadera
                        ):
                            new_forma = input("Nueva forma: ")
                            new_sistema_fijacion = input("Nuevo sistema de fijación: ")
                            new_material = input("Nuevo material: ")
                            implante.set_forma(new_forma)
                            implante.set_sistema_fijacion(new_sistema_fijacion)
                            implante.set_material(new_material)
                    else:
                        print("No se encontró el implante con el ID especificado.")
        elif menu == 4:
            for implante in sistemita.ver_inventario():
                print("Lista de implantes: \n")
                print(f'ID: {implante[1].ver_id_implante()}')
                if isinstance(implante[1], Marcapasos):
                    print("Tipo: Marcapasos\n\n")
                elif isinstance(implante[1], StentCoronario):
                    print("Tipo: Stent coronario\n\n")
                elif isinstance(implante[1], ImplanteDental):
                    print("Tipo: Implante dental\n\n")
                elif isinstance(implante[1], ImplanteCadera):
                    print("Tipo: Implante de cadera\n\n")
                elif isinstance(implante[1], ImplanteRodilla):
                    print("Tipo: Implante de rodilla\n\n")
        elif menu == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo")


if __name__ == "__main__":
    main()
