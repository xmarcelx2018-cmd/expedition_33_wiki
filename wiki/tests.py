from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import WikiEntry


class MyEntriesCategoryGroupingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='alice',
            password='secret123',
        )
        self.client.login(username='alice', password='secret123')

        self.character_entry = WikiEntry.objects.create(
            title='Aster',
            category='character',
            author=self.user,
            content='A brave explorer.'
        )
        self.weapon_entry = WikiEntry.objects.create(
            title='Night Fang',
            category='weapon',
            author=self.user,
            content='A sword from the ruins.'
        )
        self.location_entry = WikiEntry.objects.create(
            title='Old Ruins',
            category='location',
            author=self.user,
            content='A forgotten place.'
        )

    def test_my_entries_are_grouped_by_category(self):
        response = self.client.get(reverse('my_entries'))

        self.assertEqual(response.status_code, 200)
        grouped = response.context['entries_by_category']

        self.assertIn('character', grouped)
        self.assertIn('weapon', grouped)
        self.assertIn('location', grouped)

        self.assertEqual(list(grouped['character']), [self.character_entry])
        self.assertEqual(list(grouped['weapon']), [self.weapon_entry])
        self.assertEqual(list(grouped['location']), [self.location_entry])
