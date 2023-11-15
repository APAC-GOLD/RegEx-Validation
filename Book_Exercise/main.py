from pydantic import BaseModel
from classes.Author import Author
from classes.BookItem import BookItem
from classes.BookStore import BookStore

my_author1 = Author(name= "Michael Jackson",
                    author_id= "MJAC-1984")

print(my_author1)

my_author2 = Author(name= "Justin Biber", 
                   author_id= "JBAB-1995")
print(my_author2)

my_bookitem1 = BookItem(name= "Alice in Wonderland",
                        author= my_author1,
                        year_published= 2025)
print(my_bookitem1)
my_bookitem2 = BookItem(name= "Rage Against the Machine", 
                       author= my_author2, 
                       year_published= 2023)
print(my_bookitem2)

my_bookstore1 = BookStore(name= "Mac Donalds", 
                          book_shelf= [my_bookitem1, my_bookitem2])
print(my_bookstore1)

