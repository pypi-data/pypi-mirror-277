import unittest

import duckdb
import git
import sqlglot
from sqlglot import select, condition, and_, or_


class TestSQL(unittest.TestCase):

    def test_base(self):
        a = sqlglot.transpile('''

select date_format(RKSJ, '%Y-%m-%d') as dat,SRC, count(*) as coun
from a_rq_real
group by date_format(RKSJ, '%Y-%m-%d'),SRC;
;
''',
                              read="mysql", write="duckdb")[0]
        print(a)

    def test_base_1(self):
        a = sqlglot.transpile('''from a;''',
                              read="duckdb", write="mysql")[0]
        print(a)

    def test_build_sql(self):
        where = condition("x=1").and_("y=1")
        sql = select("*").from_("y").where(where).sql()
        print(sql)

    def test_build_sql_1(self):
        where = or_("b=1", and_("y=1", "z=1"))
        print(where)
        sql = select("*").from_("y").where(where).sql(dialect="duckdb")
        print(sql)


if __name__ == '__main__':
    unittest.main()
