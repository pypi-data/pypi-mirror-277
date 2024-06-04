def hello():
    return "Hello, World!"

def greet_user(user_input):
    if user_input.lower() == "hi":
        return hello()
    return "Goodbye"

