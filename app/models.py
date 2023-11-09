from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(55), nullable=False, unique=True)
    directions = db.Columns(db.String, nullable=False)
    coordinates = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Place Name {self.name}, in {self.directions} has coordinates {self.coordinates}"
    
     #relationship
    weathers = db.relationship("Weather", backref="location")
    days = db.relationship("Day", backref = "location")
    
    
class Weather(db.Model):
    __tablename__ = "weather"

    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)      #sunny, windy, etc
    weather_symbol = db.Column(db.String, nullable=False)  # a link probably?

    #relationship
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
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
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    weather = db.relationship('Weather', uselist=False, backref='day')