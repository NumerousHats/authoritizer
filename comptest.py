import jellyfish
import pandas as pd
import sys

df = pd.read_csv("testdat/huge_real_life.csv")

messy = df['vendor'].dropna().values.tolist()
messy = list(set(messy))

authorities = df['canonical firm'].dropna().values.tolist()
authorities = list(set(authorities))

for mess in messy:
    try:
        mess=mess.decode('utf8').encode('latin1').decode('utf8')
    except:
        continue # i.e. give up...
    for auth in authorities:
        auth = unicode(auth)
        score = jellyfish.jaro_winkler(mess, auth)
        if score > 0.8:
            print "{} vs {} gives {}".format(mess, auth, score)