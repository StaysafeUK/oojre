import random

class PetNamesGenerator:
    def __init__(self):
        self.large_male_dog_names = ["Rex", "Rover", "Sunny", "Goldie", "Muncher", "Zeus", "Bruno", "Duke"]
        self.medium_male_dog_names = ["Cooper", "Bandit", "Beau", "Toby", "Bailey", "Benji", "Buster", "Ace"]
        self.small_male_dog_names = ["Roy", "Paddy", "Pal", "Lightning", "Reuban", "Levi", "Teddy", "Jack"]
        self.large_female_dog_names = ["Cougar", "Roxy", "Bella", "Luna", "Lady", "Stella", "Ginger", "Athena"]
        self.medium_female_dog_names = ["Willow", "Sadie", "Issachi", "Gracie", "Chloe", "Abby", "Scout", "Daisy"]
        self.small_female_dog_names = ["Molly", "Lucy", "Bonnie", "Pipper", "Princess", "Poppy", "Coco", "Mica"]
        self.male_cat_names = ["Siba", "Milo", "Oliver", "Felix", "Tiger", "Max", "Gizmo", "Garfield", "Leo"]
        self.female_cat_names = ["Kitty", "Hazel", "Rosie", "Sophie", "Cleo", "Stella", "Nala", "Minnie", "Sheeba"]
        self.male_goldfish_names = ["Nemo", "Otto", "Speedy", "Fimn", "Bruce", "Salty", "Blaze", "Casper", "Spike"]
        self.female_goldfish_names = ["Dory", "Angel", "Ariel", "Jewel", "Nessie", "Crystal", "Corrie", "Cordelia", "Diana"]

    def suggest_dog_name(self, size, gender, num_names=3):
        size = size.lower()
        gender = gender.lower()

        if size == "large" and gender == "male":
            return random.sample(self.large_male_dog_names, num_names)
        elif size == "medium" and gender == "male":
            return random.sample(self.medium_male_dog_names, num_names)
        elif size == "small" and gender == "male":
            return random.sample(self.small_male_dog_names, num_names)
        elif size == "large" and gender == "female":
            return random.sample(self.large_female_dog_names, num_names)
        elif size == "medium" and gender == "female":
            return random.sample(self.medium_female_dog_names, num_names)
        elif size == "small" and gender == "female":
            return random.sample(self.small_female_dog_names, num_names)
        else:
            return "Invalid input for dog. Did you type in lowercase?"

    def suggest_cat_name(self, gender, num_names=3):
        gender = gender.lower()

        if gender == "male":
            return random.sample(self.male_cat_names, num_names)
        elif gender == "female":
            return random.sample(self.female_cat_names, num_names)
        else:
            return "Invalid input for cat. Did you type in lowercase?"

    def suggest_goldfish_name(self, gender, num_names=3):
        gender = gender.lower()

        if gender == "male":
            return random.sample(self.male_goldfish_names, num_names)
        elif gender == "female":
            return random.sample(self.female_goldfish_names, num_names)
        else:
            return "Invalid input for goldfish. Did you type in lowercase?"

if __name__ == "__main__":
    pet_names_generator = PetNamesGenerator()

    pet_type = input("Do you want to name a dog, cat, or a goldfish? ").lower()

    if pet_type == "dog":
        size_of_dog = input("Is your dog small, medium, or large? ").lower()
        pets_gender = input("Is your dog male or female? ").lower()
        suggested_name = pet_names_generator.suggest_dog_name(size_of_dog, pets_gender)
        print(f"Possible names for your {size_of_dog} size, {pets_gender} dog could be: {suggested_name}")

    elif pet_type == "cat":
        pets_gender = input("Is your cat male or female? ").lower()
        suggested_name = pet_names_generator.suggest_cat_name(pets_gender)
        print(f"Possible Names for your {pets_gender} cat could be: {suggested_name}")

    elif pet_type == "goldfish":
        pets_gender = input("Is your goldfish male or female? ").lower()
        suggested_name = pet_names_generator.suggest_goldfish_name(pets_gender)
        print(f"Possible names for your {pets_gender} goldfish could be: {suggested_name}")

    else:
        print("Invalid pet type. Please choose dog, cat, or goldfish.")