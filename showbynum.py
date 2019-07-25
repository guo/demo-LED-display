from client import IoTeXClient

import time
import sys
import codecs
import sys
import led

if len(sys.argv)<2:
    print sys.argv[0], "the number of msg"
show_num=int(sys.argv[1])

url = "http://159.89.223.147:14004/"
wallet = u"io1qyqsqqqqdjqgzp2h0ffzwmkcglvm25c2ac0xmnelwd7kvy"
payload = "Hello CES!"

if __name__ == "__main__":
  client = IoTeXClient(url)
  offset = 0
  count = 1
  starttime = time.time()

  starttime = time.time()
  existing_transfers = client.getTransfersByAddress(wallet, 0, 99999999)
  transfer = existing_transfers[show_num]
  if len(transfer["payload"])>0 and transfer["recipient"]==wallet:
    try:
      payload = codecs.decode(transfer["payload"], "hex").decode('utf-8')
      print "msg:", payload
    except:
      print "cannot decode"

    if len(payload)>0:
      while True:
        led.displayMessage(4, -90, 0, payload)
        time.sleep(1)

