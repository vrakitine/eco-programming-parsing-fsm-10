import MySQLdb

class SQLighter:
    def __init__(self):
        self.conn  = MySQLdb.connect("evaclickparsingfsm.mysql.pythonanywhere-services.com","evaclickparsingf","BDclick!2408","evaclickparsingf$default",charset = "utf8", use_unicode = True)
        self.c = self.conn.cursor()

    def createStateLogTable(self, table_name):
        try:
            self.c.execute("DROP TABLE IF EXISTS %s"% (table_name))
            self.c.execute("CREATE TABLE IF NOT EXISTS `%s` (`id` int(11) NOT NULL AUTO_INCREMENT,`SL_PREVIOUS_STATE_CODE` varchar(255) NOT NULL,`SL_EVENT_CODE` varchar(255) NOT NULL, `SL_CURRENT_STATE_CODE` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 "% (table_name))
            #self.c.execute("INSERT INTO `%s` (`SL_PREVIOUS_STATE_CODE`, `SL_EVENT_CODE`, `SL_CURRENT_STATE_CODE`) VALUES ('s_00', 'v_00', 's_00')"% (table_name))
            self.conn.commit()
        finally:
            self.c.close()
            self.conn.close()

    def sel_from(self,m):
        try:
            return self.c.execute("SELECT * FROM testtable WHERE id =(%s)"% (m))
        finally:
                     self.c.close()
                     self.conn.close()

    def insert(self,query):
        try:
            self.c.execute(query)
            self.conn.commit()
        finally:
                 self.c.close()
                 self.conn.close()
    def update(self,q,m,z):
        try:
            data = (m,z)
            self.c.execute(q,data)
            self.conn.commit()
            rows =self.c.fetchall()
            return rows
        finally:
            self.c.close()
            self.conn.close()
    def returnany(self,q,m):
        try:
            data = (m,)
            self.c.execute(q,data)
            self.conn.commit()
            rows =self.c.fetchall()
            return rows
        finally:
            self.c.close()
            self.conn.close()
    def update2var(self,q,m,z,x):
        try:
            data = (m,z,x)
            self.c.execute(q,data)
            self.conn.commit()
            rows =self.c.fetchall()
            return rows
        finally:
            self.c.close()
            self.conn.close()
