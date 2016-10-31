# -------
# imports
# -------

from unittest import main, TestCase
from app.models import Company, FinancialOrg, Person, City

from flask_sqlalchemy import SQLAlchemy
from __init__ import app

# initialize database object
db = SQLAlchemy(app)


# -----------
# TestCompany
# -----------

class TestCompany(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp():
        db.create_all()

    def tearDown():
        db.session.close()
        db.drop_all()

    # -------
    # Company
    # -------

    def test_company(self):
        example = Company("Airbnb",
                          "Founded in August 2008 and based in San Francisco, California, Airbnb is a trusted community marketplace for people to list, discover, and book unique spaces around the world - online or from a mobile phone. Whether an apartment for a night, a castle for a week, or a villa for month, Airbnb connects people to unique travel experiences, at any price point, in more than 26,000 cities and 192 countries. And with world-class customer service and a growing community of users, Airbnb is the easiest way for people to monetize their extra space and showcase it to an audience of millions.",
                          [], "San Francisco", ["Youniversity Ventures"], "airbnb", "http://airbnb.com")

        self.assertEqual(example.city, "San Francisco")
        self.assertEqual(example.twitter, "airbnb")

        db.session.add(example)
        db.session.commit()
        companies = Company.query.all()

        self.assertEqual(len(companies), 1)
        self.assertEqual(example.dictionary(), companies[1].dictionary)


# ----------------
# TestFinancialOrg
# ----------------

class TestFinancialOrg(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp():
        db.create_all()

    def tearDown():
        db.session.close()
        db.drop_all()

    # ------------
    # FinancialOrg
    # ------------

    def test_financial_org(self):
        example = FinancialOrg("Founders Fund",
                               "Founders Fund is a San Francisco based venture capital firm which invests at every stage in companies with revolutionary technologies.  The firm's five partners, Peter Thiel, Sean Parker, Ken Howery, Luke Nosek, and Brian Singerman have been founders of or early investors in numerous well-known companies such as Facebook, PayPal, Napster, and Palantir Technologies. Founders Fund was formed in 2005 and has launched four funds to date with more than $1 billion in aggregate capital under management.",
                               "San Francisco", ["Space Exploration Technologies"], "foundersfund",
                               "http://www.foundersfund.com")

        self.assertEqual(example.city, "San Francisco")
        self.assertEqual(example.twitter, "foundersfund")

        db.session.add(example)
        db.session.commit()
        financial_orgs = FinancialOrg.query.all()

        self.assertEqual(len(financial_orgs), 1)
        self.assertEqual(example.dictionary(), financial_orgs[1].dictionary)


# ----------
# TestPerson
# ----------

class TestPerson(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp():
        db.create_all()

    def tearDown():
        db.session.close()
        db.drop_all()

    # ------
    # Person
    # ------

    def test_Person(self):
        example = Person("Brian Chesky",
                         "Brian drives Airbnb's vision, strategy and growth. Always pushing the status quo, Brian aims to disrupt the industry with ideas that change the way people live. To grasp the full impact and experience of Airbnb, Brian rid himself of an apartment and has been living in the homes of the Airbnb community since June of 2010. He is committed to assembling a passionate, top tier team to deliver on this promise. Before Airbnb, Brian ran an industrial design shop in Los Angeles; even these days he is rarely seen without a drafting pen and sketch book in hand. Brian holds a Bachelor of Fine Arts in industrial design from the Rhode Island School of Design. He believes that what sets the company apart is the access to space that would otherwise be off limits, and haunted or not, he would be honored to someday stay in the Lincoln Bedroom through the site.",
                         "", ["Airbnb"], ["Co-founder & CEO"], "bchesky")

        self.assertEqual(example.city, "")
        self.assertEqual(example.twitter, "bchesky")

        db.session.add(example)
        db.session.commit()
        people = Person.query.all()

        self.assertEqual(len(people), 1)
        self.assertEqual(example.dictionary(), people[1].dictionary)


# --------
# TestCity
# --------

class TestCity(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp():
        db.create_all()

    def tearDown():
        db.session.close()
        db.drop_all()

    # ----
    # City
    # ----

    def test_city(self):
        example = City("Los Angeles", "CA", "USA", ["Space Exploration Technologies"], [], ["Elon Musk"])

        self.assertEqual(example.state, "CA")
        self.assertEqual(example.country, "USA")

        db.session.add(example)
        db.session.commit()
        cities = City.query.all()

        self.assertEqual(len(cities), 1)
        self.assertEqual(example.dictionary(), cities[1].dictionary)

# ----
# About
# ----

class TestAbout(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp():
        db.create_all()

    def tearDown():
        db.session.close()
        db.drop_all()

    # ----
    # About
    # ----

    def test_about(self):
        # TODO
        """
        Test about page
        """
        example = City("Los Angeles", "CA", "USA", ["Space Exploration Technologies"], [], ["Elon Musk"])

        self.assertEqual(example.state, "CA")
        self.assertEqual(example.country, "USA")

        db.session.add(example)
        db.session.commit()
        cities = City.query.all()

        self.assertEqual(len(cities), 1)
        self.assertEqual(example.dictionary(), cities[1].dictionary)


# ----
# main
# ----

if __name__ == "__main__":
    main()
