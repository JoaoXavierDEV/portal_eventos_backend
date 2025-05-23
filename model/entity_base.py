from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Configuração da sessão do SQLAlchemy
db_session = scoped_session(sessionmaker())

Base = declarative_base()

Base.query = db_session.query_property()