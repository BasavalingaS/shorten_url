from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class SessionHandler(object):

    def __init__(self):
        engine = create_engine(
            'postgres+psycopg2://postgres:postgres@localhost:5432/shorturls')
        Session = sessionmaker(bind=engine, expire_on_commit=False)
        self.session = Session()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
