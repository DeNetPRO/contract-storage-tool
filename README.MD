# Contract Storage Tool

## Install

1. Clone this repo
2. Install web3 py

```bash
pip install web3
```

## Run

```bash
python3 main.py
```

**get result something like this:**

| Network Name | Network ID | Contract Name  | Address                            |
|--------------|------------|----------------|------------------------------------|
|  Polygon  |  137  |  daowallet  | 0x6261E1AAc369CD694093455f9e2B65b31AcEdDa1 |
|  Polygon  |  137  |  pairtoken  | 0x081Ec4c0e30159C8259BAD8F4887f83010a681DC |
|  Polygon  |  137  |  proofofstorage  | 0x4d37D386462D16e25079E5c6d24f5176E64C4118 |
|  Polygon  |  137  |  userstorage  | 0xC719dA7cec15A8dEF5488528498315F5A0b8d48d |
|  Polygon  |  137  |  gastoken  | 0x1a9b54A3075119f1546C52cA0940551A6ce5d2D0 |
|  Polygon  |  137  |  nodenft  | 0xCb19BedE3e4F64B6B0085D99127F6d0A25b7180D |
|  Polygon  |  137  |  charity_pos  | 0x013e9F8cf67D3cf74789096A393fcAD2A154084F |
|  Polygon  |  137  |  gastoken_mined  | 0xF98590aaeAcaC2Abfe29126b5BE8793714dc7553 |



## Modify by your self

open main.py and edit it by yourserlf

```python3
w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com')) # RPC URL
contract_storage_address = "0xB6b309Ae66A12d69259566220A2D0e35fE4bC556" # Contract Storage Address
```