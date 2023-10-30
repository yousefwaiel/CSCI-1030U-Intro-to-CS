paragraph = "Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, making it the world's second-largest country by total area, with the world's longest coastline. Its border with the United States is the world's longest international land border. The country is characterized by a wide range of both meteorologic and geological regions. It is a sparsely inhabited country of 40 million people, the vast majority residing south of the 55th parallel in urban areas. Canada's capital is Ottawa and its three largest metropolitan areas are Toronto, Montreal, and Vancouver."
words = paragraph.split(' ')
word_frequency = {}

for n in words:
    if n not in word_frequency.keys():
        word_frequency[n] = 0
    word_frequency[n] = word_frequency[n]+1

print(word_frequency)