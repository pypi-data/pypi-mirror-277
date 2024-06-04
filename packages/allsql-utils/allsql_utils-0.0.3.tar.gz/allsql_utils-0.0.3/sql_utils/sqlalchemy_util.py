# -*- coding: utf-8 -*-
"""
@Time : 2023/12/8 10:50 
@项目：数据库的基础使用
@File : sqlalchemy_operation.by
@PRODUCT_NAME :PyCharm
"""
"""
SQL-Alchemy
SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。
参考文献：https://www.cnblogs.com/wupeiqi/articles/8259356.html

组成部分：

Engine:框架的引擎。
Connection Pooling:数据库连接池。
Dialect:选择连接数据库的DB API 种类。
Schema/Types:架构和类型。
SQL Exprression Language:SQL表达式语言。
SQLAlchemy 本身无法操作数据库，其必须以pymysql等第三方插件，Dialect用于和数据API进行交流, 根据配置文件的不同调用不同的数据库 API,从而实现对数据库的操作，

pymysql
   mysql+pymysql://<username>:<``password``>@<host>/<dbname>[?<options>]
 
 
cx_Oracle
	oracle+cx_oracle://``user``:pass@host:port/dbname[key``=value&``key``=value.]


"""
# 2.简单使用
# 使用 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine 使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。
# https://blog.csdn.net/m0_61970162/article/details/126312321
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class SQLAlchemyConfig(object):
    def __init__(self, host, username, password, port, db, charset="utf8",
                 max_overflow=0,  # 超过连接池大小外最多创建的连接
                 pool_size=5,  # 连接池中数量的大小
                 pool_timeout=30,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                 pool_recycle=-1,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                 pool_pre_ping=True
                 ):
        # 创建引擎
        if charset:
            engine_link = f'''mysql+pymysql://{username}:{password}@{host}:{port}/{db}'''
        else:
            engine_link = f'''mysql+pymysql://{username}:{password}@{host}:{port}/{db}'''
        self.engine = create_engine(engine_link,
                                    max_overflow=max_overflow,  # 超过连接池大小外最多创建的连接
                                    pool_size=pool_size,  # 连接池中数量的大小
                                    pool_timeout=pool_timeout,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                                    pool_recycle=-pool_recycle,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                                    pool_pre_ping=pool_pre_ping  # True，则将启用连接池的“pre-ping”功能，该功能在每次签出时测试连接的活跃度
                                    )


