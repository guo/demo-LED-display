#!/usr/bin/env python

import barrister
import argparse

class IoTeXClient(object):

	def __init__(self, address):
		trans  = barrister.HttpTransport(address)
		self.client = barrister.Client(trans)

	def getLatestBlockHeight(self):
		stats = self.client.Explorer.getCoinStatistic()
		return stats['height']

	def getLastBlocksByRange(self, offset, number):
		return self.client.Explorer.getLastBlocksByRange(offset, number)

	def getLastTransfersByRange(self, height, offset, number, showCoinbase):
		return self.client.Explorer.getLastTransfersByRange(height, offset, number, showCoinbase)

	def getTransfersByBlockID(self, blockId, offset, limit):
		return self.client.Explorer.getTransfersByBlockID(blockId, offset, limit)

	def getExecutionsByBlockID(self, blockId, offset, limit):
		return self.client.Explorer.getExecutionsByBlockID(blockId, offset, limit)

	def getTransfersByAddress(self, address, offset, limit):
		return self.client.Explorer.getTransfersByAddress(address, offset, limit)