from mongoengine import *


class Product(Document):
    name = StringField(max_length=200)
    description = StringField()
    category = StringField()
    price = FloatField(required=True)
    brand = StringField()
    quantity = IntField()

    def __str__(self):
        return self.name
