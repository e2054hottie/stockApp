import inspect
import re 
def mapping(func):
    def wrapper(*args, **kwargs):
        # 関数名を取得し，末尾に拡張子を追加
        file_name = func.__name__ + ".sql"

        # sqlを取得
        with open(file_name, 'r') as file:
            # ファイルの内容を読み取る
            sql = file.read()

        # パラメータ名を取得
        params = inspect.signature(func).parameters
        param_names = list(params.keys())
        
        # argsとkwargsを結合して辞書を作成
        param_dict = {param_names[i]: arg for i, arg in enumerate(args)}
        param_dict.update(kwargs)
        
        # デフォルト値を持つパラメータを追加
        for name, param in params.items():
            if name not in param_dict:
                param_dict[name] = param.default
        
        # sql内部の変数を置き換える
        return (conv(sql ,param_dict))  
    return wrapper

def conv(sql,dict):
    # すべてのパラメタを置換
    for k in dict:
        # パターンマッチングで置き換え
        pattern = re.compile(r'/\*\s*' + k + r'\s*\*/')
        sql = re.sub(pattern, str(dict[k]), sql)
    return sql