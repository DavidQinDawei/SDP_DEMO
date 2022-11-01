from django.http import JsonResponse
import json
from admins.models import Admins
from dpmember.models import Dpmember
from student.models import Student
def admins_dispatcher(request):

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
    type = params['type']
    data = params['data']
    if type == 'admins':
        entry = Admins.objects.creates(
            name = data['name'],
            email = data['email'],
            netid = data['netid'],
            password = data['password'],
            isactive = data['isactive'],
            department = data['department']
        )
    elif type == 'dpmember':
        entry = Dpmember.objects.creates(
            name = data['name'],
            email = data['email'],
            netid = data['netid'],
            password = data['password'],
            isactive = data['isactive'],
            department = data['department']
        )
    elif type == 'student':
        entry = Student.objects.creates(
            name = data['name'],
            email = data['email'],
            netid = data['netid'],
            password = data['password'],
            isactive = data['isactive'],
            major = data['major'],
            club = data['major'],
            year = data['year']
        )
    else:

        #might add a redirect here
        
        return JsonResponse({'return': 1, 'error': 'Invalid Type of User'})
    # return id if success
    return JsonResponse({'return':0, 'id': entry.id})

def find_user(request):
    # type helps navigate the database

    params = request.params
    type = params['type']
    userid = params['id']

    # find the user
    if type not in ['admins', 'student', 'dpmember']:
        return JsonResponse({'return': 1, 'error': 'Invalid Type of User or Typt Missing'})
    elif type == 'admins':
        try:
            user = Admins.objects.get(id == userid)
        except Admins.DoesNotExist:
            return ({'return': 1, 'error': 'Cannot find the user by ID'})
    elif type == 'dpmember':
        try:
            user = Dpmember.objects.get(id == userid)
        except Dpmember.DoesNotExist:
            return ({'return': 1, 'error': 'Cannot find the user by ID'})
    elif type == 'student':
        try:
            user = Student.objects.get(id == userid)
        except Student.DoesNotExist:
            return ({'return': 1, 'error': 'Cannot find the user by ID'})
    else:
        return ({'return': 1, 'error': 'Unknown Error'})
    return user

def mod_user(request):
    user = find_user(request)
    data = request.params[data]
    # modify the profile, I dont know if there is an easier way
    # also, some of the field may not be modified and may cause some error
    # like try to change the majoy of a dpmember
    # there should be more improvements in the future
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

    # save and return, might redirect to a new page
    user.save()
    return JsonResponse({"return":0})

def delete_user(request):
    
    user = find_user(request)
    user.delete()

    return JsonResponse({'return': 0})