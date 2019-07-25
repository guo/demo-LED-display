from client import IoTeXClient

import time
import sys
import codecs
import led

url = "http://159.89.223.147:14004/"
wallet = u"io1qyqsqqqqdjqgzp2h0ffzwmkcglvm25c2ac0xmnelwd7kvy"
payload = "Hello CES!"

if __name__ == "__main__":
  client = IoTeXClient(url)
  offset = 0
  count = 1
  starttime = time.time()
  try:
    existing_transfers = client.getTransfersByAddress(wallet, 0, 99999999)
    offset = len(existing_transfers)
    if offset>0:
      offset=offset-4
    print "found ", offset, "transfers, listening to new transfers"
  except:
    print "no transfers found!"

  while True:
    try:
      transfers = client.getTransfersByAddress(wallet, offset, count)
      offset += count
      for transfer in transfers:
        if len(transfer["payload"])>0 and transfer["recipient"]==wallet:
          payload = codecs.decode(transfer["payload"], "hex").decode('utf-8')
          if len(payload)>100:
            payload = payload[:100]+"..."
          print "new msg:", payload

    except:
      time.sleep(2)

    if len(payload)>0:
      led.displayMessage(4, -90, 0, payload)
