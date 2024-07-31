import requests
from requests import Response
import allure


class Send_Request():
    @allure.step('REQUEST')
    def send(self, method, url, headers=None, data=None, params=None, status=200) -> Response:
        with allure.step(method):
            res: Response = requests.request(
                method=method, url=url, headers=headers, data=data, params=params)
            if res.text.startswith('<'):
                allure.attach(res.content, 'RESPONSE',allure.attachment_type.XML)
            elif res.text.startswith('{'):
                allure.attach(res.content, 'RESPONSE',allure.attachment_type.JSON)
            else:
                allure.attach(res.content, 'RESPONSE',allure.attachment_type.TEXT)
            assert res.status_code == status, f"Response status code was not ${status}"
            return res