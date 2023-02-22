from xmlrpc import client

url = ""
bd = ""
username  = ""
password  = ""

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())


uid = common.authenticate(bd,username,password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

models_access = models.execute_kw(bd, uid, password,
                                  'academy.session','check_access_rights',
                                  ['write'], {'raise_exception':False})
print(models_access)

courses = models.execute_kw(bd,uid,password,
                            'academy.course','search_read',
                            [[['lecel', 'in', ['intermediate', 'beginner']]]])

course = models.execute_kw(bd, uid, password,
                           'academy.course', 'search',
                          [[['name','=','Accounting 200']]])
print(course)

session_fields = models.execute_kw(bd, uid, password,
                                   'academy.session','fields_get',[],{'attributes': ['string','type','required']})
print(session_fields)

new_session = models.execute(bd,uid,password,
                             'academy.session','create',
                             [{
                                 'course_id':course[0],
                                 'state':'open',
                                 'duration': 5,
                                 }])
print(new_session)