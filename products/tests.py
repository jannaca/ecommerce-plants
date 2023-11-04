from django.test import TestCase
from .models import Category, Product
from django.utils import timezone
from decimal import Decimal

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            description='This is a description.'
        )
        
    def test_category_attributes(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'This is a description.')

    def test_category_str_method(self):
        expected_str = self.category.name
        self.assertEqual(str(self.category), expected_str)
    
class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            description='This is a test category.'
        )

        # Crea un producto para usar en las pruebas
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('10.99'),
            description='This is a test product.',
            image='media/products/test_product.jpg',
            created_date=timezone.now()
        )
        self.product.categories.add(self.category)

    def test_product_attributes(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, Decimal('10.99'))
        self.assertEqual(self.product.description, 'This is a test product.')
        self.assertEqual(self.product.image, 'media/products/test_product.jpg')
        self.assertIsNotNone(self.product.created_date)
        self.assertIn(self.category, self.product.categories.all())
    
    def test_product_str_method(self):
        expected_str = self.product.name
        self.assertEqual(str(self.product),expected_str)