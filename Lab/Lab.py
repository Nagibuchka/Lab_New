import datetime

def greet(name: str) -> str:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"Hello, {name}! The current time is {current_time}."

def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()
print("Тестова зміна коду")
print("Тепер зміна на гітхабі")
