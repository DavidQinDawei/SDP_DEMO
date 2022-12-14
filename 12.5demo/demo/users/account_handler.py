from django.http import JsonResponse
import json
from users.models import Users
def account_dispatcher(request):

    # Read the HTTP request, make the content a json object.
    request.params = json.loads(request.body)

    # return 0 if success, 1 if failure
    if request.params['action'] == 'add':
        return add_user(request)
    elif request.params['action'] == 'mod':
        return mod_user(request)
    elif request.params['action'] == 'dele':
        return delete_user(request)
    else:
        return JsonResponse({'return:':1, 'error':'Cannot find the operation'})

def add_user(request):
    params = request.params
    print(params)
    #type = params['type']
    data = params['data']
    type=data['type']
    print(data)
    if type == 'admins':
        entry =Users.objects.create(
            name = data['name'],
            email = data['email'],
            netid = data['netid'],
            password = data['password'],
            isactive = data['isactive'],
            department = data['department'],
            type = data['type']
        )
    elif type == 'dpmember':
        entry = Users.objects.create(
            name = data['name'],
            email = data['email'],
            netid = data['netid'],
            password = data['password'],
            isactive = data['isactive'],
            department = data['department'],
            type = data['type']
        )
    elif type == 'student':
        entry = Users.objects.create(
            name = data['name'],
            email = data['email'],
            netid = data['netid'],
            password = data['password'],
            isactive = data['isactive'],
            major = data['major'],
            club = data['club'],
            year = data['year'],
            type = data['type']
        )
    else:

        #might add a redirect here
        
        return JsonResponse({'return': 1, 'error': 'Invalid Type of User'})
    # return id if success
    return JsonResponse({'return':0, 'id': entry.id})

def find_user(request):
    # type helps navigate the database

    params = request.params
    data = params['data']

    userid = data['id']

    # find the user
    try:
            user = Users.objects.get(id = userid)
    except Users.DoesNotExist:
        return
    return user

def mod_user(request):
    user = find_user(request)
    if user is None:
        return JsonResponse({"return":1, "error": "Cannot find the user"})
    data = request.params['data']
    # modify the profile, I dont know if there is an easier way
    # also, some of the field may not be modified and may cause some error
    # like try to change the majoy of a dpmember
    # there should be more improvements in the future
    print(data)
    if 'name' in data:
        user.name = data['name']
    # maybe use a safer way to change the passwd later
    if 'password' in data:
        user.password = data['password']
    if 'email' in data:
        user.email = data['email']
    if 'netid' in data:
        user.netid = data['netid']
    if 'isactive' in data:
        user.isactive = data['isactive']
    if 'major' in data:
        user.major = data['major']
    if 'year' in data:
        user.year = data['year']
    if 'club' in data:
        user.club = data['club']
    if 'department' in data:
        user.department = data['department']
    #It may not be safe to allow the user to change some of the attributes
    if 'type' in data:
        user.type = data['type']

    # save and return, might redirect to a new page
    user.save()
    return JsonResponse({"return":0})

def delete_user(request):
    
    user = find_user(request)
    if user is None:
        return JsonResponse({'return':1, 'error':'Cannot find the user'})
    user.delete()

    return JsonResponse({'return': 0})