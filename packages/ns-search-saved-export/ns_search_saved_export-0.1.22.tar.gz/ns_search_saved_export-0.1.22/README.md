# NetSuite SEARCH SAVED EXPORT

This library allows you to interact with saved searches by importing data from saved searches in Excel, CSV, and TXT formats.

## Installation

```python
pip install ns_search_saved_export
```

## Usage
### Get All date from a saved search

Use this method to obtain all the data from a saved search when the size of the data is less than 10000 records.

```python
from ns_search_saved_export.ns_search_saved_export import NsSearchSavedExport

# Obtain the saved search ID
search_saved_id = 'customsearch33885' # Replace with your saved search ID

# Initialize the API
api = NsSearchSavedExport(
    url='https://your-netsuite-url',
    consumer_key='your_consumer_key',
    consumer_secret='your_consumer_secret',
    token_key='your_token_key',
    token_secret='your_token_secret',
    realm='your_realm',
    search_id=search_saved_id
)

# Send request
payload = {
    'searchID': search_saved_id, # Replace with your saved search ID
}

# Obtain the data
response = api.send_request(payload)

# Extract data
data = api.extract_data(response)

# Save data to Excel
api.save_to_excel(data)

# Save data to CSV
api.save_to_csv(data)

# Save data to TXT
api.save_to_txt(data)

```

### Get data paginated from a saved search

Use this method to obtain data from a saved search when the size of the data is greater than 10000 records.

```python
from ns_search_saved_export.ns_search_saved_export import NsSearchSavedExport

# Obtain the saved search ID
search_saved_id = 'customsearch33885' # Replace with your saved search ID
page_index = 0
page_range = 10000

# Initialize the API
api = NsSearchSavedExport(
    url='https://your-netsuite-url',
    consumer_key='your_consumer_key',
    consumer_secret='your_consumer_secret',
    token_key='your_token_key',
    token_secret='your_token_secret',
    realm='your_realm',
    search_id=search_saved_id
)
# Send request
# Note: the values of pageIndex and pageRange are optional but both must be sent in case you want to obtain the data of a page

payload = {
    'searchID': search_saved_id, # Replace with your saved search ID
    'pageIndex': page_index, # Replace with your page index. Default: 0 (first page) add 1 to get the next page
    'pageRange': page_range # Replace with your page range. Default: 1000 (first page) add 1000 to get the next page. Maximum: 10000
}

data_result = []
while True:
    # Send request
    response = api.send_request(payload)

    # Convertir el diccionario a una cadena JSON
    json_string = json.dumps(response)

    # Convertir la cadena JSON de nuevo a un diccionario
    data = json.loads(json_string)

    # Extraer la lista de resultados
    results = data.get('results', [])
    
    data_result = data_result + results
    
    if len(results) == 0:
        results = {'results': data_result}

        # Optional: save the data to a file
        with open(os.path.join(api.path, 'conslidado.json'), 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)

        # Extract data
        data = api.extract_data(results)

        # Save data to Excel
        api.save_to_excel(data)

        # Save data to CSV
        api.save_to_csv(data)

        # Save data to TXT
        api.save_to_txt(data)
        break
    
    page_index += 1  
    

```

## Methods available
List of methods available in the library

```python
# Obtain the data
"""POST request to obtain saved search data

Returns:
    dict: POST request response    
"""
response = api.send_request(payload)

# Extract data
"""Structured data obtained from the saved search

    Args:
        json_data (dict): Data obtained in the POST response

    Returns:
        list: List of saved search data
"""
data = api.extract_data(response)

# Save data to Excel
"""Save data in Excel format

    Args:
        matrix (list): Search data
        file_name (str) opcional: Excel file name. Default: name of the saved search
        sheet_name (str optional): Excel sheet name. Default: data
"""
api.save_to_excel(data, 'data.xlsx', 'Sheet1')

# Save data to CSV
"""Save data in CSV format

    Args:
        matrix (list): Search data. Default: name of the saved search
        file_name (str) optional: CSV file name
"""
api.save_to_csv(data, 'data.csv')

# Save data to TXT
"""Save data in TXT format

    Args:
        matrix (list): Search data
        file_name (str) optional: TXT file name. Default: name of the saved search
"""
api.save_to_txt(data, 'data.txt')

```

