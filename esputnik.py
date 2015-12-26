import requests
import json
from django.conf import settings


class eSputnik:

    def __init__(self):
        self.url = settings.ESPUTNIK_URL
        self.user = settings.ESPUTNIK_USER
        self.password = settings.ESPUTNIK_PASSWORD
        self.address_book_id = settings.ESPUTNIK_ADDRESS_BOOK_ID
        self.prefix = settings.ESPUTNIK_PREFIX
        self.headers = {"content-type": "application/json"}

    def info(self):
        r = requests.get("{0}/api/v1/version".format(self.url), auth=(self.user, self.password))
        result = {"result": r.text, "status_code": r.status_code}
        print result
        return result

    def addressbooks(self):
        r = requests.get("{0}/api/v1/addressbooks".format(self.url), auth=(self.user, self.password))
        result = {"result": r.text, "status_code": r.status_code}
        print result
        return result

    def balance(self):
        r = requests.get("{0}/api/v1/balance".format(self.url), auth=(self.user, self.password))
        result = {"result": r.text, "status_code": r.status_code}
        print result
        return result

    def is_contact(self, data):
        r = requests.get("{0}/api/v1/contacts".format(self.url), params=data, auth=(self.user, self.password), headers=self.headers)
        if not r.text:
            return True
        else:
            return False

    def add_contact(self, info):
        data = {}
        data["addressBookId"] = self.address_book_id
        data["firstName"] = info["first_name"]
        data["channels"] = {"type": "email", "value": info["email"]}
        data["groups"] = {"name": "{0}{1}".format(info["group"], self.prefix)}
        if not self.is_contact(data):
            r = requests.post("{0}/api/v1/contact".format(self.url), data=json.dumps(data), auth=(self.user, self.password), headers=self.headers)
            result = {"result": r.text, "status_code": r.status_code}
            print result
            return result

    def remove_contact(self, id):
        r = requests.delete("{0}/api/v1/contact/{1}".format(self.url, id), auth=(self.user, self.password), headers=self.headers)
        result = {"result": r.text, "status_code": r.status_code}
        print result
        return result

    def get_contact(self, id):
        r = requests.get("{0}/api/v1/contact/{1}".format(self.url, id), auth=(self.user, self.password), headers=self.headers)
        result = {"result": r.text, "status_code": r.status_code}
        print result
        return result

    def update_contact(self, id, info):
        data = {}
        data["addressBookId"] = self.address_book_id
        data["firstName"] = info["first_name"]
        data["channels"] = {"type": "email", "value": info["email"]}
        data["groups"] = {"name": "{0}{1}".format(info["group"], self.prefix)}
        r = requests.put("{0}/api/v1/contact/{1}".format(self.url, id), data=json.dumps(data), auth=(self.user, self.password), headers=self.headers)
        print r.text
        return True


# https://esputnik.com.ua/api/

#api = eSputnik()

#api.balance()
# {'status_code': 200, 'result': u'{"currentBalance":"0.0","creditLimit":"0.0","currency":"UAH","bonusEmails":"2500","bonusSmses":"10"}'}

#api.addressbooks()
# {'status_code': 200, 'result': u'{"addressBook":{"addressBookId":"8550","name":"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439","fieldGroups":{"name":"Personal","fields":[{"id":"18884","name":"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f","description":{"required":"false","readonly":"false"}},{"id":"18885","name":"\u041f\u043e\u043b","description":{"allowedValues":{"possibleValues":["\u043c","\u0436"]},"required":"false","readonly":"false"}}]}}}'}

#api.info()
# {'status_code': 200, 'result': u'{"version":"20417","protocolVersion":"1.0"}'}

#info = {"email": "test@test.com", "first_name": "first_name", "group": "test"}
#api.add_contact(info)
# {'status_code': 200, 'result': u'{"id":"95064156"}'}

#api.remove_contact(id=95064156)
# {'status_code': 200, 'result': u"Contact with id='95064156' has been deleted"}

#api.get_contact(id=95064060)
# {'status_code': 200, 'result': u'{"firstName":"first_name","channels":[{"type":"email","value":"test@test.com"}],"addressBookId":8585,"id":95064060,"groups":[{"id":3601264,"name":"test","type":"Static"}]}'}

#api.update_contact(95064060, info)
# Contact with id='95064060' has been updated
