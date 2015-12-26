# python-esputnik-api
Python class for use esputnik

```
api = eSputnik()

api.balance()
# {'status_code': 200, 'result': u'{"currentBalance":"0.0","creditLimit":"0.0","currency":"UAH","bonusEmails":"2500","bonusSmses":"10"}'}

api.addressbooks()
# {'status_code': 200, 'result': u'{"addressBook":{"addressBookId":"8550","name":"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439","fieldGroups":{"name":"Personal","fields":[{"id":"18884","name":"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f","description":{"required":"false","readonly":"false"}},{"id":"18885","name":"\u041f\u043e\u043b","description":{"allowedValues":{"possibleValues":["\u043c","\u0436"]},"required":"false","readonly":"false"}}]}}}'}

api.info()
# {'status_code': 200, 'result': u'{"version":"20417","protocolVersion":"1.0"}'}

info = {"email": "test@test.com", "first_name": "first_name", "group": "test"}
api.add_contact(info)
# {'status_code': 200, 'result': u'{"id":"95064156"}'}

api.remove_contact(id=95064156)
# {'status_code': 200, 'result': u"Contact with id='95064156' has been deleted"}

api.get_contact(id=95064060)
# {'status_code': 200, 'result': u'{"firstName":"first_name","channels":[{"type":"email","value":"test@test.com"}],"addressBookId":8585,"id":95064060,"groups":[{"id":3601264,"name":"test","type":"Static"}]}'}

api.update_contact(95064060, info)
# Contact with id='95064060' has been updated

```
