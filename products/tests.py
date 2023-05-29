from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from .models import Product

User = get_user_model()


class ProductViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1')
        cls.product1 = Product.objects.create(
            title='product1',
            description='this is product1 description',
            price=150000,

        )

    def test_product_list_view_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_url_by_name(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_url(self):
        response = self.client.get(f'/products/{self.product1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_url_by_name(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id]))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_content(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id]))
        self.assertContains(response, self.product1.title)
        self.assertContains(response, self.product1.description)
        self.assertContains(response, self.product1.price)

    def test_404_status_if_product_id_is_not_exist(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id + 1]))
        self.assertEqual(response.status_code, 404)

    def test_product_list_template(self):
        response = self.client.get(reverse('product_list'))
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_detail_template(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id]))
        self.assertTemplateUsed(response, 'products/product_detail.html')
