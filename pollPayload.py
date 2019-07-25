from client import IoTeXClient

import time
import sys
import codecs
import led

address = "http://159.89.223.147:14004/"
smartContractAddress = "io1qyqsyqcyp8ghcfzxq9kklj0qclst6g4chpgu5s28l5vkm9"
def getExecutions(height, blockId):
	offset = 0
	count = 10
	fetch = True

	while fetch:
		try:
			executions = client.getExecutionsByBlockID(blockId, offset, count)
			offset += count

			for e in executions:
				if e['contract'] == smartContractAddress:
					payload = codecs.decode(e['data'][8:], "hex").decode('utf-8')
					led.displayMessage(4, -90, 0, payload)
					print payload

		except:
			break

if __name__ == "__main__":
    client = IoTeXClient(address)
    try:
    	curHeight = client.getLatestBlockHeight()
    except:
    	print('Could not get latest block height...')

    lastFetchedBlock = 0
    while True:
    	height = client.getLatestBlockHeight()
    	if curHeight < height and lastFetchedBlock != curHeight:
	    	print curHeight

	    	try:
	    		block = client.getLastBlocksByRange(curHeight, 1)
	    		getExecutions(curHeight, block[0]['ID'])
	    		lastFetchedBlock = curHeight
	    		curHeight += 1
	    	except:
	    		print('Failed to fetch', curHeight)

		time.sleep(1)
