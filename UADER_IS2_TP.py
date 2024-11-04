import boto3
import uuid
import platform
from datetime import datetime
from decimal import Decimal 


dynamodb = boto3.resource('dynamodb')
corporate_data_table = dynamodb.Table('CorporateData')
corporate_log_table = dynamodb.Table('CorporateLog')

uniqueID = str(uuid.uuid4())         
CPUid = str(uuid.getnode())       
sessionid = str(uuid.uuid4())      
timestamp = datetime.now().isoformat() 

domicilio = "25 de Mayo 385"
localidad = "Concepcion del Uruguay"
codigoPostal = "3260"
provincia = "Entre Ríos"
telefono = "03442 43-1442"
web = "http://www.uader.edu.ar"
sede = "FCyT"
idSeq = Decimal('124') 
metodo = "POST"

data_response = corporate_data_table.put_item(
    Item={
        'sessionID': sessionid,
        'cpuID': CPUid,
        'id': uniqueID,
        'domicilio': domicilio,
        'localidad': localidad,
        'codigoPostal': codigoPostal,
        'provincia': provincia,
        'telefono': telefono,
        'web': web,
        'sede': sede,
        'idSeq': idSeq
    }
)

print("Registro en CorporateData:")
print(f"sessionID: {sessionid}, cpuID: {CPUid}, id: {uniqueID}, domicilio: {domicilio}, localidad: {localidad}, codigoPostal: {codigoPostal}, provincia: {provincia}")
print("Código de estado de la inserción en CorporateData:", data_response['ResponseMetadata']['HTTPStatusCode'])

log_response = corporate_log_table.put_item(
    Item={
        'id': uniqueID,       
        'sessionID': sessionid,
        'cpuID': CPUid,
        'timeStamp': timestamp,
        'metodo': metodo
    }
)

print("\nRegistro en CorporateLog:")
print(f"id: {uniqueID}, sessionID: {sessionid}, cpuID: {CPUid}, timeStamp: {timestamp}, metodo: {metodo}")
print("Código de estado de la inserción en CorporateLog:", log_response['ResponseMetadata']['HTTPStatusCode'])
