from cryptos import random_key, Bitcoin
import time
import os
import functions as f
b = Bitcoin()

# VARIABLES
RANGE = 10 # Number of wallet to load in millions. Wallets are ordered by balance. The wallets with the most balance are at the top.
SEARCHES = 15 # Number of random bitcoin addresses to generate and search per second.


wallets = f.loadWallets(RANGE)

pKeysFound = []
count = 0

while True:
    for _ in range(SEARCHES):    
        key = random_key()
        segwitAddress = b.privtosegwitaddress(key)
        address = b.privtoaddr(key)
    
        if segwitAddress in wallets or address in wallets:
            pair = {key: [segwitAddress, address]}
            pKeysFound.append(pair)            
            f.writeFoundKeys(pKeysFound)
                    
        count += 1
  
    os.system('clear')
    print(f'{count:,} bitcoin adresses searched')
    
    if pKeysFound:
      print(f'{len(pKeysFound)} wallets found: {pKeysFound} "\n"')
    time.sleep(1)