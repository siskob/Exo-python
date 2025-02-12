from faker import Faker

fake = Faker(locale="fr_FR")

for _ in range(10):
    print(fake.numerify(text = "%%%-%-%%%%-%%%%-%%%-##")) # %= 1-9; # = 0-9
    print(fake.bothify(text = "Product number : ????-####")) # ?= a-z ; # = 0-9
    print("hello")