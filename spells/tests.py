from django.test import TestCase
from django.urls import reverse

from .models import Spell


class SpellListViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        number_of_spells = 13
        for spell_num in range(number_of_spells):
            Spell.objects.create(name='Mors %s' % spell_num)

    def test_view_url_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_with_name(self):
        response = self.client.get(reverse('Spell:spell_list'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_ten(self):
        response = self.client.get(reverse('Spell:spell_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['spells']) == 10)


class SpellDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        Spell.objects.get_or_create(name='abracadabra', slug='abracadabra')
        self.read_detail_update = reverse('Spell:spell_detail', kwargs={'slug': 'abracadabra'})

    def test_detail(self):
        response = self.client.get(self.read_detail_update)
        self.assertEqual(response.status_code, 200)
