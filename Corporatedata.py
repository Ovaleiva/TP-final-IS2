from singleton_meta import SingletonMeta
from decimal import Decimal

class CorporateData(metaclass=SingletonMeta):
    """Clase que maneja los datos corporativos con implementación Singleton."""
    
    def __init__(self):
        self.data = {
            'Sede': "FCyT",
            'Domicilio': "25 de Mayo 385",
            'Localidad': "Concepción del Uruguay",
            'CodigoPostal': "3260",
            'Provincia': "Entre Rios",
            'CUIT': "30-70925411-8",
            'idSeq': Decimal('123'),
            'idReq': Decimal('83'),
            'Telefono': "03442 43-1442",
            'ID': "UADER-FCyT-IS2",
            'Web': "http://www.uader.edu.ar"
        }

    def getData(self, uuid, id_sede):
        """Retorna los datos de una sede específica en formato diccionario."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not isinstance(id_sede, int) or id_sede <= 0:
            raise ValueError("El ID de la sede debe ser un número entero positivo.")
        
        return {
            'ID': self.data['ID'],
            'Domicilio': self.data['Domicilio'],
            'Localidad': self.data['Localidad'],
            'CodigoPostal': self.data['CodigoPostal'],
            'Provincia': self.data['Provincia'],
            'Telefono': self.data['Telefono'],
            'Web': self.data['Web']
        }

    def getCUIT(self, uuid, id_sede):
        """Retorna el CUIT de una sede específica."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not isinstance(id_sede, int) or id_sede <= 0:
            raise ValueError("El ID de la sede debe ser un número entero positivo.")
        
        return {'idSede': id_sede, 'CUIT': self.data['CUIT']}

    def getSeqID(self, uuid, id_sede):
        """Incrementa y retorna el ID de secuencia para una sede específica."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not isinstance(id_sede, int) or id_sede <= 0:
            raise ValueError("El ID de la sede debe ser un número entero positivo.")
        
        self.data['idSeq'] += 1
        return {'idSede': id_sede, 'seqID': self.data['idSeq']}
