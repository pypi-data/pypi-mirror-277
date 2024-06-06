#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shi4712
@description: 
@version: 1.0.0
@file: downloaderTest.py
@time: 2024/6/6 15:07
"""

if __name__ == '__main__':
    from ArticleAnalyst.function.downloader import Downloader
    testUrl = "scRNA"
    pubmed_email = ''   # Always tell NCBI who you are

    downloader = Downloader(pubmed_email)
    testRecords, failedUrls = downloader.download(testUrl)

    print(len(testRecords))
    PMIDList = []
    for record in testRecords:
        try:
            PMIDList.append(record["PMID"])
        except KeyError:
            continue

    print("Total {} articles are downloaded successful for {}!".format(len(set(PMIDList)), testUrl))

