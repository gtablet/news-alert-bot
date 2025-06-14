import requests
from bs4 import BeautifulSoup
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, params=params)

def get_latest_news():
    url = 'https://search.naver.com/search.naver?where=news&query=산업은행&sort=1'
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    news_items = soup.select('a.news_tit')

    news = []
    for item in news_items:
        title = item['title']
        link = item['href']
        news.append(f"{title}\n{link}")
    return news

def main():
    news = get_latest_news()
    for item in news[:3]:
        send_telegram_message(f"[산업은행 뉴스]\n{item}")

if __name__ == "__main__":
    main()
