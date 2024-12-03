from lark import Lark, Transformer, Tree

sql_grammar = open('queryParser.lark').read()
parser = Lark(sql_grammar, parser='lalr')

# class SQLTransformer(Transformer):
#     def select_stmt(self, items):
#         return f"SELECT statement: {self._format_items(items)}"
#     def update_stmt(self, items):
#         return f"UPDATE statement: {self._format_items(items)}"
#     def insert_stmt(self, items):
#         return f"INSERT statement: {self._format_items(items)}"
#     def delete_stmt(self, items):
#         return f"DELETE statement: {self._format_items(items)}"
#     def column_list(self, items):
#         return f"Columns: {', '.join(items)}"
#     def assignment_list(self, items):
#         return f"Assignments: {', '.join(items)}"
#     def value_list(self, items):
#         return f"Values: {', '.join(items)}"
#     def conditions(self, items):
#         return f"Conditions: {', '.join(items)}"
#     def condition(self, items):
#         return f"Condition: {items[0]} = {items[1]}"
#     def placeholder(self, items):
#         return f"Placeholder: {' '.join(items)}"
#     def conditional_where_clause(self, items):
#         return f"Conditional WHERE clause: IF {items[0]} THEN WHERE {self._format_items(items[1:])} END"
    
#     def _format_items(self, items):
#         return ' '.join(str(item) for item in items)

sql_parser = Lark(sql_grammar, parser='lalr', transformer=Transformer())

# def parse_sql(sql):
#     parsed_tree = sql_parser.parse(sql)
#     return parsed_tree

# XML出力用関数
def tree_to_xml(tree, level=0):
    indent = "  " * level
    if isinstance(tree, Tree):
        children_xml = "".join(tree_to_xml(child, level + 1) for child in tree.children)
        return f"{indent}<{tree.data}>\n{children_xml}{indent}</{tree.data}>\n"
    else:
        return f"{indent}<{tree.type}>{tree}</{tree.type}>\n"

# メインプログラム
def parse_to_xml(input_text):
    parser = Lark(sql_grammar, start="start", parser="lalr")
    tree = parser.parse(input_text)
    xml_output = tree_to_xml(tree)
    return xml_output

# サンプル入力
input_text = """
SELECT * FROM table_name /*%if 1==value*/ WHERE column1 = /* value1.value */ /*%end */
"""
xml_result = parse_to_xml(input_text)

# 結果表示
print(xml_result)