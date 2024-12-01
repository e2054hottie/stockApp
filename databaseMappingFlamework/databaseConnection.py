import pymysql
import databaseMappingFlamework.classFactory as cf 
from databaseMappingFlamework.config import Config

class DatabaseConnection:
    def __init__(self):
        # データベース接続設定を行う
        self.data = Config.getConfig()
    
    def open(self):
        # データベース接続
        self.conn = pymysql.connect(
            host=self.data["dbsetting"]["host"],
            port=self.data["dbsetting"]["port"],
            user=self.data["dbsetting"]["user"],
            password=self.data["dbsetting"]["password"],
            database=self.data["dbsetting"]["database"],
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def exec(self,sql):
        self.open()
        # sqlを実行
        print("executedSQL=",sql)
        cursor = self.conn.cursor()

        try:
            cursor.execute(sql)
        except Exception as e:
            self.conn.rollback()
            print(f'{e}')
            return 
        self.conn.commit()

        # 結果の取得
        result = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return result