from django.test import TestCase
from .models import Book
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
class BookAPITests(APITestCase):
    #Setting up of the required tests

    def SetUp(self):
        self.user = User.objects.create_user(username='test_user', password='test123#')
        self.client.login(username="test_user", password="test123")
       
        self.book = Book.objects.create(title='Test_Book', publication_year=2019, author='Orwell')
        
    def test_get_books(self):
        # Testing if an authenticated user can get the list of books
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)


    def test_unauthenticated_user(self):
        # Check if an authenticated user can access the list of books
        self.client.logout()
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)  

    def test_unauthenticated_user_create(self):
        # Check if an authenticated user can access create books.
        self.client.logout()
        response = self.client.get("/api/books/create")
        self.assertEqual(response.status_code, 401)  

    def test_create_book_authenticated_user(self):
        #Check if an authenticated user can create books. 
        self.client.login(username='test_user', password='test123')
        data = {'title': 'Test_Book', 'publication_year': 2019, 'author': 'Orwell'}

        response = self.client.post(self.create_url, data)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Book.objects.get(pk=response.data['id']).title, 'Test_Book')