# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moschitta_query']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'moschitta-query',
    'version': '0.1.0',
    'description': 'Fluent Query Builder Library',
    'long_description': "# Moschitta Query Documentation\n\nThe `moschitta-query` package provides a Fluent Query Builder for the Moschitta Framework, enabling developers to generate SQL queries programmatically using a fluent interface.\n\n## Installation\n\nYou can install `moschitta-query` via pip:\n\n```bash\npip install moschitta-query\n```\n\nOr use it with Poetry:\n\n```bash\npoetry add moschitta-query\n```\n\n## Usage\n\n### Basic Query Construction\n\nTo use `moschitta-query`, you need to initialize an instance of the `Query` class.\n\n```python\nfrom moschitta_query.query import Query\n\n# Create a basic select query\nquery = Query().select('id', 'name').from_('users')\nprint(query.to_sql())\n# Output: SELECT id, name FROM users\n```\n\n### Adding Conditions\n\nYou can add conditions to your query using the `where` method.\n\n```python\n# Add a where clause to the query\nquery = Query().select('*').from_('users').where('age > 21')\nprint(query.to_sql())\n# Output: SELECT * FROM users WHERE age > 21\n```\n\n### Joining Tables\n\nPerform joins using the `join` method.\n\n```python\n# Perform an inner join with another table\nquery = Query().select('users.id', 'users.name', 'orders.total').from_('users') \\\n               .join('orders', 'users.id = orders.user_id')\nprint(query.to_sql())\n# Output: SELECT users.id, users.name, orders.total FROM users JOIN orders ON users.id = orders.user_id\n```\n\n### Ordering Results\n\nSpecify the order of the result set using the `order_by` method.\n\n```python\n# Order the result set by a column\nquery = Query().select('name').from_('users').order_by('name')\nprint(query.to_sql())\n# Output: SELECT name FROM users ORDER BY name\n```\n\n## API Reference\n\n### `moschitta_query.query.Query`\n\n- `select(*columns: str) -> Query`: Specifies the columns to select in the query.\n- `from_(table: str) -> Query`: Specifies the table to select data from.\n- `where(*conditions: str) -> Query`: Adds conditions to filter the result set.\n- `join(table: str, on_clause: str) -> Query`: Performs an inner join with another table.\n- `left_join(table: str, on_clause: str) -> Query`: Performs a left outer join with another table.\n- `right_join(table: str, on_clause: str) -> Query`: Performs a right outer join with another table.\n- `order_by(*columns: str) -> Query`: Specifies the columns to order the result set by.\n- `group_by(*columns: str) -> Query`: Groups the result set by the specified columns.\n- `having(*conditions: str) -> Query`: Adds conditions to filter the grouped result set.\n- `limit(count: int) -> Query`: Limits the number of rows returned by the query.\n- `offset(start: int) -> Query`: Specifies the starting offset for the result set.\n- `to_sql() -> str`: Returns the constructed SQL query as a string.\n\n## Contributing\n\nContributions to `moschitta-query` are welcome! You can contribute by opening issues for bugs or feature requests, submitting pull requests, or helping improve the documentation.\n\n## License\n\nThis project is licensed under the terms of the [MIT License](LICENSE).\n",
    'author': 'Skyler Saville',
    'author_email': 'skylersaville@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
