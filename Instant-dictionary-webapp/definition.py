import pandas as pd

class Definition:
    def __init__(self,text):
        self.text = text

    def get(self):
        df = pd.read_csv('data.csv')
        # coverting the datatype to tuple since it can append multiple synonyms for the given word
        return tuple(df.loc[df['word']== self.text]['definition'])

# d = Definition('Sun')
# print(d.get())

