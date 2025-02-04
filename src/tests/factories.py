import factory
from faker import Faker
from django.contrib.gis.geos import Point
from categories.models import Category
from locations.models import Location
from django.contrib.auth import get_user_model

fake = Faker()

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    password = factory.PostGenerationMethodCall("set_password", "password")

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")
    slug = factory.Sequence(lambda n: f"category-{n}")



class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.Sequence(lambda n: f"Location {n}")
    slug = factory.LazyAttribute(lambda obj: obj.name.lower().replace(" ", "-"))
    description = factory.Faker("sentence", nb_words=10)
    point = factory.LazyFunction(
        lambda: Point(
            float(fake.longitude()),
            float(fake.latitude())
        )
    )
    address = factory.Faker("address")
    city = factory.Faker("city")
    region = factory.Faker("state")
    postal_code = factory.Faker("postcode")