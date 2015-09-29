import jellyfish
import pandas as pd
import sys

df = pd.read_csv("testdat/huge_real_life.csv")

messy = df['vendor'].dropna().values.tolist()
messy = list(set(messy))

authorities = df['canonical firm'].dropna().values.tolist()
authorities = list(set(authorities))

all_scores = dict()

for mess in messy:
    try:
        # mess=mess.decode('utf-16').encode('utf-8')
        mess= unicode(mess)
    except:
        print mess # i.e. give up...

    scores = [ [x, jellyfish.jaro_winkler(mess, unicode(x))] for x in authorities]
    scores = sorted(scores, key=lambda score: -score[1])[0:9]
    all_scores[mess] = scores

print all_scores
    