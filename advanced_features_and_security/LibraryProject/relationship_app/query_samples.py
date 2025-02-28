from relationship_app.models import Library, Book, Author, Librarian

author_name = 'filler'

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)


library_name = 'empty'

library = Library.objects.get(name=library_name)
books_in_library = Library.books.all()

print(f"Books in {library_name}:")
for book in books_in_library:
    print(book.title)

library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"The Librarian for {library_name} is {librarian.name}")
