# 
# Bingo With Django Project Tests
# By Subhrajyoti Pradhan
# run $ python manage.py test rango.test_bingo

import os
import inspect
from rango.models import Category, Page
from populate_rango import populate
from django.test import TestCase
from django.urls import reverse, resolve
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

#Testing case 1, 2, 3 to check Category with additional fields for Bingo
class Category_presence_test(TestCase):
    """
    Do the Form classes exist, and do they contain the correct instance variables?
    """
    def test_module_exists(self):
        """
        Tests that the forms.py module exists in the expected location.
        """
        project_path = os.getcwd()
        rango_app_path = os.path.join(project_path, 'rango')
        forms_module_path = os.path.join(rango_app_path, 'forms.py')

        self.assertTrue(os.path.exists(forms_module_path), f"{FAILURE_HEADER}Couldn't find forms.py module.{FAILURE_FOOTER}")
    
    def test_category_form_class(self):
        """
        Does the CategoryForm implementation exist, and does it contain the correct instance variables?
        """
        # Check that we can import CategoryForm.
        import rango.forms
        self.assertTrue('CategoryForm' in dir(rango.forms), f"{FAILURE_HEADER}The class CategoryForm could not be found in Rango's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from rango.forms import CategoryForm
        category_form = CategoryForm()

        # Do you correctly link Category to CategoryForm?
        self.assertEqual(type(category_form.__dict__['instance']), Category, f"{FAILURE_HEADER}The CategoryForm does not link to the Category model. Have a look in the CategoryForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")

        # Now check that all the required fields are present, and of the correct form field type.
        fields = category_form.fields

        expected_fields = {
            'name': django_fields.CharField,
            'views': django_fields.IntegerField,
            'likes': django_fields.IntegerField,
            'slug': django_fields.CharField,
            'type' : django_fields.CharField,
            'description' : django_fields.CharField,
            'recommend_buy' : django_fields.IntegerField,
            'url' : django_fields.URLField,
            'picture' : django_fields.ImageField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your CategoryForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in CategoryForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")

    def test_empty_category(self):
        """
        Adds a Category without pages; checks to see what the response is.
        """
        category = Category.objects.get_or_create(name='Test Category')
        response = self.client.get(reverse('rango:show_category', kwargs={'category_name_slug': 'test-category'}))
        lookup_string = '<strong>No pages currently in category.</strong>'
        self.assertIn(lookup_string, response.content.decode(), r"Error")


#Testing case 4 to check new population script & Category content
class PopulationScriptTest(TestCase):
    """
    Tests to check if populate script functions
    """
    def setUp(self):
        populate()
    
    def test_watch_description(self):
        """
        Checks proper content for watch categories.
        """
        watches = Category.objects.filter()

        for watch in watches:
            self.assertTrue(len(watch.description) < 500, f"{FAILURE_HEADER}The watch catalogue '{watch.name}' Please make sure that the description does NOT exceed 500 characters.{FAILURE_FOOTER}")
            self.assertTrue(watch.likes > 0, f"{FAILURE_HEADER}The watch catalogue '{watch.name}' Please make sure that number of likes do exist.{FAILURE_FOOTER}")
            self.assertTrue(watch.views > 0, f"{FAILURE_HEADER}The watch catalogue '{watch.name}' Please make sure that number of view do exist.{FAILURE_FOOTER}")