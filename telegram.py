import requests

token = '6549384225:AAEBaKjBcOcY8jL_g6A81L9wIprhQuSZJNY'
chat_id = -4066635565
msg = "Resultados dos experimentos: 97%"

try:
    data = {"chat_id": chat_id, "text": msg}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data)
except Exception as e:
    print("Erro no sendMessage:", e)
