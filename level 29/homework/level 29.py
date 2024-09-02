def print_even_index_numbers(numbers):
    even_index_numbers = numbers[::2]
    print(even_index_numbers)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print_even_index_numbers(numbers)

games = ["Minecraft", "Fortnite", "Among Us", "Roblox", "PUBG"]
programming_languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]
games = programming_languages
print(games)

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("saba")