from dataclasses import dataclass #Pour éviter de répéter les paramètres avec self
from typing import ClassVar #Pour les attributs de classe

@dataclass
class User:
    first_name : str #Attribut d'instance
    last_name : str
    c : ClassVar[int] #Attribut de classe


patrick = User(first_name="Patrick", last_name="Smith")
print(User.__dict__)