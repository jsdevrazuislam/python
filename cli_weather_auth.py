import json
import requests
import getpass

USER_FILE = "users.json"
API_KEY = "a7819d2e899e9e487dd34dbccf867b21" 

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

def register():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("❌ Username already exists!")
        return
    password = getpass.getpass("Enter new password: ")
    users[username] = password
    save_users(users)
    print("✅ Registration successful!")

def login():
    users = load_users()
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in users and users[username] == password:
        print("✅ Login successful!")
        return username
    else:
        print("❌ Invalid credentials!")
        return None

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"🌤️ Weather in {city}: {data['weather'][0]['description'].capitalize()} - {data['main']['temp']}°C")
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching weather data:", e)

def main():
    while True:
        print("\n🌍 Welcome to CLI Weather App")
        print("1️⃣ Register")
        print("2️⃣ Login")
        print("3️⃣ Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                city = input("Enter city name: ")
                get_weather(city)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
