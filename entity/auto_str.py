def auto_str(cls):
    """概要
    クラスデコレータ
    すべてのメンバに対して，辞書型に変換
    """
    def __str__(self):
        return str({key: str(value) for key, value in self.__dict__.items()})
    
    cls.__str__ = __str__
    return cls