# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_csv("EAFL _ Matching - dataset (1).csv")

TEMAS = list(set(df["TEMA"].values))


PESSOAS = list(set(df["PESSOA"].values))