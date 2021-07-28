# LunesPy

## Interface for consuming the REST APIs of *Lunes Node*
---

## Getting Started

You can install LunesPy using:

    pip install LunesPy

## Documentation

The library utilizes classes to represent various Lunes data structures:

- lunespy.Address
- lunespy.Asset
- lunespy.AssetPair
- lunespy.Order

#### Code Example
```python
import lunespy as lp

myAddress = lp.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
otherAddress = lp.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM')
myAddress.sendLunes(otherAddress, 10000000)
myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
while not myToken.status():
	pass
myAddress.sendAsset(otherAddress, myToken, 50)

```

### Address Class
__lunespy.Address(address, publicKey, privateKey, seed)__ _Creates a new Address object_

#### attributes:
- _address_
- _publicKey_
- _privateKey_
- _seed_

#### methods:

`balance(assetId='', confirmations=0)` returns balance of Lunes or other assets

`assets()` returns a list of assets owned by the address

`issueAsset(name, description, quantity, decimals=0, reissuable=False, txFee=DEFAULT_ASSET_FEE, timestamp=0)` issue a new asset

`reissueAsset(Asset, quantity, reissuable=False, txFee=DEFAULT_ASSET_FEE, timestamp=0)` reissue an asset

`burnAsset(Asset, quantity, txFee=DEFAULT_ASSET_FEE, timestamp=0)` burn the specified quantity of an asset

`sendLunes(recipient, amount, attachment='', txFee=DEFAULT_TX_FEE, timestamp=0)` send specified amount of Lunes to recipient

`massTransferLunes(transfers, attachment='', timestamp=0)` sending Lunes tokens via a mass transfer

`sendAsset(recipient, asset, amount, attachment='', txFee=DEFAULT_TX_FEE, timestamp=0)` send specified amount of an asset to recipient

`massTransferLunes(self, transfers, attachment='', timestamp=0)` sending an asset via mass transfer

`lease(recipient, amount, txFee=DEFAULT_LEASE_FEE, timestamp=0)` post a lease transaction

`leaseCancel(leaseId, txFee=DEFAULT_LEASE_FEE, timestamp=0)` cancel a lease

`createAlias(alias, txFee=DEFAULT_ALIAS_FEE, timestamp=0)` create alias


### Asset Class
__lunespy.Asset(assetId)__ _Creates a new Asset object_

#### attributes:
- _status_
- _assetId_
- _issuer_
- _name_
- _description_
- _quantity_
- _decimals_ = 0
- _reissuable = False_

#### methods:
`status()` returns 'Issued' if the asset exists


## Other functions
`lunespy.setNode(node, chain, chain_id)`  set node URL ('http://ip-address:port') and chain (either 'mainnet' or 'testnet', or any other chain, if you also define the chain id)

`lunespy.setChain(chain, chain_id)`  set chain (either 'mainnet' or 'testnet', or any other chain if you also supply the chain id)

`lunespy.setOffline()`  switch to offline mode; sign tx locally without broadcasting to network

`lunespy.setOnline()`  switch to online mode; sign tx locally a broadcast to network

`lunespy.validateAddress(address)`  checks if the provided address is a valid Lunes address

`lunespy.setMatcher(node)`  set matcher URL ('http://ip-address:port')

`lunespy.setDatafeed(node)`  set datafeed URL ('http://ip-address:port')

`lunespy.height()` get blockchain height

`lunespy.lastblock()` get last block

`lunespy.block(n)` get block at specified height

`lunespy.tx(id)` get transaction details


### Default Fees
The fees for lunes/asset transfers, asset issue/reissue/burn and matcher transactions are set by default as follows:
* DEFAULT_TX_FEE = 100000
* DEFAULT_ASSET_FEE = 100000000
* DEFAULT_MATCHER_FEE = 1000000
* DEFAULT_LEASE_FEE = 100000
* DEFAULT_ALIAS_FEE = 100000

## More Examples

#### Playing with addresses:

```python
import lunespy as lp

# generate a new address
myAddress = lp.Address()  

# set an address with an address
myAddress = lp.Address('3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh')

# get an existing address from seed
myAddress = lp.Address(seed='seven wrist bargain hope pattern banner plastic maple student chaos grit next space visa answer')

# get an existing address from privateKey
myAddress = lp.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')

# get an existing address from a publicKey
address = lp.Address(publicKey=“EYNuSmW4Adtcc6AMCZyxkiHMPmF2BZ2XxvjpBip3UFZL”)

# get an address from a seed with a different nonce (This is especially useful for accessing addresses generated by nodes)
myAddress = lp.Address(seed='seven wrist bargain hope pattern banner plastic maple student chaos grit next space visa answer', nonce=1)
```

