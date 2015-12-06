from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sess = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
