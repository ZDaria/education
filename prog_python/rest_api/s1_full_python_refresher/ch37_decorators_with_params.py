import functools


user = {"username": "jose", "access_level": "admin"}


def make_secure(access_lvl):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_lvl:
                return func(*args, **kwargs)
            else:
                return f"No {access_lvl} permissions for user " \
                       f"{user['username']}."

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_pwd():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_pwd():
    return "user: user_pwd"


print(get_admin_pwd())
