from cryptos import Bitcoin
import os
import functions as f
import sys
import time

b = Bitcoin()

print("This is a BTC wallet finder and generator")
print("Select the desired option:")
print("""
    1. Download wallets with balance and try to generate key pairs for any of this wallets.
    2. Search for brainwallets given a certain file with phrases.
    3. Generate a new wallet.
    4. Exit.
""")

while True:
    userAction = input("Enter the desired number option: ")

    if userAction == "1":
        wallets = f.loadWallets()
        pKeysFound = []
        count = 0

        sleepTime = input("Enter wait time per search (in milliseconds): ")
        sleepTimeMS = int(sleepTime) / 1000

        while True:
            randWallet = f.genWallet()

            if (
                randWallet[1] in wallets
                or randWallet[2] in wallets
                or randWallet[3] in wallets
            ):
                pKeysFound.append(randWallet)
                f.writeFoundKeys(pKeysFound)

            count += 1
            sys.stdout.write(
                f"\r{count:,} bitcoin addresses searched, {len(pKeysFound)} private keys with balance found."
            )
            sys.stdout.flush()

            time.sleep(sleepTimeMS)
            # os.system("clear")
            # print(
            #     f"{count:,} bitcoin adresses searched, {len(pKeysFound)} private keys with balance found."
            # )

    elif userAction == "2":
        os.system("clear")
        wallets = f.loadWallets()
        fileName = input(
            "Enter the name of the file with the phrases (must be in root dir): "
        )
        passwords = set()
        count = 0

        with open(fileName, "r") as file:
            for line in file:
                passwords.add(line.strip())

        for password in passwords:
            randWallet = f.genWallet(password)

            if (
                randWallet[1] in wallets
                or randWallet[2] in wallets
                or randWallet[3] in wallets
            ):
                f.writeFoundKeys(
                    f"Brainwallet: {password} \nPrivate Key: {randWallet[0]} \nSegwit Address: {randWallet[1]} \np2pkh Address: {randWallet[2]} \n p2sh Address: {randWallet[3]} \n\n"
                )
            count += 1
            os.system("clear")
            print(f"{count:,} passwords tried.")
    elif userAction == "3":
        randWallet = f.genWallet()
        print(
            f"Private Key: {randWallet[0]} \nSegwit Address: {randWallet[1]} \np2pkh Address: {randWallet[2]} \n p2sh Address: {randWallet[3]} \n\n"
        )

    elif userAction == "4":
        exit()
