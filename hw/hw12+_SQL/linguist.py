from sqlalchemy import sessionmaker, create_engine, Column, Integer, String, ForeignKey, or_
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///linguist.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()



class User (Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Deck (Base):
    __tablename__='decks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

class Card (Base):
    __tablename__='cards'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)



def user_create(name, email, password):
    session = Session()
    new_user = User(name=name, email=email, password=password) 
    session.add(new_user)
    session.commit()
    return new_user

def user_get_by_id(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    return user

def user_update_name(user_id, name):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        user.name = name
        session.commit()
        return user
    return None

def user_change_password(user_id, old_password, new_password):
    session = Session()
    user = session.query(User).filter_by(id=user_id, password = old_password).first()    
    
    if user:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        session.delete(user)
        session.commit()
        return True
    return False
    
def deck_create(name, user_id):
    session = Session()
    new_deck = Deck(name=name, user_id=user_id)
    session.add(new_deck)
    session.commit()
    return new_deck

def deck_get_by_id(deck_id):
    session = Session()
    deck = session.query(Deck).filter_by(id=deck_id).first()
    return deck

def deck_update(deck_id, name):
    session = Session()
    deck = session.query(Deck).filter_by(id=deck_id).first()

    if deck:
        deck.name = name
        session.commit()
        return deck
    return None

def deck_delete_by_id(deck_id):
    session = Session()
    deck = session.query(Deck).filter_by(id=deck_id).first()

    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False

def card_create(user_id, word, translation, tip):
    session = Session()
    new_card = Card(user_id = user_id, word = word, translation = translation, tip = tip)
    session.add(new_card)
    session.commit()
    return new_card

def card_get_by_id(card_id):
    session = Session()
    card = session.query(Card).filter_by(id = card_id).first()
    return card

def card_filter(sub_word):
    session = Session()
    results = session.query(Card).filter(
    or_(
        Card.word.like('%' + sub_word + '%'),
        Card.translation.like('%' + sub_word + '%'),
        Card.tip.like('%' + sub_word + '%')
    )).all()
    return results

def card_update(card_id, word=None, translation=None, tip=None):
    session = Session()
    new_card = session.query(Card).filter_by(id = card_id).first()

    if new_card:
        if word is not None:
            new_card.word = word
        if tip is not None:
            new_card.tip = tip
        if translation is not None:
            new_card.translation = translation
        session.commit()
        return new_card
    return None

def card_delete_by_id(card_id):
    session = Session()
    card = session.query(Card).filter_by(id = card_id).first()
    if card:
        session.delete(card)
        session.commit
        return True
    return False

Base.metadata.create_all(engine)