from django.db import models

# Create your models here.
# crud_app/models.py

class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
