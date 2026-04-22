from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ملاحظة: سنحتاج لاحقاً لإضافة كود الربط المباشر بـ Exness هنا
@app.route('/')
def home():
    return "Trading Bridge is Live and Ready!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received signal:", data)
    
    # استخراج البيانات من Make
    action = data.get('actionType')
    volume = data.get('volume')
    symbol = data.get('symbol', 'XAUUSD')
    
    return jsonify({"status": "received", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
