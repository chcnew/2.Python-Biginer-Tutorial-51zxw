class parent:
    def __init__(self):
        self.name = 'parent'

    def getName(self):
        print(self.name)

    class child:
        def __init__(self):
            self.name = 'child'

        def getName(self):
            print(self.name)


if __name__ == '__main__':
    p = parent()
    c = parent.child()
    p.getName()
    c.getName()
