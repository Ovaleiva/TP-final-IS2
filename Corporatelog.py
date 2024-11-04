import uuid
from datetime import datetime
from singleton_meta import SingletonMeta

class CorporateLog(metaclass=SingletonMeta):
    """Clase que maneja los registros (logs) de acciones con implementación Singleton."""
    
    def __init__(self):
        self.logs = []
        self.uuidCPU = uuid.getnode()

    def post(self, uuid, action):
        """Registra un log de la acción con un timestamp."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not action or not isinstance(action, str):
            raise ValueError("La acción debe ser una cadena no vacía.")
        
        timestamp = datetime.now()
        log_entry = {
            'uuid': uuid,
            'uuidCPU': self.uuidCPU,
            'action': action,
            'timestamp': timestamp,
            'status': 'OK'
        }
        self.logs.append(log_entry)
        print(f"Log registrado: {log_entry}")
        return log_entry

    def list(self, uuidCPU, uuid=None):
        """Lista los logs asociados a un uuidCPU, opcionalmente filtrados por uuid de sesión."""
        if not isinstance(uuidCPU, int) or uuidCPU <= 0:
            raise ValueError("El UUID de la CPU debe ser un número entero positivo.")
        
        filtered_logs = [log for log in self.logs if log['uuidCPU'] == uuidCPU]
        if uuid:
            filtered_logs = [log for log in filtered_logs if log['uuid'] == uuid]

        print(f"Logs encontrados: {filtered_logs}")
        return filtered_logs
