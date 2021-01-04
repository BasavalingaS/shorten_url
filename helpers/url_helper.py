from sqlalchemy import create_engine
from session import SessionHandler
from models.urls import Urls
import random
from hashids import Hashids


class UrlHelper(object):

    def insert(self, input_url):
        with SessionHandler() as session:
            old_url = self.get(input_url=input_url)
            if old_url is None:
                short_url = self.generate_short_url(input_url)
                short_url_id = session.query(Urls).filter_by(short_url=short_url).first()
                while short_url_id is not None:
                    short_url = self.generate_short_url(input_url)
                    short_url_id = session.query(Urls).filter_by(short_url=short_url).first()
                url = Urls(url=input_url, short_url=short_url)
                session.add(url)
                session.commit()
                return url
            else:
                print("Records already exists in db")
                return old_url

    def get(self, url_id=None, input_url=None, short_url=None):
        with SessionHandler() as session:
            if url_id is not None:
                return session.query(Urls).filter_by(url_id=url_id).first()
            if input_url is not None:
                return session.query(Urls).filter_by(url=input_url).first()
            return session.query(Urls).filter_by(short_url=short_url).first()

    def delete(self, url_id):
        url = self.get(url_id)
        if url is not None:
            with SessionHandler() as session:
                session.delete(url)
                session.commit()
        return url

    @staticmethod
    def generate_short_url(url):
        return Hashids(salt=url).encode(random.randint(2, 999))


