import xml.etree.ElementTree as Et

tree = Et.parse("Book.xml")
books_list = tree.findall("Books/*")
for book in books_list:
    print(book.tag, book.attrib)
    for book_content in book:
        print('\t', book_content.tag, ': ', book_content.text)

# get book with title
book_with_title = tree.find("Books/Book[Title = 'The Colour of Magic']")
print("book_with_title 'The Colour of Magic' is:\n", book_with_title)

# get book with id
book_with_id = tree.find("Books/Book[@id = '1']")
print("book_with_id 1 is:\n", book_with_id)

# get book with index
book_with_index = tree.find("Books/Book[2]")
print("book_with_index [2] is:\n", book_with_index)

# get last book with Book tag name
the_last_book = tree.find("Books/Book[last()]")
print("the_last_book is:\n", the_last_book)
