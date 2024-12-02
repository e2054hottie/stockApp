def replace_placeholders(template, *args):
    """
    テンプレート内のプレースホルダーを，引数で与えられた値で置換する．

    Args:
        template (str): プレースホルダーを含むテンプレート文字列
        args (tuple): プレースホルダーに対応する値のリスト

    Returns:
        str: 置換後の文字列
    """
    
    for i, arg in enumerate(args):
        placeholder = f"{{{i}}}"
        template = template.replace(placeholder, str(arg))
    return template