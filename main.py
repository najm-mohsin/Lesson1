# Create a list of favorite colors
colors = ["red", "blue", "green"]

# Print the list
print("Your favorite colors are:", colors)
# Create a dictionary with user input
user_details = {
    "name": input("What is your name? "),
    "age": input("How old are you? "),
    "hobby": input("What is your favorite hobby? ")
}

# Print the dictionary
print("Here are your details:", user_details)
# Update the hobby in the dictionary
new_hobby = input("What is your new favorite hobby? ")
user_details["hobby"] = new_hobby

# Print the updated dictionary
print("Updated details:", user_details)
# Add a new key-value pair
user_details["favorite_food"] = input("What is your favorite food? ")

# Print the updated dictionary
print("Updated details with favorite food:", user_details)
# Remove the 'age' key-value pair
user_details.pop("age", None)

# Print the updated dictionary
print("Updated details after removing age:", user_details)
# Add a list of favorite movies
user_details["favorite_movies"] = ["Toy Story", "Finding Nemo", "The Incredibles"]

# Print the updated dictionary
print("Details with favorite movies:", user_details)
# Loop through the dictionary
for key, value in user_details.items():
    print(key, ":", value)
# Create a dictionary with names and favorite things
favorites = {
    "Alice": ["red", "pizza", "soccer"],
    "Bob": ["blue", "burger", "chess"],
    "Charlie": ["green", "pasta", "reading"]
}

# Print the dictionary
print("Favorites of everyone:", favorites)
