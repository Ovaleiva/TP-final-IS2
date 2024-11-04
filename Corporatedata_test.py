import unittest
from Corporatedata import CorporateData 
class Corporatedata_test(unittest.TestCase):

    def setUp(self):
        """Configura una nueva instancia de CorporateData para cada prueba."""
        self.corporate_data = CorporateData()

    def test_singleton_corporate_data(self):
        """Verifica que CorporateData se implemente como un Singleton."""
        instance1 = CorporateData()
        instance2 = CorporateData()
        self.assertIs(instance1, instance2, "CorporateData no se comporta como un Singleton.")

    def test_get_data_success(self):
        """Prueba de recuperación de datos exitoso."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"  # UUID válido
        id_sede = 1
        data = self.corporate_data.getData(uuid_session, id_sede)
        self.assertEqual(data['ID'], self.corporate_data.data['ID'])
        self.assertEqual(data['Domicilio'], self.corporate_data.data['Domicilio'])

    def test_get_data_with_invalid_uuid(self):
        """Prueba de recuperación de datos con UUID inválido."""
        with self.assertRaises(ValueError) as context:
            self.corporate_data.getData("", 1)
        self.assertEqual(str(context.exception), "UUID no es válido o está ausente.")

    def test_get_data_with_invalid_id_sede(self):
        """Prueba de recuperación de datos con ID de sede inválido."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        with self.assertRaises(ValueError) as context:
            self.corporate_data.getData(uuid_session, 0)  # ID de sede inválido
        self.assertEqual(str(context.exception), "El ID de la sede debe ser un número entero positivo.")

    def test_get_cuit_success(self):
        """Prueba de recuperación del CUIT exitoso."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        id_sede = 1
        cuit = self.corporate_data.getCUIT(uuid_session, id_sede)
        self.assertEqual(cuit['CUIT'], self.corporate_data.data['CUIT'])

    def test_get_cuit_with_invalid_uuid(self):
        """Prueba de recuperación del CUIT con UUID inválido."""
        with self.assertRaises(ValueError) as context:
            self.corporate_data.getCUIT("", 1)
        self.assertEqual(str(context.exception), "UUID no es válido o está ausente.")

    def test_get_cuit_with_invalid_id_sede(self):
        """Prueba de recuperación del CUIT con ID de sede inválido."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        with self.assertRaises(ValueError) as context:
            self.corporate_data.getCUIT(uuid_session, 0)  # ID de sede inválido
        self.assertEqual(str(context.exception), "El ID de la sede debe ser un número entero positivo.")

    def test_get_seq_id_success(self):
        """Prueba de incremento y recuperación del ID de secuencia exitoso."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        id_sede = 1
        seq_id = self.corporate_data.getSeqID(uuid_session, id_sede)
        self.assertEqual(seq_id['seqID'], self.corporate_data.data['idSeq'])

    def test_get_seq_id_with_invalid_uuid(self):
        """Prueba de recuperación del ID de secuencia con UUID inválido."""
        with self.assertRaises(ValueError) as context:
            self.corporate_data.getSeqID("", 1)
        self.assertEqual(str(context.exception), "UUID no es válido o está ausente.")

    def test_get_seq_id_with_invalid_id_sede(self):
        """Prueba de recuperación del ID de secuencia con ID de sede inválido."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        with self.assertRaises(ValueError) as context:
            self.corporate_data.getSeqID(uuid_session, 0)  # ID de sede inválido
        self.assertEqual(str(context.exception), "El ID de la sede debe ser un número entero positivo.")


if __name__ == "__main__":
    unittest.main()