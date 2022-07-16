from dataclasses import dataclass, field, replace


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, default=20, repr=False)
    name: str
    job: str
    age: int
    strength: int = field(repr=False, default=15)
    
    def __post_init__(self):
        object.__setattr__(self, 'sort_index', 50)
        
        
 
def main()->None:
    
    person = Person("Peter Edward", "Software Developer", 35)
    person1 = Person("Peter Edward", "Software developer", 35)
    
    print(id(person))
    print(id(person1))
    
    print(person)
    print(person == person1)
    print(person == person1)
    



if __name__ == "__main__":
    main()