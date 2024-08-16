import itertools
import string
import requests
import time

def check_username_availability(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    time.sleep(2)
    
    if response.status_code == 200:
        response_json = response.json()
        if "id" in response_json:
            return True
    elif response.status_code == 404:
        return False

    return False

def generate_usernames():
    characters = string.ascii_lowercase + string.digits + '_'
    for combo in itertools.product(characters, repeat=3):
        yield ''.join(combo)

def find_available_usernames():
    taken_usernames = []
    total_taken = 0
    with open("namesthatwork.txt", "w") as file:
        for username in generate_usernames():
            if check_username_availability(username):
                taken_usernames.append(username)
                file.write(f"{username}\n")
                total_taken += 1
                print(f"Taken: {username}")
            else:
                print(f"Available: {username}")
    return taken_usernames, total_taken

def display_menu():
    print(r"""
 _______                            _________                    _____   __   
 \      \  _____     _____    ____  \_   ___ \ _______ _____   _/ ____\_/  |_ 
 /   |   \ \__  \   /     \ _/ __ \ /    \  \/ \_  __ \\__  \  \   __\ \   __\
/    |    \ / __ \_|  Y Y  \\  ___/ \     \____ |  | \/ / __ \_ |  |    |  |  
\____|__  /(____  /|__|_|  / \___  > \______  / |__|   (____  / |__|    |__|  
        \/      \/       \/      \/         \/              \/                
                       
                              Made by HauntingBug
    """)

def username_checker():
    username = input("Enter a username to check availability: ")
    if check_username_availability(username):
        print(f"The username '{username}' is taken.")
    else:
        print(f"The username '{username}' is available.")

def main():
    while True:
        display_menu()
        print("\nMenu:")
        print("1. Check a specific username's availability")
        print("2. Generate and check 3-letter usernames")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1, 2, 3): ")
        
        if choice == '1':
            username_checker()
        elif choice == '2':
            taken_usernames, total_taken = find_available_usernames()
            print(f"\nTotal number of taken usernames: {total_taken}")
            print(f"Taken usernames saved to namesthatwork.txt.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