#### Balances:
```python
import lunespy as lp

myAddress = lp.Address('3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh')

# get Lunes balance
print("Your balance is %18d" % myAddress.balance())

# get Lunes balance after 20 confirmations
print("Your balance is %18d" % myAddress.balance(confirmations = 20))

# get an asset balance
print("Your asset balance is %18d" % myAddress.balance('DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J'))
```

#### Lunes and asset transfers:
```python
import lunespy as lp

myAddress = lp.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')

# send Lunes to another address
myAddress.sendLunes(recipient = lp.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM'),
                    amount = 100000000)

# send asset to another address
myToken = lp.Asset('4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV')
myAddress.sendAsset(recipient = lp.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM'),
                    asset = myToken,
                    amount = 1000)
```

#### Issuing an asset:
```python
import lunespy as lp

myToken = myAddress.issueToken( name = "MyToken",
                                description = "This is my first token",
                                quantity = 1000000,
                                decimals = 2 )
```

#### Create an alias:
```python
import lunespy as lp

lp.setNode(node = 'http://127.0.0.1:5555', chain = 'testnet')

myAddress = lp.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
myAddress.createAlias("MYALIAS1")
```

#### Mass payment:
```python
import lunespy as lp

recipients =   ['3PBbp6bg2YEnHfdJtYM7jzzXYQeb7sx5oFg',
                '3P4A27aCd3skNja46pcgrLYEnK36TkSzgUp',
                '3P81U3ujotNUwZMWALdcJQLzBVbrAuUQMfs',
                '3PGcKEMwQcEbmeL8Jhe9nZQRBNCNdcHCoZP',
                '3PKjtzZ4FhKrJUikbQ1hRk5xbwVKDyTyvkn']

myAddress = lp.Address(privateKey = "CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S")

for address in recipients:
	myAddress.sendLunes(lp.Address(address), 1000000)
```

#### Mass transfer of Lunes (feature 11)
```python
import lunespy as lp

transfers = [
	{ 'recipient': '3N1xca2DY8AEwqRDAJpzUgY99eq8J9h4rB3', 'amount': 1 },
	{ 'recipient': '3N3YWbQ27NnK7tek6ASFh38Bj93guLxxSi1', 'amount': 2 },
	{ 'recipient': '3MwiB5UkWxt4X1qJ8DQpP2LpM3m48V1z5rC', 'amount': 3 }
]

address = lp.Address(privateKey = "CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S")
address.massTransferLunes(transfers)
```

#### Mass transfer of Assets (feature 11)
```python
import lunespy as lp

transfers = [
	{ 'recipient': '3N1xca2DY8AEwqRDAJpzUgY99eq8J9h4rB3', 'amount': 1 },
	{ 'recipient': '3N3YWbQ27NnK7tek6ASFh38Bj93guLxxSi1', 'amount': 2 },
	{ 'recipient': '3MwiB5UkWxt4X1qJ8DQpP2LpM3m48V1z5rC', 'amount': 3 }
]

address = lp.Address(privateKey = "CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S")
address.massTransferAssets(transfers, lp.Asset('9DtBNdyBCyViLZHptyF1HbQk73F6s7nQ5dXhNHubtBhd'))
```

#### Token airdrop:
```python
import lunespy as lp

myAddress = lp.Address(privateKey = '`')
myToken = lp.Asset('4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV')
amount = 1000

with open('recipients.txt') as f:
	lines = f.readlines()
for address in lines:
	myAddress.sendAsset(lp.Address(address.strip()), myToken, amount)
```

#### LPOS
```python
import lunespy as lp

# connect to a local testnet node
lp.setNode(node = 'http://127.0.0.1:5555', chain = 'testnet')

myAddress = lp.Address(privateKey = 'CsBpQpNE3Z1THNMS9vJPaXqYwN9Hgmhd9AsAPrM3tiuJ')
minerAddress = lp.Address('3NBThmVJmcexzJ9itP9KiiC2K6qnGQwpqMq')

# lease 1000 Lunes to minerAddress
leaseId = myAddress.lease(minerAddress, 100000000000)

