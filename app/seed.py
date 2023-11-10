from app import app
from models import db, Location, Weather, Day
from faker import Faker
from random import choice as rc
import random

fake = Faker()


with app.app_context():
    print("Deleting existing records...")
    Location.query.delete()
    Weather.query.delete()
    Day.query.delete()

    days = []

    for _ in range(10):
        day = Day(
            day=fake.date.weekday(),
            date=fake.date(),
            time_of_the_day=rc(["Morning", "Afternoon", "Evening"])
        )

        days.append(day)
    
    db.session.add_all(days)
    print("Days added successfully!")

    for _ in range(20):
        weather = Weather(
            temp=random.randint(0,40),
            condition=rc(["Sunny", "Windy", "Rainy", "Cloudy", "Calm"]),
        )