import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(all_characters, k=length - 4)
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to the Secure Password Generator!")
    try:
        length = int(input("Enter the desired length of the passwords (minimum 4): "))
        number = int(input("Enter the number of passwords to generate: "))
        
        if length < 4:
            raise ValueError("Password length should be at least 4 characters.")
        
        passwords = [generate_password(length) for _ in range(number)]
        
        print("\nGenerated Passwords:")
        for idx, pwd in enumerate(passwords, 1):
            print(f"{idx}: {pwd}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")

if __name__ == "__main__":
    main()
