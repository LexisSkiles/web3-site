from flask import Flask, render_template, request
from web3 import Web3

app = Flask(__name__)

# Replace 'YOUR_INFURA_PROJECT_ID' with your Infura project ID
INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'

# Initialize a web3 provider using Infura
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_balance', methods=['POST'])
def check_balance():
    wallet_address = request.form['wallet_address']
    try:
        balance = w3.eth.get_balance(wallet_address)
        balance_eth = w3.fromWei(balance, 'ether')
        return f"Balance for {wallet_address}: {balance_eth} ETH"
    except Exception as e:
        return f"Error getting balance for {wallet_address}: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
