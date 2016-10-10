import datetime as dt

from flask_login import UserMixin

from beerbackend.database import Column, Model, SurrogatePK, db, reference_col, relationship
from beerbackend.extensions import bcrypt

class Beer(SurrogatePK, Model):
    """It's a beer!"""

    __tablename__ = 'beers'
    beer_name = Column(db.String(80), unique=True, nullable=False)
    abv = Column(db.Numeric, nullable=False)
    hoppiness = Column(db.Numeric, nullable=False)
    bitterness = Column(db.Numeric, nullable=False)
    fruitiness = Column(db.Numeric, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, beer_name, abv, hoppiness, bitterness, fruitiness, **kwargs):
        db.Model.__init__(self, beer_name=beer_name, abv=abv, hoppiness=hoppiness,
                          bitterness=bitterness, fruitiness=fruitiness, **kwargs)

    def __repr__(self):
        """What makes a beer a beer, I say?"""
        return '<Beer({beer_name!r})>'.format(beer_name=self.beer_name)
