import importlib
from databaseMappingFlamework.config import Config

class ClassFactory:
    """概要
    クラス名とディクショナリを受取，動的にインスタンスを生成する機能を提供する
    """
    def generate(class_name):
        def inner(data):
            configJson = Config.getConfig()
            module_name = configJson["entityFolder"].replace("./","")+"."+class_name
            # module = globals().get(module_name)
            module = importlib.import_module(module_name)
            if module is None:
                raise ValueError(f"モジュール {module_name} が見つかりません")

            cls = getattr(module, class_name, None)

            if cls is None:
                raise ValueError(f"クラス {class_name} が見つかりません")

            # クラスのインスタンスを生成
            instance = cls()

            # ディクショナリのキーと値をインスタンスの属性に設定
            for key, value in data.items():
                key = key.replace(".","_")
                setattr(instance, key, value)

            return instance
        return inner
    
    # ディクショナリ型のリストで渡された場合
    def generate_list(class_name,datas):
         return list(map(ClassFactory.generate(class_name),datas))