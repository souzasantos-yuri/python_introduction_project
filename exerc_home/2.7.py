#Write a program that creates a dictionary with fruit names as keys and their respective prices as values. Ask the user for the name of a fruit and display the corresponding price.

fruit_dict = {

    "apple": 1.5,
    "banana": 2.75,
    "grape": 1.90,
    "pear": 1.25,
    "orange": 0.65,
    "lime": 1.25,
    "dragonfruit": 2.15,
    "pineapple": 3.20,
    "jackfruit": 5.80

}

print("Choose your fruit: ")
print("apple            pear             dragonfruit")
print("banana           orange           pineaple")
print("grape            lime             jackfruit")
chosen_fruit = input("Choose your fruit: ")

print(f"{chosen_fruit} price is: {fruit_dict[chosen_fruit]}")