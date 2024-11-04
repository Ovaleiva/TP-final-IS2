import unittest
from Corporatelog import CorporateLog
class Corporatelog_test(unittest.TestCase):

    def setUp(self):
        """Configura una nueva instancia de CorporateLog para cada prueba."""
        self.corporate_log = CorporateLog()

    def test_singleton_corporate_log(self):
        """Verifica que CorporateLog se implemente como un Singleton."""
        instance1 = CorporateLog()
        instance2 = CorporateLog()
        self.assertIs(instance1, instance2, "CorporateLog no se comporta como un Singleton.")

    def test_post_log_success(self):
        """Prueba de registro de log exitoso."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        action = "Test Action"
        log_entry = self.corporate_log.post(uuid_session, action)
        self.assertEqual(log_entry['action'], action)

    def test_post_log_with_invalid_uuid(self):
        """Prueba de registro de log con UUID inválido."""
        with self.assertRaises(ValueError) as context:
            self.corporate_log.post("", "Test Action")
        self.assertEqual(str(context.exception), "UUID no es válido o está ausente.")

    def test_post_log_with_invalid_action(self):
        """Prueba de registro de log con acción inválida."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        with self.assertRaises(ValueError) as context:
            self.corporate_log.post(uuid_session, "")
        self.assertEqual(str(context.exception), "La acción debe ser una cadena no vacía.")

    def test_list_logs_success(self):
        """Prueba de listado de logs exitoso."""
        uuid_session = "123e4567-e89b-12d3-a456-426614174000"
        self.corporate_log.post(uuid_session, "Log Entry 1")
        logs = self.corporate_log.list(self.corporate_log.uuidCPU)
        self.assertEqual(len(logs), 1)


if __name__ == "__main__":
    unittest.main()