class pymysqlOperations(SQLAlchemyConfig):
    def __init__(self, host, username, password, port, db, charset="utf8",
                 max_overflow=0,  # 超过连接池大小外最多创建的连接
                 pool_size=5,  # 连接池中数量的大小
                 pool_timeout=30,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                 pool_recycle=-1,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                 pool_pre_ping=True):
        super().__init__(host, username, password, port, db, charset=charset,
                         max_overflow=max_overflow,  # 超过连接池大小外最多创建的连接
                         pool_size=pool_size,  # 连接池中数量的大小
                         pool_timeout=pool_timeout,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                         pool_recycle=pool_recycle,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                         pool_pre_ping=pool_pre_ping)
        self.conn = self.engine.raw_connection()
        self.cursor = self.conn.cursor()

    def _conn(self):
        try:
            self.conn = self.engine.raw_connection()
            self.cursor = self.conn.cursor()
            print(datetime.datetime.now(), "数据库连接成功")
            return True
        except Exception as e:
            print(datetime.datetime.now(), "数据库连接失败:" + str(e))
            return False
        # 通过ping()实现数据库的长连接

    # </editor-fold>
    # <editor-fold desc="新建数据库">
    def create_database(self, db_name):
        """
        :param db_name:数据库名称
        :return:
        """

        sql = f'create database if not exists {db_name};'
        self.cursor.execute(sql)
        return db_name

    # </editor-fold>
    # <editor-fold desc="删除数据库">
    def drop_database(self, db_name):
        """
        :param db_name:数据库名称
        :return:
        """

        sql = f'drop database if exists {db_name};'
        self.cursor.execute(sql)

    # </editor-fold>
    # <editor-fold desc="查看服务器上的所有数据库">
    def show_databases(self):

        sql = 'show databases;'

        return [i[0] for i in self.select(sql)]

    # </editor-fold>
    # <editor-fold desc="查看当前数据库">
    def select_database(self):

        sql = 'select database();'
        return self.select(sql)

    # </editor-fold>
    # <editor-fold desc="创建数据表">
    def create_table(self, sql):

        # 创建表
        # '''CREATE TABLE COMPANY
        # (
        #     ID INT PRIMARY KEY NOT NULL auto_increment,
        #     NAME TEXT NOT NULL,
        #     AGE INT NOT NULL,
        #     ADDRESS CHAR(50),SALARY REAL,
        #     score float(3,1)
        # );'''
        self.cursor.execute(sql)
        # self.conn.commit()

    # </editor-fold>
    # <editor-fold desc="查看当前数据库中所有的表">
    def show_tables(self):

        ''''''
        sql = 'show tables;'
        return [i[0] for i in self.select(sql)]

    # </editor-fold>
    # <editor-fold desc="删除数据库表">
    def drop_table(self, tbl_name):

        '''
        :param tbl_name:表名
        :return:
        '''
        sql = f'drop table if exists {tbl_name};'
        self.cursor.execute(sql)

    # </editor-fold>
    # <editor-fold desc="插入数据">
    def insert(self, sql):

        """
        :param sql:"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )"
        :return:
        """
        """
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
        """
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            self.conn.rollback()
            # self.close()

    # </editor-fold>
    # <editor-fold desc="批量插入数据">
    def insert_executemany(self, sql, val):

        """
        :param sql:"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )"
        :return:
        """
        '''
        data = [['2022-11-07 15:11:23', '077558', '13.4', '22.5', '-1.157', 1],
        ['2022-11-07 15:10:21', '077559', '5.6', '21.4', '-1.844', 3],
        ['2022-11-07 15:10:20', '077560', '10.9', '21.8', '-1.811', 4],
        ['2022-11-07 15:12:13', '077561', '11.5', '22.5', '-1.854', 2]]
        insert_sql = f""" INSERT INTO {waterlevelgauge}(create_time, water_gauge, osmotic_pressure, tem, `value`,info_id)
               VALUES (%s, %s,%s,  %s, %s,  %s);
       """
        '''
        # try:
        #     print("sql", sql)
        #     # 执行sql语句
        #     self.cursor.executemany(sql, val)
        #     # 提交到数据库执行
        #     self.conn.commit()
        # except Exception as e:
        #     print(e)
        #     self.conn.rollback()
        # 执行sql语句
        self.cursor.executemany(sql, val)
        # 提交到数据库执行
        self.conn.commit()

    # </editor-fold>
    # <editor-fold desc="查询数据">
    def select(self, sql):

        """
        :param sql:"SELECT id, name, address, salary  from COMPANY"
        :return:
        """
        # Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
        # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
        # fetchall(): 接收全部的返回结果行.
        # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        # self.conn.commit()
        return list(results)

    def select_dic(self, table, sql=None):
        """
                dat = self.cursor.select_dic("sensor_water_hikvision_video",f"select * from sensor_water_hikvision_video where number='{number}' limit 1;")
        """

        if not sql:
            sql = f"""select * from {table}"""
        list_data = []
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        table_fileds = self.select_table_fileds(table)
        for dat in data:
            text = {}
            # 使用cursor游标的description方法，得到数据库的每一列的信息
            # 将data信息与其拼接为字典，并存放入列表中
            # 其实还有个数据库方法获取列名信息：PRAGMA TABLE INOF([表名])
            for s, x in enumerate(table_fileds):
                text[x] = dat[s]
            # 若是多个引用值，list.append(str(text))
            list_data.append(text)
        # self.conn.commit()
        return list_data

    # </editor-fold>
    # <editor-fold desc="更新数据">
    def update(self, sql, ):

        """
        :param sql:"UPDATE COMPANY set SALARY = 25000.00 where ID=1"
        :return:
        """
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()
            self.close()

    # </editor-fold>
    # <editor-fold desc="删除数据">
    def delete(self, sql):

        """
        :param sql:"DELETE from COMPANY where ID=2;"
        :return:
        """
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()
            self.close()

    # </editor-fold>
    # <editor-fold desc="关闭数据库">
    def close(self):

        self.conn.close()

    # </editor-fold>
    def select_table_fileds(self, table):

        sql = f"""show columns from {table};"""
        """+-------------+----------------------+------+-----+-------------------+-----------------------------+
            | Field       | Type                 | Null | Key | Default           | Extra                       |
            +-------------+----------------------+------+-----+-------------------+-----------------------------+
            | actor_id    | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
            | first_name  | varchar(45)          | NO   |     | NULL              |                             |
            | last_name   | varchar(45)          | NO   | MUL | NULL              |                             |
            | last_update | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
            +-------------+----------------------+------+-----+-------------------+-----------------------------+
            4 rows in set (0.00 sec)
        """
        data = self.select(sql)
        data = [i.get("Field") if isinstance(i, dict) else i[0] for i in data]
        return data

    def other_sql(self, key, tables=None, databases=None):

        dic = {
            # 查询某一张表中所有字段及注释信息
            # 1: f"""-- select COLUMN_NAME,column_comment from INFORMATION_SCHEMA.Columns where table_name ="{tables}";""",
            1: f"""select COLUMN_NAME,column_comment from INFORMATION_SCHEMA.Columns where table_name=`{tables}`; """,
            # 查询某一张表中的所有字段，字段之间以逗号隔开，进行拼接
            2: f"""select  group_concat(COLUMN_NAME) from INFORMATION_SCHEMA.Columns where table_name = {tables};""",
            3: f"""""",
            4: f"""""",
            5: f"""""",
            6: f"""""",
            7: f"""""",
            8: f"""""",
            9: f"""""",
            10: f"""""",
            11: f"""""",
            12: f"""""",
        }
        return dic.get(key)

    def Permission_sql(self):
        """-- 查询权限
        SHOW GRANTS FOR '用户名'@'主机名';
        SHOW GRANTS FOR 'lisi'@'%';
        -- 授予权限
        grant 权限列表 on 数据库名.表名 to '用户名'@'主机名';

        -- 给张三用户授予所有权限，在任意数据库任意表上
        GRANT ALL ON *.* TO 'zhangsan'@'localhost';
        -- 撤销权限：
        revoke 权限列表 on 数据库名.表名 from '用户名'@'主机名';
        REVOKE UPDATE ON db3.`account` FROM 'lisi'@'%';

        管理用户
        添加用户
        语法：CREATE USER '用户名'@'主机名' IDENTIFIED BY '密码';
        删除用户
        语法：DROP USER '用户名'@'主机名';
        """
        dic = {
            1: f"""""",
            2: f"""""",
            3: f"""""",
            4: f"""""",
            5: f"""""",
            6: f"""""",
            7: f"""""",
            8: f"""""",
            9: f"""""",
            10: f"""""",
            11: f"""""",
            12: f"""""",
        }
    # </editor-fold>


