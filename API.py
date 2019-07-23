#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from config import Config
from modules import request_nasa_api
def response_request_nasa_api(API_TOKEN):
    result = request_nasa_api(API_TOKEN)
    response = {
        'result': result
    }
    with open(Config.LOCAL_RESPONSE_DIR + '/result_request_nasa_api.json', 'w') as response_file:
        json.dump(response, response_file)
    response = json.dumps(response)
    print(response)
    return response
