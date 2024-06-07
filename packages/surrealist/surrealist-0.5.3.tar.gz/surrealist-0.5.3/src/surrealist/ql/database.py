import logging
from typing import Optional, Tuple, List, Dict, Union, Any, Callable

from surrealist.ql.statements import Select, Remove, Live
from surrealist.ql.statements.define import (DefineEvent, DefineUser, DefineParam, DefineAnalyzer, DefineScope,
                                             DefineIndex, DefineToken, DefineTable, DefineField)
from surrealist.ql.statements.rebuild_index import RebuildIndex
from surrealist.ql.statements.relate import Relate
from surrealist.ql.statements.returns import Return
from surrealist.ql.statements.statement import Statement
from surrealist.ql.statements.transaction import Transaction
from surrealist.ql.table import Table
from surrealist.result import SurrealResult
from surrealist.surreal import Surreal
from surrealist.utils import DEFAULT_TIMEOUT

logger = logging.getLogger("surrealist.databaseQL")


class Database:
    """
    Represents connected database(in some namespace) to operate on.
    It has features of the database level, including switch to table level. You can use DEFINE/REMOVE, query or
    transactions here, but for simple CRUD you need to switch to table level

    Examples: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py
    """

    def __init__(self, url: str, namespace: str, database: str, credentials: Optional[Tuple[str, str]],
                 use_http: bool = False, timeout: int = DEFAULT_TIMEOUT):
        self._namespace = namespace
        self._database = database
        self._connection = Surreal(url, namespace, database, credentials, use_http, timeout).connect()
        self._connected = True
        logger.info("DatabaseQL is up")

    def __enter__(self):
        return self

    def __exit__(self, *exc_details):
        self.close()

    def is_connected(self) -> bool:
        """
        Return if a database is connected
        :return: True if connection is active, False otherwise
        """
        return self._connected

    @property
    def namespace(self) -> str:
        """
        Return name if the namespace
        :return: namespace
        """
        return self._namespace

    @property
    def name(self) -> str:
        """
        Return name of the database
        :return: database name
        """
        return self._database

    def close(self):
        """
        Closes the connection. You cannot and should not use a database object after that
        """
        logger.info("DatabaseQL is closed")
        self._connection.close()
        self._connected = False

    def tables(self) -> List[str]:
        """
        Return list of the table names at a current database
        :return: string list with the names
        """
        logger.info("Get tables for db %s", self._database)
        return self._connection.db_tables().result

    def info(self) -> Dict:
        """
        Return full info about a database, actually call for "INFO FOR DB;" via query
        :return: a result of the response
        """
        logger.info("Get info for db %s", self._database)
        return self._connection.db_info().result

    def raw_query(self, query: str) -> SurrealResult:
        """
        Execute a raw QL query on a database, you should use it in cases when your query is large or complicated, or it
        is just more appropriate for you.

        :param query: text of the query, it will be sent to SurrealDB as is
        :return: a result of the response
        """
        logger.info("Query for db %s", self._database)
        return self._connection.query(query)

    def returns(self, query: str) -> Return:
        """
        Return result of the query

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/return

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param query: string query to execute
        :return: Return object
        """
        return Return(self._connection, query)

    def __getattr__(self, item) -> Table:
        """
        We actually need this to use dot as the switch to table level as "db.person" instead of "db.table("person")"
        :param item: name of the table to work with
        :return: a table object
        """
        return Table(item, self._connection)

    def table(self, name) -> Table:
        """
        Switch to the Table level(an object) after that you can and should use table operations (CRUD)

        :param name: name of the table to work with
        :return: a table object
        """
        return Table(name, self._connection)

    def transaction(self, statements: List[Statement]) -> Transaction:
        """
        Create a transaction object to generate a query or run

        Refer to: https://docs.surrealdb.com/docs/surrealql/transactions

        :param statements: list of appropriate statements (select, create, delete. etc.)
        :return: Transaction object
        """
        return Transaction(self._connection, statements)

    def select_from(self, select: Select, *args, alias: Optional[Tuple[str, Union[str, Statement]]] = None,
                    value: Optional[str] = None) -> Select:
        """
        Allow selecting from sub-query (select)

        :param select: Select object
        :param args: which fields to select, if no fields or "*" - selects all
        :param alias: pairs of names and values
        :param value: on exists add VALUE statement
        :return: Select object
        """
        return Select(self._connection, select, *args, alias=alias, value=value)

    def define_event(self, name: str, table_name: str, then: Union[str, Statement]) -> DefineEvent:
        """
        Allow defining event on table

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/event

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name for the event
        :param table_name: name of the table
        :param then: action to perform
        :return: DefineEvent object
        """
        return DefineEvent(self._connection, name, table_name, then)

    def remove_event(self, name: str, table_name: str) -> Remove:
        """
        Remove an event linked to table

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/remove

        :param name: name of the event
        :param table_name: name of the table
        :return: Remove object
        """
        return Remove(self._connection, table_name=table_name, type_="EVENT", name=name)

    def define_user(self, user_name: str, password: str) -> DefineUser:
        """
        Allow defining user for a current database

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/user

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param user_name: name for the new user
        :param password: password for user
        :return: DefineUser object
        """
        return DefineUser(self._connection, user_name=user_name, password=password)

    def remove_user(self, user_name: str) -> Remove:
        """
        Remove user of the database

        :param user_name: name of the user
        :return: Remove object
        """
        return Remove(self._connection, "", type_="USER", name=user_name)

    def define_param(self, name: str, value: Any) -> DefineParam:
        """
        Represents DEFINE PARAM statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/param

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name of the parameter
        :param value: value for the parameter
        :return: DefineParam object
        """
        return DefineParam(self._connection, name, value)

    def remove_param(self, name: str) -> Remove:
        """
        Remove parameter of the database

        :param name: name of the parameter
        :return: Remove object
        """
        return Remove(self._connection, "", type_="PARAM", name=name)

    def define_analyzer(self, name: str) -> DefineAnalyzer:
        """
        Represents DEFINE ANALYZER statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/analyzer

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name for the analyzer
        :return: DefineAnalyzer object
        """
        return DefineAnalyzer(self._connection, name)

    def remove_analyzer(self, name: str) -> Remove:
        """
        Remove the analyzer

        :param name: name of the analzer
        :return: Remove object
        """
        return Remove(self._connection, '', type_="ANALYZER", name=name)

    def define_scope(self, name: str, duration: str, signup: Union[str, Statement],
                     signin: Union[str, Statement]) -> DefineScope:
        """
        Represents DEFINE SCOPE statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/scope

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name for the new scope
        :param duration: session duration, like 24h
        :param signup: Create statement with string or Statement representation
        :param signin: Select statement with string or Statement representation
        :return: DefineScope object
        """
        return DefineScope(self._connection, name, duration, signup, signin)

    def remove_scope(self, name: str) -> Remove:
        """
        Remove the scope

        :param name: name of the scope
        :return: Remove object
        """
        return Remove(self._connection, "", type_="SCOPE", name=name)

    def define_index(self, name: str, table_name: str) -> DefineIndex:
        """
        Represents DEFINE INDEX statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/indexes

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name for the index
        :param table_name: name of table to work with
        :return: DefineINdex object
        """
        return DefineIndex(self._connection, name, table_name)

    def rebuild_index(self, index_name: str, table_name: str, if_exists: bool = False) -> RebuildIndex:
        """
        Represents REBUILD INDEX object, used to rebuild resources.

        Refer to: https://surrealdb.com/docs/surrealdb/surrealql/statements/rebuild

        :param index_name: name of the index
        :param table_name: name of the table
        :param if_exists: use IF EXISTS statement if True
        :return: RebuildIndex object
        """
        return RebuildIndex(self._connection, index_name=index_name, table_name=table_name, if_exists=if_exists)

    def remove_index(self, name: str, table_name: str) -> Remove:
        """
        Remove index by name on the table

        :param name: name og the index
        :param table_name: name of the table
        :return: Remove object
        """
        return Remove(self._connection, name=name, table_name=table_name, type_="INDEX")

    def define_token(self, name: str, token_type: str, value: str) -> DefineToken:
        """
        Represents DEFINE TOKEN statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/token

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name for the token
        :param token_type: type of the token, for example, RS256
        :param value: value of the token
        :return: DefineIndex object
        """
        return DefineToken(self._connection, name, token_type, value)

    def remove_token(self, name: str) -> Remove:
        """
        Remove token by name for the database

        :param name: name of the token
        :return: Remove object
        """
        return Remove(self._connection, "", type_="TOKEN", name=name)

    def relate(self, value: str) -> Relate:
        """
        Represents RELATE statement, it should be able to use any statements from documentation

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/relate

        Examples: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/ql_relate_examples.py

        :param value: relate representation, see examples
        :return: Relate object
        """
        return Relate(self._connection, value=value)

    def live_query(self, table_name: str, callback: Callable[[Dict], None], select: Optional[str] = None,
                   use_diff: bool = False) -> Live:
        """
        Represents LIVE statement for a live query

        Example:
        db.live_query("person", func).alias("first_name", "NAME").where("age > 22").run()

        Refer to: https://surrealdb.com/docs/surrealdb/surrealql/statements/live

        Refer to: https://github.com/kotolex/surrealist?tab=readme-ov-file#live-query

        Examples: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/ql_live_examples.py

        :param table_name: name od the table to live select
        :param callback: function to call on live query event, signature is `def callback(arg:Dict) -> None`
        :param select: raw query to insert between LIVE SELECT and FROM {table}, so the result will be
        LIVE SELECT {select} FROM {table_name}.
        If it is provided, other parameters (diff, alias, value) will be ignored
        :param use_diff: return result in DIFF format
        :return: Live object
        """
        return Live(self._connection, table_name, callback, select, use_diff)

    def kill_query(self, live_id: str) -> SurrealResult:
        """
        Represents a KILL statement, for killing a live query by id

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/kill

        :param live_id: id of the query
        :return: result
        """
        return self._connection.kill(live_id)

    def define_table(self, name: str) -> DefineTable:
        """
        Represents DEFINE TABLE statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/table

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param name: name of the new table
        :return: DefineTable object
        """
        return DefineTable(self._connection, name)

    def define_field(self, field_name: str, table_name: str) -> DefineField:
        """
        Represents DEFINE FIELD statement

        Refer to: https://docs.surrealdb.com/docs/surrealql/statements/define/field

        Example: https://github.com/kotolex/surrealist/blob/master/examples/surreal_ql/database.py

        :param field_name: name of the field
        :param table_name: name of the table
        :return: DefineField object
        """
        return DefineField(self._connection, field_name, table_name)

    def remove_field(self, field_name: str, table_name: str) -> Remove:
        """
        Remove field by name for the table

        :param field_name: name of the field
        :param table_name: name of the table
        :return: Remove object
        """
        return Remove(self._connection, table_name, type_="FIELD", name=field_name)

    def remove_table(self, table_name: str) -> Remove:
        """
        Remove table by name for the database

        :param table_name: name of the table to remove
        :return: Remove object
        """
        return Remove(self._connection, table_name, type_="TABLE", name="")

    def __repr__(self):
        return f"Database(namespace={self._namespace}, name={self._database}, connected={self.is_connected()})"