class EngineOperations(SQLAlchemyConfig):
    def __init__(self, host, username, password, port, db, charset="utf8",
                 max_overflow=0,  # 超过连接池大小外最多创建的连接
                 pool_size=5,  # 连接池中数量的大小
                 pool_timeout=30,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                 pool_recycle=-1,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                 pool_pre_ping=True):
        super().__init__(host, username, password, port, db, charset=charset,
                         max_overflow=max_overflow,  # 超过连接池大小外最多创建的连接
                         pool_size=pool_size,  # 连接池中数量的大小
                         pool_timeout=pool_timeout,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                         pool_recycle=pool_recycle,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                         pool_pre_ping=pool_pre_ping)
        # 执行sql语句


class OrmSQLAlchemyOperations(SQLAlchemyConfig):
    def __init__(self, host, username, password, port, db, charset="utf8",
                 max_overflow=0,  # 超过连接池大小外最多创建的连接
                 pool_size=5,  # 连接池中数量的大小
                 pool_timeout=30,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                 pool_recycle=-1,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                 pool_pre_ping=True):
        super().__init__(host, username, password, port, db, charset=charset,
                         max_overflow=max_overflow,  # 超过连接池大小外最多创建的连接
                         pool_size=pool_size,  # 连接池中数量的大小
                         pool_timeout=pool_timeout,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
                         pool_recycle=pool_recycle,  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
                         pool_pre_ping=pool_pre_ping)
        self.Base = declarative_base()  # 实例化映射关系的类对象,后期的数据库表类直接继承该类。

    def init_db(self):
        self.Base.metadata.create_all(self.engine)  # 创建所有表

    def drop_db(self):  # 删除表的所有函数。执行
        self.Base.metadata.drop_all(self.engine)
