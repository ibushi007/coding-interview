from rest_framework.test import APITestCase
from rest_framework import status
from api.models.company import Company
from api.models.category import Category

class CategoryViewTests(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.category = Category.objects.create(company=self.company, name="Parent Category")

    def test_list(self):
        self.assertEqual(self.client.get('/api/categories/').status_code, 200)
        
    def test_retrieve(self):
        self.assertEqual(self.client.get(f'/api/categories/{self.category.id}/').status_code, 200)

    def test_create(self):
        response = self.client.post('/api/categories/', {
            'company': str(self.company.id), 
            'name': 'New Category'
            })
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        response = self.client.put(f'/api/categories/{self.category.id}/', {
            'company': str(self.company.id),
            'name': 'Updated Category'
            })
        self.assertEqual(response.status_code, 200)

    def test_destroy(self):
        response = self.client.delete(f'/api/categories/{self.category.id}/')
        self.assertEqual(response.status_code, 204)
