import uuid 
from Corporatedata import CorporateData
from Corporatelog import CorporateLog
import pprint
from decimal import Decimal

def pretty_print(data, title):
    """Imprime los datos en un formato legible."""
    print(f"{title}:")
    print("{")
    for key, value in data.items():
        print(f"    '{key}': '{value}',")
    print("}\n")

def pretty_print_log(logs):
    """Imprime la lista de logs en un formato legible."""
    print("Logs registrados:")
    for index, log in enumerate(logs, start=1):
        print(f"{index}. {{")
        for key, value in log.items():
            print(f"        '{key}': '{value}',")
        print("    }")
    print() 

if __name__ == "__main__":
    corporate_data = CorporateData()
    corporate_log = CorporateLog()

    uuid_session = str(uuid.uuid4())
    id_sede = 1

    data = corporate_data.getData(uuid_session, id_sede)
    pretty_print(data, "Datos de la sede")

    cuit = corporate_data.getCUIT(uuid_session, id_sede)
    pretty_print(cuit, "CUIT de la sede")

    seq_id = corporate_data.getSeqID(uuid_session, id_sede)
    pretty_print(seq_id, "ID de secuencia de la sede")

    corporate_log.post(uuid_session, "getData")
    corporate_log.post(uuid_session, "getCUIT")
    corporate_log.post(uuid_session, "getSeqID")

    log_list = corporate_log.list(corporate_log.uuidCPU)
    pretty_print_log(log_list)
