import unittest
from unittest.mock import patch, Mock, mock_open, call
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
    @patch('weather_service.requests.get')
    def test_multiple_cities(self, mock_get):
        """Test plusieurs villes avec une seule méthode"""

        cities_and_temps = [
        ("Paris", 25.0),
        ("Londres", 18.5),
        ("Tokyo", 30.2)
        ]

        for city, expected_temp in cities_and_temps:
            with self.subTest(city=city):
                # Configure le mock pour chaque ville
                fake_response = Mock()
                fake_response.status_code = 200
                fake_response.json.return_value = {"main": {"temp": expected_temp}}
                mock_get.return_value = fake_response

                # Appelle la fonction
                result = get_temperature(city)

                # Vérifie le résultat
                self.assertEqual(result, expected_temp)

                # Vérifie que l'appel API a été fait avec les bons paramètres
                mock_get.assert_called_with(
                    "http://api.openweathermap.org/data/2.5/weather",
                    params={
                        'q': city,
                        'appid': 'fake_api_key',
                        'units': 'metric'
                    }
                )

class TestWeatherReport(unittest.TestCase):

    def setUp(self):
        self.city = "Paris"
        self.expected_temp = 20.5
        self.fixed_date = "2024-01-01T12:00:00"
        self.expected_entry = {
            "city": self.city,
            "temperature": self.expected_temp,
            "timestamp": self.fixed_date
        }

    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('weather_service.get_temperature')
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        """Test sauvegarde rapport météo - succès"""

        # Configure les mocks
        mock_get_temp.return_value = self.expected_temp
        mock_datetime.now.return_value.isoformat.return_value = self.fixed_date

        # Appelle la fonction
        result = save_weather_report(self.city)

        # Vérifie le résultat
        self.assertTrue(result)

        # Vérifie que get_temperature a bien été appelé avec "Paris"
        mock_get_temp.assert_called_once_with(self.city)

        # Vérifie que open a été appelé en lecture puis en écriture
        mock_file.assert_any_call('weather_log.json', 'r')
        mock_file.assert_any_call('weather_log.json', 'w')

        # Concatène tous les contenus écrits dans le fichier
        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)

        # Vérifie que les données attendues sont bien présentes
        self.assertIn(self.city, written_data)
        self.assertIn(str(self.expected_temp), written_data)
        self.assertIn(self.fixed_date, written_data)


if __name__ == '__main__':
    unittest.main()