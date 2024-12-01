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

def get_sql_from_file(func,class_name):
    # 関数名を取得し，末尾に拡張子を追加
    file_name = Config.getConfig()["sqlFolder"] + "/" + class_name + "/" + func.__name__ + ".sql"

    # sqlを取得
    with open(file_name, 'r') as file:
        # ファイルの内容を読み取る
        sql = file.read()
    return sql

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
        print(param_names,args)
    
    # 仮引数名と実引数の対応
    param_dict = {param_names[i]: arg for i, arg in enumerate(args)}
    print("dict=",param_dict)

    # デフォルト値を持つパラメータを追加
    for name in param_dict:
        print("param=",param_dict[name])
        sql = replace_placeholders(sql,name,param_dict[name])
    
    # sql内部の変数を置き換える
    return sql 

def select(class_name,only_one=False):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            # sql文を作成
            sql = get_sql(func,get_class(args),args,kwargs)

            print("executedSQL=[\"",sql,"\"]")
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

def get_text_up_to_dot(text):
    # ドットまでの部分を抽出する正規表現パターン（ドットを含めない）
    pattern = re.compile(r'^[^.]*')
    match = pattern.search(text)
    if match:
        return match.group(0)
    return None

# インスタンスをとsqlの文字列を受取，チェインをたどり値を取得
def get_nested_attribute(instance, attr_chain):
    # 属性のチェインを分割．最初の要素はインスタンなので削除
    attrs = attr_chain.split('.')[1:] 
    value = instance
    for attr in attrs:
        value = getattr(value, attr)
    return value

def replace_placeholders(sql_query, param_name,instance):
    # プレースホルダーのパターンを定義
    pattern = re.compile(r'(/\*\s*[\w\.]+\s*\*/)')
    # プレースホルダーを検索して置き換える
    matches = pattern.findall(sql_query)
    for match in matches:
        # プレースホルダーから変数名を抽出
        var_name = re.sub(r'/\*\s*|\s*\*/', '', match)

        if param_name != get_text_up_to_dot(var_name):
            continue
        
        if '.' in var_name:
            value = get_nested_attribute(instance, var_name)
            value = typeMapping(value)
        else:
            value = (typeMapping(instance))
        # プレースホルダーを属性値で置き換える
        sql_query = sql_query.replace(match, str(value))
    return sql_query