import faker

fake = faker.Faker()

def get_user(): #Générer un nom et prenom aléatoire
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):#Générer plusieurs noms et prenoms aléatoires
    # users = []
    # for _ in range(n):
    #    users.append(get_user())
    # return users
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    user = get_users(n = 5)
    print(user) 