# To read binary data we open file in 'rt' 
# To read binary data we open file in 'wt'

with open('Star Wars.json', 'rb') as s:
    data = s.read()
    print(data)

    with open("new.json", "wb") as d:
        d.write(data)

data.close()
