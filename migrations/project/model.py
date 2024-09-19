from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    @classmethod
    def create(cls, session, product_name, type, price):
        product = cls(product_name=product_name, type=type, price=price)
        session.add(product)
        session.commit()
        return product

    @classmethod
    def delete(cls, session, product_id):
        product = session.query(cls).filter_by(id=product_id).first()
        if product:
            session.delete(product)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, product_id):
        return session.query(cls).filter_by(id=product_id).first()
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    purchases = relationship("Purchased", back_populates="user")

    @classmethod
    def create(cls, session, name, contact):
        user = cls(name=name, contact=contact)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def delete(cls, session, user_id):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).filter_by(id=user_id).first()
    
class Purchased(Base):
    __tablename__ = 'purchased'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_name = Column(String, ForeignKey('products.product_name'), nullable=False )
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_cost = Column(Float, nullable=False)

    user = relationship("User", back_populates="purchases")

    @classmethod
    def create(cls, session, user_id, product_name, price, quantity):
        total_cost = price * quantity
        purchase = cls(user_id=user_id, product_name=product_name, price=price, quantity=quantity, total_cost=total_cost)
        session.add(purchase)
        session.commit()
        return purchase

    @classmethod
    def delete(cls, session, purchase_id):
        purchase = session.query(cls).filter_by(id=purchase_id).first()
        if purchase:
            session.delete(purchase)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, purchase_id):
        return session.query(cls).filter_by(id=purchase_id).first()

def setup_db():
    engine = create_engine('sqlite:///car_shop.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()