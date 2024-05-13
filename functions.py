from cryptos import sha256, random_key, Bitcoin
import os

b = Bitcoin()


def loadWallets():
    limit = int(input("Enter the number of wallets to load in millions: "))

    wallets = set()
    linesInMillions = limit * 1000000

    if not os.path.exists("blockchair_bitcoin_addresses_and_balance_LATEST.tsv"):
        print("Downloading wallet list...")
        os.system(
            "wget http://addresses.loyce.club/blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz"
        )
        print("Uncompressing wallet list...")
        os.system("gunzip blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz")

    print("Loading wallets...")
    with open("blockchair_bitcoin_addresses_and_balance_LATEST.tsv", "r") as file:
        for _ in range(linesInMillions):
            line = file.readline().strip()
            if not line:
                break
            wallet, _ = line.split("\t")
            wallets.add(wallet)
    os.system("clear")
    return wallets


def writeFoundKeys(pKeysFound):
    existingContent = []
    with open("foundKeys.txt", "r") as file:
        existingContent = file.readlines()

    with open("foundKeys.txt", "w") as file:
        file.writelines(existingContent)
        for pair in pKeysFound:
            file.write(str(pair) + "\n")

    return None


def genWallet(phrase=None):
    if phrase:
        pkey = sha256(phrase)
    else:
        pkey = random_key()

    segwit = b.privtosegwitaddress(pkey)
    p2pkh = b.privtop2pkh(pkey)
    p2sh = b.privtop2wpkh_p2sh(pkey)

    return [pkey, segwit, p2pkh, p2sh]
