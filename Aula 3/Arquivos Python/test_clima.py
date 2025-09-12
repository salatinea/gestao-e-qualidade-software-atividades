import unittest
from unittest.mock import patch, Mock
from clima import buscar_clima

class TestBuscarClima(unittest.TestCase):

    @patch("clima.requests.get")
    def test_resposta_valida(self, mock_get):
      mock_response = Mock()
      mock_response.json.return_value = {"temperatura": 25.5}
      mock_get.return_value = mock_response
      self.assertEqual(buscar_clima("São Paulo"), 25.5)

    @patch("clima.requests.get")
    def test_resposta_sem_temperatura(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"umidade": 80}
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as cm:
            buscar_clima("Rio de Janeiro")
        self.assertIn("temperatura", str(cm.exception))

if __name__ == "__main__":
    unittest.main()
