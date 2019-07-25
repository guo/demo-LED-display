from client import IoTeXClient

import time
import sys
import codecs

url = "http://159.89.223.147:14004/"
wallet = u"io1qyqsqqqqdjqgzp2h0ffzwmkcglvm25c2ac0xmnelwd7kvy"
payload = "Hello CES!"
i = 0

if __name__ == "__main__":
  client = IoTeXClient(url)
  offset = 0
  count = 1

  starttime = time.time()
  existing_transfers = client.getTransfersByAddress(wallet, 0, 99999999)
  for transfer in existing_transfers:
    if len(transfer["payload"])>0 and transfer["recipient"]==wallet:
      try:
        payload = codecs.decode(transfer["payload"], "hex").decode('utf-8')
        print i, "new msg:", payload
      except:
        print i, "cannot decode"
    i=i+1
