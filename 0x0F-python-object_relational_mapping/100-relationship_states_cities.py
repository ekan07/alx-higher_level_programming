#!/usr/bin/python3
"""creates the State “California” with
the City “San Francisco” from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # generate database schema
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    with Session() as session:
        state = State(name="California")
        city = City(name="San Francisco")
        state.cities.append(city)

        session.add_all([state, city])
        session.commit()
