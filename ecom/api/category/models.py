from django.db import models

"""
    Steps while working with a single app and creating it's API

    Overview

    1. CREATE A MODEL

    2. REGISTER IN ADMIN

    3. serializers.py FILE TO SERIALIZE DATA IN JSON

    4. VIEWS TO GET ALL CATEGORIES (ONLY FOR THIS APP)

    5. SETUP URL

    - Create two files in your app
        1. serializers.py
        2. urls.py
    - Create a model for your purpose
    - Once model class is ready, goto admin.py and register it
    - Add some data to your category
    - Override __str__ to view 'name' given
    - Prepare your serialization
    - Create a view for your API with help of Model & Serializers
    - Setup URL
"""
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name