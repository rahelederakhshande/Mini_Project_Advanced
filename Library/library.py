class Library:
    def __init__(self, obj):
        self.obj = obj
        self.entities = {
            "members": {},
            "books": {},
            "librarians": {}
        }

    def __str__(self):
        return str(len(self.entities['members']))
    
    def add_data(self, obj):
        type_ = type(obj).__name__.lower() + "s"
        self.entities[type_][obj.id_] = obj

    @staticmethod
    def show_info(data):
        for v in data.values():
            print(v)
        if not data:
            print('Empty')

    def display(self, obj_type = None):
        if obj_type:
            obj_type += "s"
            try:
                data = self.entities[obj_type]
            except:
                print("Error")
            else:
                print("\n " + "_ " * 10 + obj_type + "_ " * 10)
        else:
            for key, ent in self.entities.items():
                print("\n " + "_ " * 10 + key + "_ " * 10)
                self.show_info(ent)
    
    def search(self, obj_type, criteria):
        try:
            data = self.entities[obj_type]
        except KeyError:
            print(f"Error: {obj_type} not found")
            return

        results = [obj for obj in data.values() if criteria(obj)]

        if results:
            print(f"\nSearch results for {obj_type}:")
            self.show_info({obj.id_: obj for obj in results})
        else:
            print(f"No results found for {obj_type}")
                