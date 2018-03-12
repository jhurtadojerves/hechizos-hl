import json

from django.test import TestCase
from django.urls import reverse

from spells.models import Spell


class TestAPI(TestCase):

    def setUp(self):
        Spell.objects.get_or_create(
            name='abracadabra',
            slug='abracadabra'
        )
        Spell.objects.get_or_create(
            name='abracadabra2',
            slug='abracadabra2'
        )

        self.read_url = reverse('Api:list')
        self.detail_url = reverse('Api:detail', kwargs={'slug': 'abracadabra'})

    def test_list(self):
        response = self.client.get(self.read_url)

        self.assertContains(response, 'abracadabra')
        self.assertContains(response, 'abracadabra2')

    def test_detail(self):
        response = self.client.get(self.detail_url)
        data = json.loads(response.content.decode('utf-8'))
        content = {
            'name': 'abracadabra',
            'battles': True,
            'method': 'Verbal',
            'object': 'Con Varita',
            'description': '',
            'range': [],
            'type': 'Efecto'
        }

        self.assertEquals(data, content)
