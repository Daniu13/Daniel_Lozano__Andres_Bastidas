"Hallo"
import datetime

class Implante:
    def __init__(self) -> None:
        self.__fecha_implantacion = None
        self.__medico = None
        self.__estado = None
        self.__fecha_revision = None
        self.__fecha_mantenimiento = None

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

class Paciente:
    def __init__(self) -> None:
        self.__id = None
        self.__implantes = set()

    def ver_id(self):
        return self.__id
    def ver_implantes(self):
        return self.__implantes
    def set_id(self, id):
        self.__id = id
    def agregar_implante(self, implante):
        if self.verificar_implante(implante):
            self.__implantes.add(implante)
            return True
        return False
    def eliminar_implante(self, implante):
        if self.verificar_implante(implante):
            self.__implantes.discard(implante)
            return True
        return False
    def verificar_implante(self, implante):
        if implante in self.__implantes:
            return True
        return False

class Marcapasos(Implante):
    def __init__(self) -> None:
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
    def añadir_paciente(self, paciente):
        if not self.verificar_paciente(paciente):
            self.__inventario[paciente] = paciente.ver_implantes()
    def eliminar_paciente(self, paciente):
        if self.verificar_paciente(paciente):
            self.__inventario.pop(paciente)
    def ver_inventario(self):
        conjuntos_implantes = [paciente.ver_implantes() for paciente in self.__inventario.values()]
        lista_implantes = [implante for implantes in conjuntos_implantes for implante in implantes]
        return lista_implantes
        # lista_implantes = []
        # for implantes in conjuntos_implantes:
        #     for implante in implantes:
        #         lista_implantes.append(implante)
                
def main():
    pass

if __name__ == '__main__':
    main()