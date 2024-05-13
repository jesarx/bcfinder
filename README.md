# BCFINDER

## This script generates random private keys and looks if the wallet has balance on it

Running:

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

This downloads the [latest list of all funded BTC addresses](http://addresses.loyce.club/), generates random private keys with its respective public addresses and then search for this wallets in the downloaded list.

This script can also search for brainwallets with a given list of passwords
