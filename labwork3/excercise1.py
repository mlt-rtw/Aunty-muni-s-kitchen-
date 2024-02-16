current_users = ["temi", "kobby", "eshun", "SCOTT", "Sarah"]
new_users = ["john", "MaRY", "David", "scott", "Sarah"]

for new_user in new_users:
  lower_new_user = new_user.lower()
  if lower_new_user in [user.lower() for user in current_users]:
    print(f"Sorry, the username {new_user} is already taken.")
  else:
    print(f"The username {new_user} is available!")
