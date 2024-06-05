from ns_search_saved_export  import NsSearchSavedExport

import os 
import json

search_saved_id = 'customsearch33885'
api = NsSearchSavedExport(
    # url = 'https://5469654.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=3472&deploy=1',
    url = 'https://5469654.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=3579&deploy=1',
    consumer_key = '6bf7afb708cd34d17d64c19ee74a305e9aa476b85ce7a0143feafd3e841c195a',
    consumer_secret = '029be94e829b9dbd17e33257bc3416739da4aeaa4974169673e34bbee8668037',
    token_key = '2d726b31b7a05d11bbdc517e470cf53310613c9f474f50ac3e348d8a2e6e3d8a',
    token_secret = '6a842ba5f1e13dd56e9cef9a88f7bb05e498973de1942e540ea8554050c3fc44',
    realm = '5469654',
    search_id=search_saved_id
)
    

page_index = 0
page_range = 10000

data_result = []
while True:
    print(page_index)
    
    # Send request
    payload = {'searchID': search_saved_id, 'pageIndex': page_index, 'pageRange': page_range }

    response = api.send_request(payload)

    # Convertir el diccionario a una cadena JSON
    json_string = json.dumps(response)

    # Convertir la cadena JSON de nuevo a un diccionario
    data = json.loads(json_string)

    # Extraer la lista de resultados
    results = data.get('results', [])
    
    data_result = data_result + results
    
    if len(results) == 0:
        break
    
    page_index += 1  
    
    if page_index == 4:
        results = {'results': data_result}
        
        api.create_folder_part()
        with open(os.path.join(api.path_part, 'conslidado.json'), 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)
    
        # todo exportacion
        # Extract data
        data = api.extract_data(results)

        # Save data to Excel
        api.save_to_excel(data)

        # Save data to CSV
        api.save_to_csv(data)

        # Save data to TXT
        api.save_to_txt(data)


        break
    
    with open(os.path.join("data_test", f'{page_index}.json'), 'w', encoding='utf-8') as json_file:
        json.dump(response, json_file, ensure_ascii=False, indent=4)

# print(responser)





