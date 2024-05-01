from django.shortcuts import render

def users(request):
    users = [
        {'id': 1, 'username': 'user1', 'usertag': 'tag1'},
        {'id': 2, 'username': 'user2', 'usertag': 'tag2'},
        # Add more users as needed
    ]
    return render(request, 'users.html', {'users': users})

def profile(request, user_id):
    user_profile = {
        'id': user_id, 
        'username': f'user{user_id}', 
        'usertag': f'tag{user_id}',
        'following': ['user2', 'user3', 'user4'],  # Users this user is following
        'followers': ['user5', 'user6', 'user7'],  # Users following this user
    }
    tweets = [
        {'content': 'First tweet'},
        {'content': 'Second tweet'},
        # Add more tweets as needed
    ]
    return render(request, 'profile.html', {'user_profile': user_profile, 'tweets': tweets})