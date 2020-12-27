from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Urls(Base):
    __tablename__ = 'urls'
    url_id = Column('id', Integer, Sequence('urls_id_seq'), primary_key=True)
    url = Column(String(50))
    short_url = Column(String(50))

    def __repr__(self):
        return "<Urls(url='%s', short_url='%s')>" % (
            self.url, self.short_url)
