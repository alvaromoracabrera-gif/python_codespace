name = input("Full name: ").strip()

print(f"{name.upper()} has {len(name.replace(' ', ''))} letters")

words = name.split()
username = (words[0][0] + words[1]).lower()

print(f"Username: {username}")
