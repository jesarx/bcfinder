# BCFINDER

## This script generates random private keys and looks if the wallet has balance on it

Running:

```bash
python3 -m pip install -r requirements.txt
python3 btc-heist.py
```

This downloads the [latest list of all funded BTC addresses](http://addresses.loyce.club/), generates random private keys with its respective public addresses and then search for this wallets in the downloaded list.

By default it generates and searches 10 wallets per second and only takes into account the 10 million wallets with the most balance. This options can be modified.
