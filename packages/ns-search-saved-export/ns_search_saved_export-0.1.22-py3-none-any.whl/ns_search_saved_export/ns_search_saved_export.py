import os
import logging
import json
import oauth2 as oauth
import requests
import pandas as pd
from .utils import SignatureMethod_HMAC_SHA256


#region Configurar el manejador de logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configurar el manejador de logging (opcional)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
#endregion

class NsSearchSavedExport:
    def __init__(self, url: str, consumer_key: str, consumer_secret: str, token_key: str, token_secret: str, realm: str, search_id: str = ''):
        """Class constructor

        Args:
            url (str): RESTlet service URL to export saved search
            consumer_key (str): Netsuite integration client key
            consumer_secret (str): Netsuite integration client secret key
            token_key (str): NetSuite Access Key Token
            token_secret (str): NetSuite Access Secret Token
            realm (str): NetSuite domain environment ID. Example: 123456
            searchID (str): search ID of the search saved in NetSuite
        """
        self.url = url
        self.consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
        self.token = oauth.Token(key=token_key, secret=token_secret)
        self.realm = realm
        self.search_id = search_id
    
        self.path = self.create_folder("data")
        self.file_name = self.rename(self.search_id)
        

    def _generate_oauth_params(self):
        """Returns the structured oauth parameters

        Returns:
            dict: Oauth params
        """
        try: 
            return {
                'oauth_version': '1.0',
                'oauth_nonce': oauth.generate_nonce(),
                'oauth_timestamp': str(oauth.generate_timestamp()),
                'oauth_token': self.token.key,
                'oauth_consumer_key': self.consumer.key,
                'oauth_signature_method': 'HMAC-SHA256'
            }
        except Exception as e:
            logger.error(f"Error  {self._generate_oauth_params.__name__}: ".format(e))
            return {}

    def send_request(self, payload):
        """POST request to obtain saved search data

        Returns:
            dict: POST request response
        """
        try:
            params = self._generate_oauth_params()
            req = oauth.Request(method='POST', url=self.url, parameters=params)
            signature_method = SignatureMethod_HMAC_SHA256()
            req.sign_request(signature_method, self.consumer, self.token)
            header = req.to_header(self.realm)
            headers = {'Authorization': header['Authorization'].encode('ascii', 'ignore'), 'Content-Type': 'application/json'}
            
            response = requests.post(url=self.url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
                
            # Imprimir respuesta completa
            return response.json()
        except Exception as e:
            logger.error(f"Error  {self.send_request.__name__}: {format(e)}")
            return {}
        
    def extract_data(self, json_data: dict):
        """Structured data obtained from the saved search

        Args:
            json_data (dict): Data obtained in the POST response

        Returns:
            list: List of saved search data
        """
        try:
            # Export original JSON data to a JSON file
            with open(f'{self.file_name}.json', 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=4)
            
            matrix = []
            headers = []

            # Verificar si 'results' está en json_data
            if 'results' not in json_data:
                raise KeyError("La clave 'results' no se encuentra en los datos de respuesta.")

            for index, data in enumerate(json_data['results']):
                row = []
                if index == 0:
                    headers = list(data.keys())
                    matrix.append(headers)

                for key in headers:
                    value = data.get(key, "")
                    row.append(value)
                matrix.append(row)
            
            return matrix
        except Exception as e:
            logger.error(f"Error  {self.extract_data.__name__}: {format(e)}")

    def save_to_excel(self, matrix: list, file_name: str = None, sheet_name: str = "data"):
        """Save data in Excel format

        Args:
            matrix (list): Search data
            file_name (str) opcional: Excel file name
            sheet_name (str optional): Excel sheet name
        """
        try:
            self.file_name = self.rename(file_name)
                
            df = pd.DataFrame(matrix[1:], columns=matrix[0])
            df.to_excel(f'{self.file_name}.xlsx', sheet_name=sheet_name, index=False)
            
        except Exception as e:
            logger.error(f"Error  {self.save_to_excel.__name__}: ".format(e))
        
    def save_to_csv(self, matrix: list, file_name: str = None):
        """Save data in CSV format

        Args:
            matrix (list): Search data
            file_name (str) optional: CSV file name
        """
        try:
            self.file_name = self.rename(file_name)
            df = pd.DataFrame(matrix[1:], columns=matrix[0])
            df.to_csv(f'{self.file_name}.csv', index=False)
        except Exception as e:
            logger.error(f"Error  {self.save_to_csv.__name__}: {format(e)}")

    def save_to_txt(self, matrix: list, file_name: str = None):
        """Save data in TXT format

        Args:
            matrix (list): Search data
            file_name (str) optional: TXT file name
        """
        try:
            self.file_name = self.rename(file_name)
            df = pd.DataFrame(matrix[1:], columns=matrix[0])
            df.to_csv(f'{self.file_name}.txt', sep=',', index=False, header=False)
        except Exception as e:
            logger.error(f"Error  {self.save_to_txt.__name__}: {format(e)}")
        
    def create_folder(self, name: str = "data") -> str:
        """Create a folder to save the data

        Args
            folder_name (str) optional: Folder name
            
        Returns:
            str: Folder path
        """
        try:
            self.path = os.path.join(name, self.search_id)
            if not os.path.exists(self.path):
                os.makedirs(self.path)
                
            return self.path
        except Exception as e:
            logger.error(f"Error  {self.create_folder.__name__}: ".format(e))
        
    def rename(self, name: str = None) -> str:
        """Rename the file name
        
        Args:
            name (str) optional: File name
            
        Returns:
            str: File name
        """
        try: 
            return os.path.join(self.path, name) if name else os.path.join(self.path, self.search_id)
        except Exception as e:
            logger.error(f"Error  {self.rename.__name__}: ".format(e))