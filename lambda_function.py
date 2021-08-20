import cbpro
import sms
import math
from time import time, ctime

# login credentials
API_KEY = [api-key]
SECRET_KEY = [secret-key]
PASSPHRASE = [passphrase]

# wallet addresses
BTC_ADDRESS = '35c0b264-58b0-4b3d-a57d-b33da8023539'

# how much USD to use?
# minimum $5.00
PURCHASE_AMT = '5'


# main function
def lambda_handler(event, context):
    # configuring login to my (authenticated) client and account
    auth_client = cbpro.AuthenticatedClient(API_KEY, SECRET_KEY, PASSPHRASE)

    # placing the buy order
    try:
        order = auth_client.place_market_order(product_id='BTC-USD', side='buy', funds=PURCHASE_AMT)
    except Exception as e:
        print(e)

    # sending the notification
    current_price = math.floor(float(auth_client.get_product_ticker('BTC-USD')['price']))
    satoshis = int(PURCHASE_AMT) / int(current_price) * 100000000
    t = time()

    message = 'BTCBOT purchased ' + str(math.floor(satoshis)) + ' satoshis at $' + str(
        current_price) + ' per bitcoin.\nTIMESTAMP: ' + str(ctime(t))

    # checking if the purchase was successful
    if 'funds is too small' in order['message']:
        message = 'error! you must purchase at least of $5 of bitcoin.'

    sms.send(message)

    return {
        'order': order
    }