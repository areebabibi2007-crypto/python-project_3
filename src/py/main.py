import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def run_user_input():
    attempt = 1
    
    while True:
        # User input ke hisab se header decide hoga
        print(f"\n---")
        print(f"# Attempt {attempt}")
        print("")
        print("==================================================")
        print("          RANDOM PASSWORD GENERATOR               ")
        print("==================================================")
        
        user_input = input("\nEnter Password Length (6-50): ")
        
        if not user_input.isdigit():
            print("Please enter a valid number.")
            print("")
        else:
            length = int(user_input)
            if length < 6:
                print("Error: Password length must be at least 6.")
                print("")
            elif length > 50:
                print("Error: Password length cannot exceed 50.")
                print("")
            else:
                pwd = generate_password(length)
                print("\nGenerated Password")
                print("--------------------------------------------------")
                print(pwd)
                print("--------------------------------------------------")
                print("```")
                # Sahi password banne ke baad loop stop ho jayega
                break
                
        attempt += 1

# Program run karein
run_user_input()