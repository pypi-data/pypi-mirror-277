def hello():
    return "Hello, World!"


def greet_user(user_input):
    if user_input.lower() == "hi":
        return hello()
    if user_input.lower() == "how are you?":
        return "i am fine. how about you?"
    return "Goodbye"
