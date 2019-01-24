from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import constants as const

logger = const.logger


def init_sessionmaker():
    try:
        engine = create_engine(const.DATABASE_URL,
                               connect_args={'sslmode': 'require'},
                               pool_size=50)
        base = const.BASE
        base.metadata.create_all(engine)
        return sessionmaker(bind=engine)
    except:
        logger.error("Cannot connect to db")


session_factory = init_sessionmaker()
Session = scoped_session(session_factory)
