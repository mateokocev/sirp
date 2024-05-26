import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

CSV_FILE_PATH = "Melbourne_housing_PROCESSED.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',')

Base = declarative_base()


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    suburb = Column(String(100), nullable=False)
    postcode = Column(Integer, nullable=False)
    CouncilArea = Column(String(100), nullable=False)
    regionname = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

class Property(Base):
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    address = Column(String(90), nullable=False)
    landsize = Column(Integer)
    buildingArea = Column(String(50))
    yearBuilt = Column(String(50))
    propertycount = Column(Integer)
    parking_area = Column(String(50))

class HouseDetails(Base):
    __tablename__ = 'house_details'
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    rooms = Column(Integer)
    type = Column(String(1))
    bedroom = Column(Float)
    bathroom = Column(Float)
    car = Column(Float)

class Seller(Base):
    __tablename__ = 'seller'
    id = Column(Integer, primary_key=True)
    seller_name = Column(String(100))

class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    seller_id = Column(Integer, ForeignKey('seller.id'))
    dateOfSale = Column(Date, nullable=False)
    method = Column(String(2))
    price = Column(Integer)


engine = create_engine('mysql+pymysql://root:root@localhost:3306/melhouse', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def convert_date(date_str):
    return datetime.strptime(date_str, '%d/%m/%Y')

for index, row in df.iterrows():

    location = Location(suburb=row['Suburb'],
                        postcode=row['Postcode'],
                        CouncilArea=row['CouncilArea'],
                        regionname=row['Regionname'],
                        latitude=row['Latitude'],
                        longitude=row['Longitude'])
    session.add(location)
    session.flush()
    
    property = Property(address=row['Address'],
                        landsize=row['Landsize'],
                        buildingArea=row['BuildingArea'],
                        yearBuilt=row['YearBuilt'],
                        propertycount=row['Propertycount'],
                        parking_area=row['ParkingArea'])
    property.location_id = location.id
    session.add(property)
    session.flush()

    house_details = HouseDetails(rooms=row['Rooms'],
                                 type=row['Type'],
                                 bedroom=row['Bedroom'],
                                 bathroom=row['Bathroom'],
                                 car=row['Car'])
    house_details.property_id = property.id
    session.add(house_details)
    session.flush()

    seller = Seller(seller_name=row['SellerG'])
    session.add(seller)
    session.flush()

    sale = Sale(dateOfSale=convert_date(row['Date']),
                method=row['Method'],
                price=row['Price']
    )
    sale.property_id = property.id
    sale.seller_id = seller.id
    session.add(sale)
    session.flush()

session.commit()
session.close()
print("Tablice su popunjene.")