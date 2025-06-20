import unittest
from unittest.mock import patch, Mock, mock_open
from weather_service import get_temperature, save_weather_report
import requests  # Nécessaire pour RequestException

class TestWeather(unittest.TestCase):

    def setUp(self):
        """Prépare les données communes à tous les tests"""
        self.sample_weather_data = {'main': {'temp': 25.5}}
        self.test_city = "Paris"
        self.invalid_city = "VilleInexistante"
        self.api_url = "http://api.openweathermap.org/data/2.5/weather"
        self.default_params = {
            'appid': 'fake_api_key',
            'units': 'metric'
        }

    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        """Test avec mock pour une réponse API réussie"""

        fake_response = Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = self.sample_weather_data
        mock_get.return_value = fake_response

        result = get_temperature(self.test_city)
        self.assertEqual(result, self.sample_weather_data['main']['temp'])

        mock_get.assert_called_once_with(
            self.api_url,
            params={
                'q': self.test_city,
                'appid': 'fake_api_key',
                'units': 'metric'
            }
        )

    @patch('weather_service.requests.get')
    def test_get_temperature_city_not_found(self, mock_get):
        """Test quand la ville n'existe pas"""

        fake_response = Mock()
        fake_response.status_code = 404
        mock_get.return_value = fake_response

        result = get_temperature(self.invalid_city)
        self.assertIsNone(result)

        mock_get.assert_called_once_with(
            self.api_url,
            params={
                'q': self.invalid_city,
                'appid': 'fake_api_key',
                'units': 'metric'
            }
        )

    @patch('weather_service.requests.get')
    def test_get_temperature_network_error(self, mock_get):
        """Test quand il y a une erreur réseau"""

        mock_get.side_effect = requests.exceptions.RequestException("Erreur réseau")

        result = get_temperature(self.test_city)
        self.assertIsNone(result)

        mock_get.assert_called_once_with(
            self.api_url,
            params={
                'q': self.test_city,
                'appid': 'fake_api_key',
                'units': 'metric'
            }
        )

class TestWeatherReport(unittest.TestCase):

    def setUp(self):
        # Prépare des données communes si besoin
        self.city = "Paris"
        self.fixed_date = "2025-06-20T15:00:00"

    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('weather_service.get_temperature')
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        """Test sauvegarde rapport météo - EXERCICE PRINCIPAL"""

        # Configure mock_get_temp pour retourner 20.5
        mock_get_temp.return_value = 20.5

        # Configure mock_datetime.now().isoformat() pour retourner une date fixe
        mock_now = Mock()
        mock_now.isoformat.return_value = self.fixed_date
        mock_datetime.now.return_value = mock_now

        # Appelle la fonction à tester
        result = save_weather_report(self.city)

        # Vérifie que le résultat est True
        self.assertTrue(result)

        # Vérifie que get_temperature a été appelé avec "Paris"
        mock_get_temp.assert_called_once_with(self.city)

        # Vérifie que le fichier a été ouvert en lecture puis en écriture
        expected_calls = [unittest.mock.call('weather_log.json', 'r'),
                          unittest.mock.call('weather_log.json', 'w')]
        self.assertEqual(mock_file.call_args_list, expected_calls)

        # Vérifie que le contenu écrit dans le fichier contient la bonne info
        handle = mock_file()
        # Le handle.write doit avoir été appelé, vérifie que les données JSON contiennent la bonne date et température
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn(self.fixed_date, written_data)
        self.assertIn(str(20.5), written_data)


if __name__ == '__main__':
    unittest.main()