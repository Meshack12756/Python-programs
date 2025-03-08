import random
import string as st

print(f"Your Password: ")

chars = st.ascii_lowercase + st.digits + st.punctuation + st.ascii_uppercase

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)

