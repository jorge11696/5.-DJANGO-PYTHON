from datetime import date

users = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'country':'Spain',
        'city':'Castellon',
        'is_admin': True
    },
    {
        'email': 'freddier@platzi.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321',
        'country':'Spain',
        'city':'Valencia'
    },
    {
        'email': 'yesica@platzi.com',
        'first_name': 'Yésica',
        'last_name': 'Cortés',
        'country':'Spain',
        'city':'Valencia',
        'password': 'qwerty',
        'birthdate': date(1990, 12,19)
    },
    {
        'email': 'arturo@platzi.com',
        'first_name': 'Arturo',
        'last_name': 'Martínez',
        'country':'Spain',
        'city':'Valencia',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    }
]
from posts.models import User

#Imprimimos su email
for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)

#Traer info a la BD
from posts.models import User

user = User.objects.get(email='freddier@platzi.com')#object es el acceso al ORM y get trae al usuario

#Añadir campo city y country
from posts.models import User

users = User.objects.filter(email__endswith='@platzi.com').update(country=España, city=Castellon)
