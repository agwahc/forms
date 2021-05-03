class start:
    def access(self):
        a = open('note.txt', 'r')
        b = []
        for i in a:
            x = str.casefold(i)
            b.append(x.split())
        return b

    def populate(self): # populates dbk
        # searches for meaning, for unsearched words in the dbk words column and fills in info
        d =