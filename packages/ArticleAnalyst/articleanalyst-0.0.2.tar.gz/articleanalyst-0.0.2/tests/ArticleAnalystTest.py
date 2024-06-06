#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shi4712
@description: 
@version: 1.0.0
@file: ArticleAnalystTest.py
@time: 2024/6/6 14:48
"""
from ArticleAnalyst import ArticleAnalyst

if __name__ == '__main__':
    pubmed_email = ''  # Always tell NCBI who you are

    articleAnalyst = ArticleAnalyst(
        dataSource="file", filePath="./HCM_major.json",
        email=pubmed_email,
    )

    # ArticleAnalyst basic function test
    newArticles1 = articleAnalyst.getArticles('1185292')
    newArticleAnalyst1 = ArticleAnalyst(dataSource="self", articles=newArticles1)

    newArticles2 = articleAnalyst.getArticles(['1185292', '36797483'])
    newArticleAnalyst2 = ArticleAnalyst(dataSource="self", articles=newArticles2)

    ArticleAnalyst.concat([newArticleAnalyst1, newArticleAnalyst2])
    articleAnalyst.dropNa(subset="MH")
    articleAnalyst.dropNa(subset=["MH", "PG"])
    articleAnalyst.dropNa(subset=["MH", "PG"], how="all")

    articleAnalyst = ArticleAnalyst(
        dataSource="file", filePath="./HCM_major.json",
    )
    articleAnalyst.search(Year=[(">", 2000)])
    articleAnalyst.search(Year=[(">", 2000), ("<", 2015)], how="all")
    articleAnalyst.search(Year=[(">", 2000), ("<", 2015)], how="any")
    articleAnalyst.search(
        Year=[(">", 2000), ("<", 2015)],
        Journal=[("get", "Journal Abbrs"), ("contains", "Nature")],
        how="all"
    )

    citGraph = articleAnalyst.getCit()

    # ArticleSet embedding function test
    targetArticleAnalyst = articleAnalyst.search(Year=[(">", 2022)])

    targetArticleAnalyst.setMeSHAnalyst()
    targetArticleAnalyst.projectArticles(
        dimensions=["Proteins", "Diseases Category"],
        keyAdded="Embedding",
    )
    print("!")
    matrix = targetArticleAnalyst.returnDistanceMatrix(reference="Embedding")
    meshDistribution = articleAnalyst.returnYearDistribution(["MHDict"])

    # association analysis test
    articleAnalyst = articleAnalyst.search(Year=[(">", 2005)])
    articleAnalyst.setMeSHAnalyst()
    articleAnalyst.associationAnalysis(rowCategories=["Heart Septum"], colCategories=["Diseases Category"])

    # ArticleAnalyst enrichment analysis test
    targetArticleAnalyst = articleAnalyst.search(Year=[(">", 2000)])
    targetArticleAnalyst.setMeSHAnalyst()
    targetArticleAnalyst.enrichmentAnalysis(other="background", root="Carrier Proteins")

    print("????")

