import os
import json
import requests
from utils.apipagespeed import lighthouses
from utils.check_status_code import check_status_code

with open('pagespeed.json',  encoding="utf8") as \
        pagespeedurls:
    urlsJson = json.load(pagespeedurls)

    for urls in urlsJson:
        statusOK = check_status_code(urls["url"])

        if statusOK == False:
            continue

        else:
            lighthouse = lighthouses(urls)

            if lighthouse is None:
                print('Erro no envio para a Elastic...')
                print('')

            else:
                urlelastic = os.environ["ELASTIC_URL_API"]
                login = os.environ["AUTH_USER"]
                pswd = os.environ["AUTH_PASS"]
                headers = {"Content-Type": "application/json"}
                r = requests.post(url=urlelastic, auth=(
                    login, pswd), headers=headers, data=json.dumps(lighthouse))
                print('Sucesso no Envio...')
                print('')
