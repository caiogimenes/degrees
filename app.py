class Person():
    def __init__(self, nome):
        self.name = nome
        self.parents=[]
        self.children=[]
    
    def add_parents(self, node):
        if self.parents == 2:
            return KeyError
        node.add_children(self)
        return self.parents.append(node)
    
    def add_children(self, nome):
        return self.children.append(nome)
    
    def distance(self, node):
        total=0
        if node in self.children or self.parents:
            return total
        return node

def main():
    names = ["caio", "celino", "antonio", "francisco"]
    tree = [Person(name) for name in names]
    
    for i in range(0, len(tree) - 1):
        tree[i].add_parents(tree[i+1])
    
    for person in tree:
        print("Nome: ", person.name)
        for parent in person.parents:
            print("Pais: ", parent.name)
        for child in person.children:
            print("Filhos: ", child.name)
        print("=================================")
    
    
main()