Library Management System (Cope-Old)
====================================

<quote>Forked from <link>https://github.com/sourabhv/Cope-Old</link></quote>
Upgraded for new Django 1.11

A digital library tool comprising of a public access view and equipped with fully functioning administrative tasks such as cataloging and circulation of books.


Requirements
============

Python 3.5+

Django 1.11+

Getting Started
===============

clone the repository
run python manage.py makemigrations
run python populate_book.py
run python populate_student.py
run python manage.py runserver to start the server
go to localhost:8000/search from a browser.