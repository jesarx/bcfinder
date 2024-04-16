import os

def loadWallets(NumberOfLines=10):
    wallets = set()
    linesInMillions = NumberOfLines * 1000000
    
    if not os.path.exists('blockchair_bitcoin_addresses_and_balance_LATEST.tsv'):
        print('Downloading wallet list...')
        os.system('wget http://addresses.loyce.club/blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz')
        print('Uncompressing wallet list...')
        os.system('tar -xzf blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz')
        os.system('rm blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz')
    
    print('Loading wallets...')    
    with open('blockchair_bitcoin_addresses_and_balance_LATEST.tsv', 'r') as file:
        for _ in range(linesInMillions):  
            line = file.readline().strip() 
            if not line:  
                break
            wallet, _ = line.split('\t') 
            wallets.add(wallet)
    os.system('clear')
    return wallets

def writeFoundKeys(pKeysFound):
    with open('foundKeys.txt', 'w') as file:
        for pair in pKeysFound:
            file.write(str(pair) + '\n')
            
    return None
  
