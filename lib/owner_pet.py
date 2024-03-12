class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of 'Owner' class.")

        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")

        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                owner_pets.append(pet)
        return owner_pets

    def add_pet(self, pet):
        if isinstance (pet, Pet):
            pet.owner = self
        else: 
            raise Exception("Pet must be an instance of 'Pet' class.")

    def get_sorted_pets(self):
        sorted_pets = sorted (self.pets(), key=self.pet_name)
        return sorted_pets

    def pet_name(self, pet):
        return pet.name