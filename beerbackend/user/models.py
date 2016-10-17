# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from beerbackend.database import Column, Model, SurrogatePK, db, reference_col, relationship
from beerbackend.extensions import bcrypt
from itsdangerous import(TimedJSONWebSignatureSerializer as srl,
                         BadSignature, SignatureExpired)
import os


class Role(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)


class User(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""

        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, value):
        """Check password."""
        print(value)
        return bcrypt.check_password_hash(self.password, value)

    def generate_auth_token(self, expire_time=None):
        s = srl(os.environ.get('BEERBACKEND_SECRET',default=None), expires_in=expire_time)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = srl(os.environ.get('BEERBACKEND_SECRET',default=None))
        try:
            data=s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

