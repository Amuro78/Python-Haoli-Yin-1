"""Module 11-1"""
class Publication:
    def __init__(self,name):
        self.name=name

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author=author
        self.page_count=page_count
        Publication.__init__(self,name)

    def print_information(self):
        print("Book information:")
        print(f"Book name: {self.name}")
        print(f"Author: {self.author}")
        print(f"page count: {self.page_count}")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.chief_editor=chief_editor
        Publication.__init__(self,name)

    def print_information(self):
        print("\nMagazine information:")
        print(f'Magazine name: {self.name}')
        print(f"Chief editor: {self.chief_editor}")




book=Book("Compartment No. 6","Rosa Liksom",192)
magazine=Magazine("Donald Duck","Aki Hyyppä")

book.print_information()
magazine.print_information()