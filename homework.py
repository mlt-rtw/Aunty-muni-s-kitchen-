# Create a list of email addresses (not in alphabetical order)
emails = ["brie@gmail.com", "eshun@gmail.com", "sarfo@gmail.com", "temi@gmail.com"]

# Print the original list
print("Original list:")
for email in emails:
    print(email)

# Sort the list alphabetically (ascending)
emails.sort()

# Print the sorted list
print("\nList sorted alphabetically:")
for email in emails:
    print(email)

# Add more email addresses using the append() method
emails.append("jonathan@gmail.com")
emails.append("kwame@gmail.com")

# Print the updated list
print("\nUpdated list:")
for email in emails:
    print(email)

# Remove an email address from the list
emails.remove("eshun@gmail.com")

# Print the number of people attending the wedding
number_of_guests = len(emails)
print("\nNumber of guests:", number_of_guests)

# Print all email addresses in lowercase and alphabetical order
print("\nGuest email addresses (lowercase, alphabetical):")
for email in sorted(emails, key=str.lower):
    print(email.lower())
