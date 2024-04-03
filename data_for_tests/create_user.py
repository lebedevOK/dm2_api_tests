from datetime import datetime
import random

"""
Register new user
"""
def new_user():
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        login_gen = str(f"user_{timestamp}")
        # login_gen = GenDataUser.generate_login()
        email_gen = f"user_{timestamp}@qw.ru"
        # email_gen = GenDataUser.generate_email()
        password_gen = str(random.randint(100000, 999999))

        with open("../emails.txt", "a") as file:
          file.write(email_gen + "\n")

        return login_gen, email_gen, password_gen

print(new_user())