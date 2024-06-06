#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .articleAnalyst import ArticleAnalyst
from .function.meshAnalyst import MeSHAnalyst

import os
baseDir = os.path.dirname(os.path.abspath(__file__))
saveDir = os.path.join(baseDir, "download", "test")  # The dir to save article information downloaded from PubMed
ArticleAnalyst.saveDir = saveDir
if not os.path.exists(saveDir):
    os.mkdir(saveDir)
