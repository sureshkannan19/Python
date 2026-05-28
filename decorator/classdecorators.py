import contextvars
user_var = contextvars.ContextVar('user_details')

class UserDetails:

    def __init__(self, username, role):
        self.username = username
        self.role = role

class RoleDecorator:

    def __init__(self, role):
        self.role = role

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            user_details = user_var.get(None)
            if not user_details or self.role != user_details.role:
                raise ValueError("Unauthorized")
            return func(*args, **kwargs)
        return wrapper

user_var.set(UserDetails("SK", "admin"))

@RoleDecorator(role="admin")
def process():
    print(f"Processing Completed")

process()