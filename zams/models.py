from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime

from .database import Base, session

# lets do a little of introspection to save us time
# writing functions to convert as dictionaries
import inspect

# ensure that all class/table/structures have a tablename matching
# their name in lowercase and respective plurarlalized form
# provide method that automatically generates a dictionary of it's attributes
class MetaTableDictionary(type):
    def as_dictionary(self):
        # get all attributes
        attributes = inspect.getmembers(self, lambda attr:not(inspect.isroutine(attr)))
        # separate just the variables by name
        tvars = [attr for attr in attributes if not(attr[0].startswith('__') and attr[0].endswith('__'))]
        # convert the tupples into a dictionary
        dictionary = {}
        for var in tvars:
            dictionary[var[0]] = var[1]

        return dictionary

    def __new__(cls, clsname, superclasses, attributedict):
        attributedict['as_dictionary'] = MetaTableDictionary.as_dictionary
        tablename = clsname.lower()
        if clsname.endswith('y'):
            tablename = tablename[:-1] + 'ies'
        else:
            tablename += 's'
        attributedict['__tablename__'] = tablename
        return type.__new__(cls, clsname, superclasses, attributedict)

    
# Asset related tables/structures
class Asset(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    
    pass

class AssetCategory(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    
    pass

class AssetType(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class AssetModel(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class AssetStatus(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class Location(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class LocationCategory(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class Department(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class Supplier(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class SupplierCategory(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

class SystemUser(Base, metaclass=MetaTableDictionary):

    id = Column(Integer, primary_key = True)
    pass

