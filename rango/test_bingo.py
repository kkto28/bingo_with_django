# 
# Bingo With Django Project Tests
# By Subhrajyoti Pradhan
# With assistance from tango with django 2 tests (https://github.com/maxwelld90/tango_with_django_2_code/blob/master/progress_tests/tests_chapter7.py)

# Once this is complete, run $ python manage.py test rango.test_bingo
# 
# 

#

import os
import inspect
from rango.models import Category, Page
from populate_rango import populate
from django.test import TestCase
from django.urls import reverse, resolve
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


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

#The following test has been taken from tests_chapter6.py of the aforementioned github page

class PopulationScriptTest(TestCase):
    """
    Tests to check if populate script functions
    """
    def setUp(self):
        populate()
    
    def test_page_objects_have_views(self):
        """
        Checks the basic requirement that all pages must have a positive view count.
        """
        pages = Category.objects.filter()

        for page in pages:
            self.assertTrue(len(page.description) < 500, f"{FAILURE_HEADER}The page '{page.name}' Please make sure that the description does NOT exceed 500 characters.{FAILURE_FOOTER}")

#The following test had been created by team Bingo

#class AdminAccessTest(TestCase):
