"""
This module provides the Query class for building SQL queries using a fluent interface.
"""

from typing import Any, Dict, List


class Query:
    """
    The Query class is used to build SQL queries using a fluent interface.
    """

    def __init__(self):
        self._select_columns: List[str] = []
        self._from_table: str = ""
        self._clauses: Dict[str, Any] = {
            "where": [],
            "join": [],
            "order_by": [],
            "group_by": [],
            "having": [],
        }
        self._limit: Dict[str, int] = {
            "count": None,
            "offset": None,
        }

    def select(self, *columns: str) -> "Query":
        """
        Specifies the columns to select in the query.
        """
        self._select_columns.extend(columns)
        return self

    def from_(self, table: str) -> "Query":
        """
        Specifies the table to select data from.
        """
        self._from_table = table
        return self

    def where(self, *conditions: str) -> "Query":
        """
        Adds conditions to filter the result set.
        """
        self._clauses["where"].extend(conditions)
        return self

    def join(self, table: str, on_clause: str) -> "Query":
        """
        Performs an inner join with another table.
        """
        self._clauses["join"].append(f"JOIN {table} ON {on_clause}")
        return self

    def left_join(self, table: str, on_clause: str) -> "Query":
        """
        Performs a left outer join with another table.
        """
        self._clauses["join"].append(f"LEFT JOIN {table} ON {on_clause}")
        return self

    def right_join(self, table: str, on_clause: str) -> "Query":
        """
        Performs a right outer join with another table.
        """
        self._clauses["join"].append(f"RIGHT JOIN {table} ON {on_clause}")
        return self

    def order_by(self, *columns: str) -> "Query":
        """
        Specifies the columns to order the result set by.
        """
        self._clauses["order_by"].extend(columns)
        return self

    def group_by(self, *columns: str) -> "Query":
        """
        Groups the result set by the specified columns.
        """
        self._clauses["group_by"].extend(columns)
        return self

    def having(self, *conditions: str) -> "Query":
        """
        Adds conditions to filter the grouped result set.
        """
        self._clauses["having"].extend(conditions)
        return self

    def limit(self, count: int) -> "Query":
        """
        Limits the number of rows returned by the query.
        """
        self._limit["count"] = count
        return self

    def offset(self, start: int) -> "Query":
        """
        Specifies the starting offset for the result set.
        """
        self._limit["offset"] = start
        return self

    def to_sql(self) -> str:
        """
        Returns the constructed SQL query as a string.
        """
        query = f"SELECT {', '.join(self._select_columns)} FROM {self._from_table}"
        if self._clauses["join"]:
            query += " " + " ".join(self._clauses["join"])
        if self._clauses["where"]:
            query += " WHERE " + " AND ".join(self._clauses["where"])
        if self._clauses["group_by"]:
            query += " GROUP BY " + ", ".join(self._clauses["group_by"])
        if self._clauses["having"]:
            query += " HAVING " + " AND ".join(self._clauses["having"])
        if self._clauses["order_by"]:
            query += " ORDER BY " + ", ".join(self._clauses["order_by"])
        if self._limit["count"] is not None:
            query += f" LIMIT {self._limit['count']}"
        if self._limit["offset"] is not None:
            query += f" OFFSET {self._limit['offset']}"
        return query
