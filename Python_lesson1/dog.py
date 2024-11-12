class Dog():
    species = 'Canis familiaris'

    def __init__(self,name,age):
        self.name = name
        self.age =age

doogie = Dog('doggy', 2)
dog_details = doogie.age
species_details = doogie.species
print(dog_details)
print(species_details)