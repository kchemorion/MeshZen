from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests

app_name = 'users'


def login_with_zenodo(request):
    # Step 1: Redirect users to Zenodo authentication page
    client_id = 'hSK0EShDLtQ30XCrmAxFTCvAzn759w5qhKwguH9E'
    redirect_uri = 'http://localhost:8000/login_with_zenodo/callback_from_zenodo'
    scope = 'deposit:write deposit:actions'
    url = f'https://zenodo.org/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}'
    return redirect(url)

def callback_from_zenodo(request):
    # Step 2: Obtain access and refresh tokens
    client_id = 'hSK0EShDLtQ30XCrmAxFTCvAzn759w5qhKwguH9E'
    client_secret = 'c43i953RJULF6cfULsLtBWmMbPyhpeUJwnFlP05NWAHkjY091fi2WkSgV4Nl'
    code = request.GET.get('code')
    redirect_uri = 'http://localhost:8000/login_with_zenodo/callback_from_zenodo'
    url = 'https://zenodo.org/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=data)
    access_token = response.json()['access_token']

    # Step 3: Get user data from Zenodo API
    headers = {'Authorization': f'Bearer {access_token}'}
    user_url = 'https://zenodo.org/api/deposit/depositions'
    response = requests.get(user_url, headers=headers)
    user_data = response.json()

    # Step 4: Create or authenticate user in Django database
    user_id = user_data[0]['userId']
    email = user_data[0]['email']
    name = user_data[0]['name']
    username = email.split('@')[0]
    password = User.objects.make_random_password()
    user, created = User.objects.get_or_create(username=username, email=email, first_name=name)
    if created:
        user.set_password(password)
        user.save()
    user = authenticate(request, username=username, password=password)
    login(request, user)

    return redirect('base:home')



