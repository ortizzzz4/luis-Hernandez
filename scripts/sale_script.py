from xmlrpc import client

url = 'http://127.0.0.1:8069/'
db = 'academy'
username ='luis'
password = '1234'

commo = client.ServerProxy("{}/xmlrpc/2/commo".format(url))
print(commo)

uid = commo.authenticate(db,username,password,{})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db,uid,password,
                                 'sale.order','check_access_rights',
                                 ['write'],{'raise_exception': False})

print(model_access)

draft_quotes = models.execute_kw(db,uid,password,
                                 'sale.order','search',
                                 [[['state','=', 'draft']]])
print(draft_quotes)


if_confirmed = models.execute_kw(db,uid,password,
                                 'sale.order','action_confirm',
                                 [draft_quotes])
print(if_confirmed)
