import yfinance as yf
import json
from datetime import datetime, timedelta

def get_financial_data(ticker):
    # 銘柄の情報を取得
    stock = yf.Ticker(ticker)

    # 財務状況
    financials = {str(k): v for k, v in stock.financials.to_dict().items()}
    # financials = {str(k): v for k, v in stock.quarterly_financials.to_dict().items()}

    # financialsLatest = {str(k): v for k, v in stock.quarterly_financials.to_dict().items()}
    balance_sheet = {str(k): v for k,v in stock.balance_sheet.to_dict().items()}
    cashflow = {str(k):v for k,v in stock.cashflow.to_dict().items()}

    # 株価推移（過去5年間、1か月ごと）
    end_date = datetime.today()

    start_date = end_date - timedelta(days=5*365)

    hist = stock.history(start=start_date, end=end_date, interval="1mo")

    stock_price_history = hist['Close'].to_dict()

    # Timestampを文字列に変換
    stock_price_history = {str(k): v for k, v in stock_price_history.items()}

    # 株価指標
    stock_info = stock.info

    # 配当金情報（利回り、配当性向）
    dividends = stock.dividends.to_dict()
    dividends = {str(k): v for k, v in dividends.items()}  # Timestampを文字列に変換
    dividend_yield = stock_info.get('dividendYield', None)
    payout_ratio = stock_info.get('payoutRatio', None)

   

    # 利回りをパーセンテージに変換
    if dividend_yield is not None:
        dividend_yield *= 100
   
    # データをまとめる
    data = {
        "name":stock.info["longName"],
        "financials": financials,
        "balance_sheet": balance_sheet,
        "cashflow": cashflow,
        "stock_price_history": stock_price_history,
        "stock_info": {
            "currentPrice": stock_info.get("currentPrice"),
            "marketCap": stock_info.get("marketCap"),
            "trailingPE": stock_info.get("trailingPE"),
            "forwardPE": stock_info.get("forwardPE"),
            "priceToBook": stock_info.get("priceToBook"),
            "revenueGrowth": stock_info.get("revenueGrowth"),
            "earningsGrowth": stock_info.get("earningsGrowth"),
            "grossMargins": stock_info.get("grossMargins"),
            "operatingMargins": stock_info.get("operatingMargins"),
            "ebitdaMargins": stock_info.get("ebitdaMargins"),
            "returnOnAssets": stock_info.get("returnOnAssets"),
            "returnOnEquity": stock_info.get("returnOnEquity"),
            "currentRatio": stock_info.get("currentRatio"),
            "quickRatio": stock_info.get("quickRatio"),
            "debtToEquity": stock_info.get("debtToEquity")
        },
        "dividends": dividends,
        "dividend_yield": dividend_yield,
        "payout_ratio": payout_ratio
    }

    # JSONファイルに保存
    # with open(filename, 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)
    print(data)
    return data