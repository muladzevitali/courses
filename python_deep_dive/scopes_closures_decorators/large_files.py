import pandas
import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
data = [[ random.choice(WORDS) for _ in range(7)] for _ in range(2_000_000)]
dataframe = pandas.DataFrame(data, columns=("a", "b", "c", "d", "e", "f", "g"))

dataframe.to_csv("test.csv", compression='gzip')