#!/usr/bin/env python
# -*- coding: utf-8 -*-

from transferdata import TransferData

def main():
	access_token = 'AtomX_Packs_Collection_2023.part10.rar'	# get your access token from Dropbox Developers
	transferData = TransferData(access_token)

	file_from = '10.rar'
	file_to = '10.rar'	# The full path to upload the file to, including the file name


	# API v2
	transferData.upload_file(file_from=file_from, file_to=file_to)

if __name__ == '__main__':
	main()
