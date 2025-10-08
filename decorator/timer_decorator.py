
def login_required(func):
    def wrapper(user, *args, **kwagrs):
        if user.is_authanticated:
            return func(user, *args, **kwagrs)
        else:
            print("You must be logged in to view this page.")
    return wrapper

class User:
    def __init__(self, name, is_authanticated):
        self.name = name
        self.is_authanticated = is_authanticated
        
# Create authanticated and non authanticated user by using User class
auth_user = User("Fasial", True)
non_auth_user = User("Alam", False)


@login_required
def view_profile(user):
    print(f"Viewing profile of {user.name}")

view_profile(auth_user)
view_profile(non_auth_user)