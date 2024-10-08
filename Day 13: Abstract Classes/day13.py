from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author,price):
        self.title=title
        self.author=author
        self.price=price
        
    def display(self):
        print("Title: {:s}".format(title))
        print("Author: {:s}".format(author))
        print("Price: {:d}".format(price))
    

title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()
