# dca_btc
Programatically purchase crypto via Coinbase API

For a bit I've wanted to create something that would automatically buy stocks/crypto and not have to think about it. A few months ago I got something like this working, but it was only able to run locally on my laptop, which became really burdensom. After getting my AWS cloud practioner cert I felt a lot more comfortable getting started with some aws services, and Lambda seemed like a good fit. I opted for my program to only execute once a week, which means it was able to stay in the free-tier and cost no money to host in the cloud.

All the code I uploaded does is the purchase of certain amounts of crypto via a Python wrapper of the coinbase API. Every time it makes a purchase it alerts the respective phone number/email of the number of satoshis it bought, at what price, and the timestamp. I uploaded it to Lambda and set a trigger for it to execute every 10080 minutes (1 week). In theory, it can be configured to purchase other crypto assets, but the alert message would be incorrect because I hardcoded it in terms of BTC.
