class People:
    def __init__(self):
        self.people_list = []
        self.index = 0
    
    def add_person(self, name):
        self.people_list.append(name)
        return self.people_list
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.people_list):
            person = self.people_list[self.index]
            self.index += 1
            return person
        else:
            raise StopIteration('Люди уже перебраны!')


people = People()

people.add_person('Lena')
people.add_person('Masha')
people.add_person('Dasha')

for i in people:
    print(i, end=' ')

# print(people.__next__())
# print(people.__next__())
# print(people.__next__())
# print(people.__next__())
