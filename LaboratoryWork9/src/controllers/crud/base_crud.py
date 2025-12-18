import sqlite3

from typing import Any, Type
from functools import partial

from LaboratoryWork9.src.models.base_model import BaseModel
from LaboratoryWork9.src.utils.decorators import check_types


class BaseCRUD:
    """
    Provides us with middle-level crud interface with sqlite api.
    """

    @check_types(Any, str, tuple | list, Any)
    def __init__(self, file: str, attributes: tuple,
                 typeName: type):
        """
        Initializing sqlite3 base objects

        Args:
            file (str): Database file name (without .db extension).
            attributes (Tuple): Tuple of (name, sql_type, python_type) for columns.
            typeName (Type): Model class for data parsing.
        """
        self._table_name = file
        self._connection = sqlite3.connect(f"{file}.db")
        self._cursor = self._connection.cursor()
        self._attributes = (
            ("id", "INTEGER PRIMARY KEY AUTOINCREMENT", int),
            *attributes
        )
        self._keys = tuple(vals[0] for vals in self._attributes)
        if not self._cursor.execute(
                "SELECT name FROM sqlite_master").fetchall():
            self._create_table()
        self._parseFromTuple = partial(
            self._parseFromTuple,
            typeName=typeName
        )

    def _create_table(self):
        """
        Creates the local database table
        """
        self._cursor.execute(
            f"""
            CREATE TABLE {self._table_name} (
                {",".join(map(lambda x: " ".join(x[:-1]),
                              self._attributes))}
            );
            """
        )

    @check_types(Any, Any)
    def create(self, obj: Type[BaseModel]):
        """
        Inserts a new record into the table.

        Args:
            obj (Type[BaseModel]): The object to insert.
        """
        self._cursor.execute(
            f"""
            INSERT INTO {self._table_name} 
                ({",".join(self._keys[1:])}) 
                VALUES ({",".join(["?"] * len(self._keys[1:]))})
            """,
            self._parseToTuple(obj)[1:]
        )
        self._connection.commit()
        obj.id = self._cursor.lastrowid

    @check_types(Any, tuple, Any)
    def _parseFromTuple(self, item: tuple,
                        typeName: type) -> Type[BaseModel]:
        """
        Converts database tuple to model object.

        Args:
            item (tuple): Database row tuple.
            typeName (Type): Model class.

        Returns:
            Type[BaseModel]: Model instance.
        """
        return typeName(*[(self._attributes[i][2])(item[i])
                          for i in range(len(self._attributes))])

    @check_types(Any, Any)
    def _parseToTuple(self, obj: Type[BaseModel]) -> tuple:
        """
        Converts model object to database tuple.

        Args:
            obj (Type[BaseModel]): Model object.

        Returns:
            Tuple: Tuple of object attributes.
        """
        return tuple(obj.__getattribute__(key) for key in self._keys)

    @check_types(Any, str, Any)
    def read(self, attribute: str, value: Any) -> Any:
        """
        Gives back a single record by attribute value.

        Args:
            attribute (str): Column name to filter by.
            value (Any): Value to match.

        Returns:
            Any: Single model instance.

        Raises:
            KeyError: If attribute doesn't exist.
        """
        if attribute not in self._keys:
            raise KeyError(f"CRUD: no such column '{attribute}'")
        self._cursor.execute(
            f"""
            SELECT * FROM {self._table_name} WHERE {attribute} = ?
            """,
            (value,)
        )
        return self._parseFromTuple(self._cursor.fetchall()[0])

    def readAll(self, attribute: str = None,
                values: list = None) -> list:
        """
        Gives back multiple records.

        Args:
            attribute (str): Column name to filter by (optional).
            values (List): List of values to match (optional).

        Returns:
            List: The list of model instances.

        Raises:
            KeyError: If attribute doesn't exist.
        """
        if attribute is None or values is None:
            self._cursor.execute(
                f"SELECT * FROM {self._table_name}"
            )
        else:
            if attribute not in self._keys:
                raise KeyError(f"CRUD: no such column '{attribute}'")
            if len(values) == 0:
                return []
            self._cursor.execute(
                f"""
                SELECT * FROM {self._table_name} WHERE
                    {attribute} IN ({",".join("?" * len(values))})
                """,
                values
            )
        return [self._parseFromTuple(item) for item in
                self._cursor.fetchall()]

    @check_types(Any, str, Any, Any)
    def update(self, attribute: str,
               value: Any, new_value: Type[BaseModel]):
        """
        Updates a single record.

        Args:
            attribute (str): Column name to identify record.
            value (Any): Value to match.
            new_value (Type[BaseModel]): Updated model object.

        Raises:
            KeyError: If attribute doesn't exist.
        """
        if attribute not in self._keys:
            raise KeyError(f"CRUD: no such column '{attribute}'")
        self._cursor.execute(
            f"""
            UPDATE {self._table_name} SET 
                {",".join(key + "=?"
                          for key in self._keys[1:])}
                WHERE {attribute} = ?
            """,
            self._parseToTuple(new_value)[1:] +
            (value,)
        )
        self._connection.commit()

    @check_types(Any, str, list, Any)
    def updateAll(self, attribute: str,
                  values: list, new_value: Type[BaseModel]):
        """
        Updates multiple records.

        Args:
            attribute (str): Column name to identify records.
            values (List): List of values to match.
            new_value (Type[BaseModel]): Updated model object.

        Raises:
            KeyError: If attribute doesn't exist.
        """
        if attribute not in self._keys:
            raise KeyError(f"CRUD: no such column '{attribute}'")
        self._cursor.executemany(
            f"""
            UPDATE {self._table_name} SET 
                {",".join(key + "=?"
                          for key in self._keys[1:])}
                WHERE {attribute} = ?
            """,
            [
                self._parseToTuple(new_value)[1:] +
                (value,)
                for value in values
            ]
        )
        self._connection.commit()

    @check_types(Any, str, Any)
    def delete(self, attribute: str, value: Any):
        """
        Deletes a single record.

        Args:
            attribute (str): Column name to identify record.
            value (Any): Value to match.

        Raises:
            KeyError: If attribute doesn't exist.
        """
        if attribute not in self._keys:
            raise KeyError(f"CRUD: no such column '{attribute}'")
        self._cursor.execute(
            f"""
            DELETE FROM {self._table_name} WHERE {attribute} = ?
            """,
            (value,)
        )
        self._connection.commit()

    def deleteAll(self, attribute: str, values: list):
        """
        Deletes multiple records or all records.

        Args:
            attribute (str): Column name to identify
                records (optional).
            values (List): List of values to
                match (optional).

        Raises:
            KeyError: If attribute doesn't exist.
        """
        if not attribute or not values:
            self._cursor.execute(
                f"DELETE * FROM {self._table_name}"
            )
        else:
            if attribute not in self._keys:
                raise KeyError(f"CRUD: no such column '{attribute}'")
            self._cursor.executemany(
                f"""
                DELETE FROM {self._table_name} WHERE {attribute} = ?
                """,
                [(i,) for i in values]
            )
            self._connection.commit()

    def __del__(self):
        """
        Closes database connection
        """
        self._connection.close()