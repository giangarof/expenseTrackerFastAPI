income = [
    {"name": "salary", "ammount": 4000},
    {"name": "freelance", "ammount": 1000},
]


class Income:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name


mylist = [Income(1, "first"), Income(2, "second"), Income(3, "third")]
# print(mylist)

for x in range(len(mylist)):
    print(x.id)
