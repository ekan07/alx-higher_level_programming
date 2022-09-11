#!/usr/bin/python3
"""adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states_rows = session.query(State).filter(State.name.like('%a%'))
        for state in states_rows:
            session.delete(state)
        session.commit()
