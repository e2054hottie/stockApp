import inspect
import re
import json

from databaseMappingFlamework.databaseConnection import DatabaseConnection 
from databaseMappingFlamework.classFactory import ClassFactory
from databaseMappingFlamework.config import Config
from databaseMappingFlamework.exception.exceptions import MultipleResultsError

def get_class(args):
    # パラメタを取得
    temp_list = list(args)
    inst = temp_list[0]
    return inst.__class__.__name__
    

def typeMapping(data):
    if isinstance(data, str):
        return f'"{data}"'
    return data

def get_sql(func,class_name,args, kwargs):
    # 関数名を取得し，末尾に拡張子を追加
    file_name = Config.getConfig()["sqlFolder"] + "/" + class_name + "/" + func.__name__ + ".sql"

    # sqlを取得
    with open(file_name, 'r') as file:
        # ファイルの内容を読み取る
        sql = file.read()

    # パラメータ名を取得
    params = inspect.signature(func).parameters
    
    param_names = list(params.keys())

    if "self" in param_names:
        param_names.remove("self")
        temp_list = list(args)
        del temp_list[0]
        args = tuple(temp_list)

    for i, arg in enumerate(args):
        print(i,arg)

    
    # argsの辞書を作成
    param_dict = {param_names[i]: typeMapping(arg) for i, arg in enumerate(args)}
    param_dict.update(kwargs)

    # デフォルト値を持つパラメータを追加
    for name, param in params.items():
        if name not in param_dict:
            param_dict[name] = param.default
    
    # sql内部の変数を置き換える
    return (conv(sql ,param_dict)) 

def select(class_name,only_one=False):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            # sql文を作成
            sql = get_sql(func,get_class(args),args,kwargs)
            
            conn = DatabaseConnection()
            result = conn.exec(sql)
            result = ClassFactory.generate_list(class_name,result)
            
            # 結果が一つであることを期待している場合
            if only_one :
                if len(result) > 1:
                    # 2つ以上の場合エラー
                    raise MultipleResultsError(f'{func.__name__}の実行結果は1つ以下である必要がありますが，{len(result)}つ返ってきました．')
                elif len(result)==1:
                    result = result[0]
                else :
                    result = None

            return result
        return wrapper
    return outwrapper

def conv(sql,dict):
    # すべてのパラメタを置換
    for k in dict:
        # パターンマッチングで置き換え
        pattern = re.compile(r'/\*\s*' + k + r'\s*\*/')
        sql = re.sub(pattern, str(dict[k]), sql)
    return sql

