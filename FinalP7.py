Fred = {"breed":"siamese", "owner":"dale"}
George = {"breed":"ragdoll", "owner":"krista"}
Luna = {"breed":"munchkin", "owner":"don"}
Tiny = {"breed":"birman", "owner":"roger"}
Bob = {"breed":"siberian", "owner":"kevin"}
pets = [Fred, George, Luna, Tiny, Bob]

for pet in pets:
    print("Breed: " + (pet["breed"]).title() + ", " + "Owner: " + (pet["owner"]).title())