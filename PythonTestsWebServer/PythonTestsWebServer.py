import unittest
import requests

class WebServerTests(unittest.TestCase):
    def setUp(self):
        # Set up the base URL for the web server
        self.base_url = 'http://localhost:8080'
    
    def test_get_logs_route(self):
        # Send a GET request to the /logs route
        response = requests.get(f'{self.base_url}/api/logs')
        
        try:
            # Assert the status code is 200 (OK)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            
            # Assert the response content is not empty
            self.assertIsNotNone(response.json())
            
            
            print('Test "GET /logs" passed.')
            print('Response:')
            print(format_json(response.text))
            
        except requests.HTTPError as e:
            print(f'Test "GET /logs" failed. Error: {e}')
            print('Error response:')
            print(format_json(response.text))
        
    def test_create_transaction_route(self):
        # Send a GET request to the route that creates a new transaction
        response = requests.get(f'{self.base_url}/api/transaction')
        
        try:
            # Assert the status code is 200 (OK)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            
            # Assert the response content is not empty
            self.assertIsNotNone(response.json())
            
            
            print('Test "GET /transaction" passed.')
            print('Response:')
            print(format_json(response.text))
            
        except requests.HTTPError as e:
            print(f'Test "GET /transaction" failed. Error: {e}')
            print('Error response:')
            print(format_json(response.text))

def format_json(json_str):
    try:
        import json
        formatted_json = json.dumps(json.loads(json_str), indent=4)
        return formatted_json
    except ValueError:
        return json_str
    
if __name__ == '__main__':
    unittest.main()
