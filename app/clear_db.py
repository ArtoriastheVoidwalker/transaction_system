import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import contextlib
from sqlalchemy import MetaData
from db.session import engine
from db.base import Base

# meta = MetaData()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
