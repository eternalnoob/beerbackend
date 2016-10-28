import datetime as dt

from flask_login import UserMixin

from beerbackend.database import Column, Model, SurrogatePK, db, reference_col, relationship
from beerbackend.extensions import bcrypt


families = {
    1: "ipa",
    2: "brown-ale",
    3: "pale-ale",
    4: "pale-lager",
    5: "pilsner",
    6: "amber-ale",
    7: "amber-lager",
    8: "dark-lager",
    9: "porter",
    10: "stout",
    11: "bock",
    12: "strong-ale",
    13: "wheat",
    14: "specialty"
}

class Beer(SurrogatePK, Model):
    """It's a beer!"""

    __tablename__ = 'beers'
    beer_name = Column(db.String(80), unique=True, nullable=False)
    abv = Column(db.Numeric, nullable=False, default=1)
    bitter = Column(db.Numeric, nullable=False, default=1)
    color = Column(db.Numeric, nullable=False, default=1)
    fruit = Column(db.Numeric, nullable=False, default=1)
    hoppy = Column(db.Numeric, nullable=False, default=1)
    malty = Column(db.Numeric, nullable=False, default=1)
    roasty = Column(db.Numeric, nullable=False, default=1)
    smoke = Column(db.Numeric, nullable=False, default=1)
    sour = Column(db.Numeric, nullable=False, default=1)
    spice = Column(db.Numeric, nullable=False, default=1)
    sweet = Column(db.Numeric, nullable=False, default=1)
    wood = Column(db.Numeric, nullable=False, default=1)
    family = Column(db.Integer, nullable=False, default=1)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    ratings = db.relationship('Rating', backref='beer',
                              lazy='dynamic')

    def __init__(self, beer_name, abv, bitter, color, fruit,
                 hoppy, malty, roasty, smoke, sour,
                 spice, sweet, wood, **kwargs):
        db.Model.__init__(self, beer_name=beer_name, abv=abv, bitter=bitter, color=color,
                          fruit=fruit, hoppy=hoppy, malty=malty, roasty=roasty,
                          smoke=smoke, sour=sour, spice=spice, sweet=sweet,
                          wood=wood, **kwargs)

    def __repr__(self):
        """What makes a beer a beer, I say?"""
        return '<Beer({beer_name!r})>'.format(beer_name=self.beer_name)

    def to_data(self):
        return {
            "name": self.beer_name,
            "abv": self.abv,
            "bitter": self.bitter,
            "color": self.color,
            "fruit": self.fruit,
            "hoppy": self.hoppy,
            "malty": self.malty,
            "roasty": self.roasty,
            "sour": self.sour,
            "spice": self.spice,
            "sweet": self.sweet,
            "wood": self.wood,
            "id": self.id,
            "family": families.get(self.family, None)
        }

    def get_family(self):
        return families.get(self.family, None)
