from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# many locations one weather
# one day many location
# one day many weathers

class Location(db.Model,SerializerMixin):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(55), nullable=False, unique=True)
    directions = db.Columns(db.String, nullable=False)
    coordinates = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Place Name {self.name}, in {self.directions} has coordinates {self.coordinates}"
    
     #relationship
    weather_id = db.Column(db.Integer, db.ForeignKey("weathers.id"))
    day_id = db.Column(db.Integer, db.ForeignKey("days.id"))
    
    
class Weather(db.Model):
    __tablename__ = "weathers"

    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)      #sunny, windy, etc
    weather_symbol = db.Column(db.String, nullable=False)  # a link probably?

    #relationship
    locations = db.relationship("Location",backref = "weather")
    # location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    day_id = db.Column(db.Integer, db.ForeignKey('days.id'))

    def __repr__(self):
        return f"Weather condition {self.condition}"
    
   

class Day(db.Model):
    __tablename__ = "days"

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(10))                              # Monday, Tuesday, etc
    date = db.Column(db.Date, default=db.func.current_date()) 
    time = db.Column(db.Time, default=db.func.current_time())
    time_of_day = db.Column(db.String(10))  #morning, afternoon, evening

    #rrelationship

    locations = db.relationship("Location",backref = "day")
    weathers = db.relationship('Weather', backref='day')



