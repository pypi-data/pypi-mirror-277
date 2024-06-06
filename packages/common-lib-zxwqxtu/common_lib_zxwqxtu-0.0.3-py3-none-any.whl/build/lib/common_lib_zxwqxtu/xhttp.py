#coding:utf8

import urllib
import urllib.request
import json
import logging
import functools
import copy

def curl_result(input_function):
    @functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        f, log_info = logger.disabled, {}

        if f:
            log_info = {
                'method': input_function.__name__,
                'url': args[0] if args else kwargs.get('url', ''),
                'request_data': args[1] if len(args) > 1 else kwargs.get('parms', ''),
                'headers': args[2] if len(args) > 2 else kwargs.get('headers', ''),
            }

        try:
            code, result = input_function(*args, **kwargs)

            if f:
                log_info.update({'response_code': code, 'response_body': result})
                logger.info(json.dumps(log_info))

            return code == 200, result
        except Exception as e:
            if f:
                log_info.update({'response_code': 500, 'response_err': str(e)})
                logger.error(json.dumps(log_info))

            return False, None

    return wrapper

@curl_result
def get(url, timeout=60, headers={}, is_json=True):
    req = urllib.request.Request(url, headers=headers, method='GET')
    response = urllib.request.urlopen(url=req, timeout=timeout)
    result = json.loads(response.read().decode(), strict=False) if is_json else response.read().decode()
    response.close()

    return response.getcode(), result

@curl_result
def post(requrl, parms, timeout=60, headers={}, is_json=True):
    data_urlencode = urllib.parse.urlencode(parms)
    req = urllib.request.Request(url = requrl, data = data_urlencode.encode('utf-8'), headers=headers)
    response = urllib.request.urlopen(req, timeout=timeout)
    result = json.loads(response.read().decode(), strict=False) if is_json else response.read().decode()
    response.close()

    return response.getcode(), result

@curl_result
def post_json(requrl, parms, timeout=60, headers={}, is_json=True):
    data_urlencode = json.dumps(parms, ensure_ascii=False)
    headers.update({'Content-Type': 'application/json'})
    req = urllib.request.Request(url=requrl, data=data_urlencode.encode('utf-8'), headers=headers)
    response = urllib.request.urlopen(req, timeout=timeout)
    result = json.loads(response.read().decode(), strict=False) if is_json else response.read().decode()
    response.close()

    return response.getcode(), result

@curl_result
def post_text(requrl, parms, timeout=60, is_json=True):
    req = urllib.request.Request(url = requrl, data = parms.encode('utf-8'))
    response = urllib.request.urlopen(req, timeout=timeout)
    result = json.loads(response.read().decode(), strict=False) if is_json else response.read().decode()
    response.close()

    return response.getcode(), result

