from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe

# recipe creations should work only if authenticated
# recipe edit only -- by the author
# recipe delete -- only by author
# recipe visible for all users
# uhauthenticated users got redirect


# SHOULD work only for authenticated users (all mandatory inputs )
class RecipeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe_data = {
            'title': 'Test Recipe',
            'description': 'Just a test.',
            'cooking_time': '30',
        }

# to confirm if the recipe list  viewable  --> not auth
    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_recipe_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('recipe_create'), self.recipe_data)
        self.assertEqual(response.status_code, 302)  # should redirect
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.first().author, self.user)

    def test_create_recipe_unauthenticated(self):
        response = self.client.post(reverse('recipe_create'), self.recipe_data)
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(Recipe.objects.count(), 0)

# auth users can only edit/delete their recipes
    def test_edit_own_recipe(self):
        self.client.login(username='testuser', password='testpass')
        recipe = Recipe.objects.create(title='Old Title', description='Old', author=self.user)
        response = self.client.post(reverse('recipe_edit', args=[recipe.id]), {
            'title': 'New Title',
            'description': 'Updated',
            'cooking_time': '30',
        })
        recipe.refresh_from_db()
        self.assertEqual(recipe.title, 'New Title')

    def test_edit_other_users_recipe(self):
        other_user = User.objects.create_user(username='other', password='pass')
        recipe = Recipe.objects.create(title='Old', description='Old', author=other_user)
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('recipe_edit', args=[recipe.id]), {
            'title': 'Hacked Title',
            'description': 'Oops',
        })
        recipe.refresh_from_db()
        self.assertNotEqual(recipe.title, 'Hacked Title')

    def test_delete_own_recipe(self):
        self.client.login(username='testuser', password='testpass')
        recipe = Recipe.objects.create(title='ToDelete', description='bye', author=self.user)
        response = self.client.post(reverse('recipe_delete', args=[recipe.id]))
        self.assertFalse(Recipe.objects.filter(id=recipe.id).exists())

    def test_delete_other_users_recipe(self):
        other_user = User.objects.create_user(username='other', password='pass')
        recipe = Recipe.objects.create(title='KeepMe', description='nope', author=other_user)
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('recipe_delete', args=[recipe.id]))
        self.assertTrue(Recipe.objects.filter(id=recipe.id).exists())

