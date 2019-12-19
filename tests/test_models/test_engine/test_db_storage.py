#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from os import getenv
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.storage = DBStorage()
        # reload to get the HBNB_ENV = test and erase the existing ones
        cls.storage.reload()
        cls.state = State()
        cls.state.name = "Santander"
        cls.state.save()
        cls.city = City()
        cls.city.state_id = cls.state.id
        cls.city.name = "Velez"
        cls.city.save()
        cls.user = User()
        cls.user.first_name = "Jhonathan"
        cls.user.last_name = "Pericles"
        cls.user.password = "solo Perez"
        cls.user.email = "1234@yahoo.com"
        cls.user.save()
        cls.place = Place()
        cls.place.city_id = cls.city.id
        cls.place.user_id = cls.user.id
        cls.place.name = "Lovely_place"
        cls.place.number_rooms = 3
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 6
        cls.place.price_by_night = 120
        cls.place.latitude = 37.773972
        cls.place.longitude = -122.431297
        cls.place.save()
        cls.review = Review()
        cls.review.place_id = cls.place.id
        cls.review.user_id = cls.user.id
        cls.review.text = "Amazing_place,_huge_kitchen"
        cls.review.save()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_pep8_DBStorage(self):
        """Test Pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_all_DBStorage(self):
        """Test same size between storage() and existing db"""
        User = getenv("HBNB_MYSQL_USER")
        Passwd = getenv("HBNB_MYSQL_PWD")
        Db = getenv("HBNB_MYSQL_DB")
        Host = getenv("HBNB_MYSQL_HOST")
        # change the HBNB_ENV in order to no erase more
        # and use the tables created in SetUpClass
        os.environ['HBNB_ENV'] = 'No_erase'
        storage = DBStorage()
        storage.reload()
        db = MySQLdb.connect(host=Host, user=User,
                             passwd=Passwd, db=Db,
                             charset="utf8")
        query = db.cursor()
        dic = storage.all()
        lis = []
        query.execute("SHOW TABLES")
        output = query.fetchall()
        if len(output) != 0:
            for elem in output:
                if elem[0] != "place_amenity":
                    query.execute("SELECT * FROM {}".format(elem[0]))
                    salida = query.fetchall()
                    if len(salida) != 0:
                        for obj in salida:
                            lis.append(obj)
            self.assertEqual(len(dic), len(lis))
        else:
            self.assertEqual(len(dic), 0)
        query.close()
        db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_quantity_amenities(self):
        """Test same size between storage(amenities) and existing db"""
        User = getenv("HBNB_MYSQL_USER")
        Passwd = getenv("HBNB_MYSQL_PWD")
        Db = getenv("HBNB_MYSQL_DB")
        Host = getenv("HBNB_MYSQL_HOST")
        os.environ['HBNB_ENV'] = 'No_erase'
        storage = DBStorage()
        storage.reload()
        db = MySQLdb.connect(host=Host, user=User,
                             passwd=Passwd, db=Db,
                             charset="utf8")
        query = db.cursor()
        dic = storage.all(Amenity)
        lis = []
        query.execute("SHOW TABLES")
        output = query.fetchall()
        if len(output) != 0:
            for elem in output:
                if elem[0] == "amenities":
                    query.execute("SELECT * FROM {}".format(elem[0]))
                    salida = query.fetchall()
                    if len(salida) != 0:
                        for obj in salida:
                            lis.append(obj)
            self.assertEqual(len(dic), len(lis))
        else:
            self.assertEqual(len(dic), 0)
        query.close()
        db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_quantity_city(self):
        """Test same size between storage(city) and existing db"""
        User = getenv("HBNB_MYSQL_USER")
        Passwd = getenv("HBNB_MYSQL_PWD")
        Db = getenv("HBNB_MYSQL_DB")
        Host = getenv("HBNB_MYSQL_HOST")
        os.environ['HBNB_ENV'] = 'No_erase'
        storage = DBStorage()
        storage.reload()
        db = MySQLdb.connect(host=Host, user=User,
                             passwd=Passwd, db=Db,
                             charset="utf8")
        query = db.cursor()
        dic = storage.all(City)
        lis = []
        query.execute("SHOW TABLES")
        output = query.fetchall()
        if len(output) != 0:
            for elem in output:
                if elem[0] == "cities":
                    query.execute("SELECT * FROM {}".format(elem[0]))
                    salida = query.fetchall()
                    if len(salida) != 0:
                        for obj in salida:
                            lis.append(obj)
            self.assertEqual(len(dic), len(lis))
        else:
            self.assertEqual(len(dic), 0)
        query.close()
        db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add(self):
        """Test same size between storage(city) and existing db"""
        User = getenv("HBNB_MYSQL_USER")
        Passwd = getenv("HBNB_MYSQL_PWD")
        Db = getenv("HBNB_MYSQL_DB")
        Host = getenv("HBNB_MYSQL_HOST")
        os.environ['HBNB_ENV'] = 'No_erase'
        storage = DBStorage()
        storage.reload()
        db = MySQLdb.connect(host=Host, user=User,
                             passwd=Passwd, db=Db,
                             charset="utf8")
        query = db.cursor()
        dic = storage.all(State)
        lis = []
        query.execute("INSERT INTO states (id, created_at, updated_at, name)\
                      VALUES (578, '2019-05-11 00:14:40',\
                      '2019-05-11 00:14:40', '{}')".format("boyaca"))
        query.execute("SHOW TABLES")
        output = query.fetchall()
        if len(output) != 0:
            for elem in output:
                if elem[0] == "states":
                    query.execute("SELECT * FROM {}".format(elem[0]))
                    salida = query.fetchall()
                    if len(salida) != 0:
                        for obj in salida:
                            lis.append(obj)
            self.assertEqual(len(dic) + 1, len(lis))
        else:
            self.assertEqual(len(dic), 0)
        query.close()
        db.close()

if __name__ == "__main__":
    unittest.main()