# revoke the lease
myAddress.leaseCancel(leaseId)

```


### Using PyLunes in a Python shell

#### Check an address balance:
```
>>> import lunespy as lp
>>> lp.Address('37mCm11kpfQWiYaJuPJJG65PhgyhCQtqLxL')
address = 37mCm11kpfQWiYaJuPJJG65PhgyhCQtqLxL
publicKey =
privateKey =
seed =
balances:
  lunes = 1186077288304570
  BDMRyZsmDZpgKhdM7fUTknKcUbVVkDpMcqEj31PUzjMy (Tokes) = 43570656915
  RRBqh2XxcwAdLYEdSickM589Vb4RCemBCPH5mJaWhU9 (Ripto Bux) = 4938300000000
  4rmhfoscYcjz1imNDvtz45doouvrQqDpbX7xdfLB4guF (incentCoffee) = 7
  Ftim86CXM6hANxArJXZs2Fq7XLs3nJvgBzzEwQWwQn6N (Lunes) = 2117290600000000
  E4ip4jzTc4PCvebYn1818T4LNoYBVL3Y4Y4dMPatGwa9 (BitCoin) = 500000000000
  FLbGXzrpqkvucZqsHDcNxePTkh2ChmEi4GdBfDRRJVof (Incent) = 12302659925430
  GQr2fpkfmWjMaZCbqMxefbiwgvpcNgYdev7xpuX6xqcE (KISS) = 1000
  DxG3PLganyNzajHGzvWLjc4P3T2CpkBGxY4J9eJAAUPw (UltraCoin) = 200000000000000
  4eWBPyY4XNPsFLoQK3iuVUfamqKLDu5o6zQCYyp9d8Ae (LIKE) = 1000
>>>
```

#### Generate a new address:
```
>>> import lunespy as lp
>>> lp.Address()
address = 3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh
publicKey = EYNuSmW4Adtcc6AMCZyxkiHMPmF2BZ2XxvjpBip3UFZL
privateKey = CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S
seed = seven wrist bargain hope pattern banner plastic maple student chaos grit next space visa answer
balances:
  Lunes = 0
>>>
```

#### Check an asset:
```
>>> import lunespy as lp
>>> lp.Asset('DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J')
status = Issued
assetId = DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J
issuer = 3PPKF2pH4KMYgsDixjrhnWrPycVHr1Ye37V
name = LunesCommunity
description = Lunes community token.
quantity = 1000000000
decimals = 2
reissuable = False
```


### Offline signing and custom timestamps

#### Offline signing a future transaction:
```
>>> import lunespy as lp
>>> lp.setOffline()
>>> myAddress=lp.Address(privateKey="F2jVbjrKzjUsZ1AQRdnd8MmxFc85NQz5jwvZX4BXswXv")
>>> recipient=lp.Address("3P8Ya6Ary5gzwnzbBXDp3xjeNG97JEiPcdA")
# sign a future tx to transfer 100 LUNES to recipient
# the tx is valid on Jan 1st, 2020 12:00pm
>>> myAddress.sendLunes(recipient, amount=100e8, timestamp=1577880000000)
{'api-endpoint': '/assets/broadcast/transfer',
 'api-type': 'POST',
 'api-data': '{"fee": 100000,
			   "timestamp": 1577880000000,
			   "senderPublicKey": "27zdzBa1q46RCMamZ8gw2xrTGypZnbzXs5J1Y2HbUmEv",
			   "amount": 10000000000,
			   "attachment": "",
			   "recipient": "3P8Ya6Ary5gzwnzbBXDp3xjeNG97JEiPcdA"
			   "signature": "YetPopTJWC4WBPXbneWv9g6YEp6J9g9rquZWjewjdQnFbmaxtXjrRsUu69NZzHebVzUGLrhQiFFoguXJwdUn8BH"}'}
```


## Connecting to a different node or chain

LunesPy supports both mainnet and testnet chains. By default, LunesPy connects to the mainnet RPC server at https://https://lunesnode.lunes.io. It's possible to specify a different server and chain with the setNode() function

```python
import lunespy as lp

# connects to a local testnet node
lp.setNode(node = 'http://127.0.0.1:5555', chain = 'testnet')

# connects to a local mainnet node
lp.setNode(node = 'http://127.0.0.1:5555', chain = 'mainnet')

```


## License
Code released under the [MIT License](https://github.com/LunesCommunity/LunesPy/blob/master/LICENSE).
