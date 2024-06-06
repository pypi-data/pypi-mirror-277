#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shi4712
@description: 
@version: 1.0.0
@file: ArticleTest.py
@time: 2024/6/6 14:32
"""

if __name__ == '__main__':
    import json

    from ArticleAnalyst.function.article import Article

    with open("./HCM_major.json") as f:
        obj = json.load(f)

    article = Article(dataSource="file", record=obj[24])
    article.setDocument()

    print(article)

    # add attr
    article.addValue("test", "Hello World")
    print(article.test)
    try:
        article.addValue("GR", "CN 001")
    except ValueError as e:
        print(e)

    # del attr
    article.delValue("test")
    try:
        print(article.test)
    except AttributeError as e:
        print(e)
    try:
        article.delValue("Journal")
    except ValueError as e:
        print(e)

    # modify attr
    GRValue = article.GR
    print(GRValue)
    article.modifyValue("GR", ["CN 001"])
    print(article.GR)
    article.modifyValue("GR", GRValue)
    try:
        article.modifyValue("Journal", "Nature")
    except ValueError as e:
        print(e)

    # query attr
    print(article.queryValue("MH"))
    print(article.queryValue("MH", ["Humans"]))
    print(article.queryValue("MH", ["It should be False"]))

    print("Article Class Test has been finished successfully.")