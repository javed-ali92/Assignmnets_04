from hashlib import sha256

def hash_password(password):
    # Returns the SHA256 hash of the given password
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    # Returns True if the hashed password matches the stored hash for the given email
    if email not in stored_logins:
        return False
    return stored_logins[email] == hash_password(password_to_check)

def main():
    # Dictionary of stored emails and their hashed passwords
    stored_logins = {
        "user1@example.com": hash_password("secret123"),
        "user2@example.com": hash_password("mypassword"),
        "admin@site.com": hash_password("adminpass")
    }

    # Ask user for email and password
    email = input("\n\033[1;3mEnter your email: \033[0m")
    password = input("\033[1;3mEnter your password: \033[0m")

    if login(email, stored_logins, password):
        print("✅ Login successful!")
    else:
        print("❌ Login failed. Email or password is incorrect.")

if __name__ == '__main__':
    main()