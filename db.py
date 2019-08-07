import peewee

db = peewee.SqliteDatabase('user.db')

class User(peewee.Model):
    state = peewee.IntegerField(default = 0)#
    user_id = peewee.TextField(unique = True)
    phone = peewee.TextField(default = '')#
    name = peewee.TextField(default = '')#
    surname = peewee.TextField(default = '')#
    
    class Meta:
        database = db
        
def init():
    db.connect()
    db.create_tables([User], safe = True)
    db.close()
    
def get_state(user_id):
    user = User.get_or_none(user_id = user_id)
    if user is None:
        return None
    return user.state
  
def set_state(user_id, state):
    user, created = User.get_or_create(user_id = user_id)
    
    user.state = state
    user.save()
    
def get_phone(user_id):
    user = User.get_or_none(user_id = user_id)
    if user is None:
        return None
    return user.phone  

def set_phone(user_id, phone):    
    user, created = User.get_or_create(user_id = user_id)
    
    user.phone = phone
    user.save()
    
def get_name(user_id):
    user = User.get_or_none(user_id = user_id)
    if user is None:
        return None
    return user.name  

def set_name(user_id, name):    
    user, created = User.get_or_create(user_id = user_id)
    
    user.name = name
    user.save()
    
def get_surname(user_id):
    user = User.get_or_none(user_id = user_id)
    if user is None:
        return None
    return user.surname  

def set_surname(user_id, surname):    
    user, created = User.get_or_create(user_id = user_id)
    
    user.surname = surname
    user.save()
    
init()
