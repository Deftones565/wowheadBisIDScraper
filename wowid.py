from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        item_ids = get_item_ids(url)
        return render_template('result.html', item_ids=item_ids)
    return render_template('index.html')

def get_item_ids(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.select('a')
    item_ids = set()

    for link in links:
        href = link.get('href')
        if href:
            match = re.search(r'item=(\d+)', href)
            if match:
                #item_id = match.group(1)
                #item_ids.append(item_id)
                item_ids.add(match.group(1))
    
    return item_ids

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
