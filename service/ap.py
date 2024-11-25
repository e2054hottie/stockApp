import pathlib
import textwrap
import google.generativeai as genai

import json

with open('service/apikey.txt', 'r', encoding='utf-8') as file:
    key = file.read()

genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def test(code):
    query = ('あなたは株式投資に関する優秀なAIアシスタントです．'
    '東証に上場している銘柄の株について分析してください．'
    '[meigara]の今後の見通しを教えて下さい．'
    'そのさいに，配当の累進性，持続性を5.0点満点で，'
    '今後の株価の上昇期待度を5.0点満点で評価してください'
    'なお，点数は0.1点刻みでお願いします．'
    'また，返答の形式は[keishiki]に合わせてください'
    'なお，存在しない証券コードの場合，「その銘柄は存在しません」と返答してください．'
    'また，市場がプライム以外の場合，変更の最後に「この銘柄はプライム市場ではないです」と付け加えてください．'
    f'[meigara]{code}.T'
    '[keisiki] 総評(100文字以内)，配当の累進性 点数 理由，配当の持続性 点数 理由，株価の上昇期待度 点数 理由'
    )
    
    responce = model.generate_content(query)
    
    return  responce.text