from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime

from .database import Base, session
# lets do a little of introspection to save us time
# writing functions to convert as dictionaries
import inspect
import re
class TableDictionaryMixin(object):
    """
    This Mixin ensures that all classes that derive from it contain
    a __tablename__ of the plural version of it's name converted into snake_case
    and id column set as a primary_key
    and as_dictionary method to facility api design
    """

    __mapper_args__ = { 'always_refresh': True }

    @staticmethod
    def camel_to_snake(name):
        snake = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake).lower()

    @declared_attr
    def __tablename__(cls):
        tablename = TableDictionaryMixin.camel_to_snake(cls.__name__)
        if tablename.endswith('y'):
            tablename = tablename[:-1] + 'ies'
        else:
            tablename += 's'
        return tablename

    id = Column(Integer, primary_key=True)

    def as_dictionary(self):
        # get all attributes
        attributes = inspect.getmembers(self, lambda attr:not(inspect.isroutine(attr)))
        # separate just the variables by name
        tvars = [attr for attr in attributes if not(
            (attr[0].startswith('__') and attr[0].endswith('__'))
            or (attr[0].startswith('_') or attr[0].endswith('_'))
            or (attr[0].startswith('metadata')) )]

        dictionary = {}
        for var in tvars:
            dictionary[var[0]] = var[1]

        return dictionary

# Asset related tables/structures
class Asset(TableDictionaryMixin, Base):
    pass

class AssetCategory(TableDictionaryMixin, Base):
    pass

class AssetType(TableDictionaryMixin, Base):
    pass

class AssetModel(TableDictionaryMixin, Base):
    pass

class AssetStatus(TableDictionaryMixin, Base):
    pass

class Location(TableDictionaryMixin, Base):
    pass

class LocationCategory(TableDictionaryMixin, Base):
    pass

class Department(TableDictionaryMixin, Base):
    pass

class Supplier(TableDictionaryMixin, Base):
    pass

class SupplierCategory(TableDictionaryMixin, Base):
    pass

class SystemUser(TableDictionaryMixin, Base):
    pass

