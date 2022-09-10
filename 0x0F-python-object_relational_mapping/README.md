# 0x0F. Python - Object-relational mapping

## Description
The goal of this project is to learn how to use an Object-relational mapper (ORM).
The module MySQLdb will be used in Python to connect to a MySQL database, and then the module SQLAlchemy will be used.

## Table of contents
Files | Description
----- | -----------
[0-select_states.py](./0-select_states.py) | Python script that lists all states from the database hbtn_0e_0_usa
[1-filter_states.py](./1-filter_states.py) | Python script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
[2-my_filter_states.py](./2-my_filter_states.py) | Python script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
[3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | Python script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument safe from SQL injections
[4-cities_by_state.py](./4-cities_by_state.py) | Python script that lists all cities from the database hbtn_0e_4_usa
[5-filter_cities.py](./5-filter_cities.py) | Python script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
[model_state.py](./model_state.py) | python file that contains the class definition of a State and an instance Base = declarative_base()
[7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Python script that lists all State objects from the database hbtn_0e_6_usa
[8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Python script that prints the first State object from the database hbtn_0e_6_usa
[9-model_state_filter_a.py](./9-model_state_filter_a.py) | Python script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
