import numpy as np
import pandas as pd

# ipl_matches= "ipl-matches.csv" # Path to the file
ipl_matches= "https://docs.google.com/spreadsheets/d/e/2PACX-1vTgCcxYBcqxUAuYHgrqUPsdXpausK3AF-B712JJaGHHA6BKtN3LCuoiJ1VQakm_umUU1nNkxy2K79QA/pub?output=csv"
matches=pd.read_csv(ipl_matches)

print(matches.head(5))


