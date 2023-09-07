import glob

def process_file(data):
    # convert all characters to lowercase for the count
    data = data.lower()
    # replace all grammar and line breaks to have only words and spaces
    data = data.replace(",", "").replace(".", "").replace("\n", " ")
    # separate each word into a list
    data = data.split(" ")
    return data
    
def find_most_common(data):
    # could be much more elegant using a different method
    count_list = {}
    # find number of occurances of each word
    for word in data:
        if word in count_list.keys():
            count_list[word] += 1
        else:
            count_list[word] = 1
    # find most common
    maxKey = max(count_list, key=count_list.get)
    most_common = (maxKey, count_list[maxKey])
    return most_common

def start_search():
    file_list = glob.glob('Week-7/Exercise Files/02/*.txt')
    data = []
    for item in file_list:
        with open(item, 'r') as f:
            # may be better to use readline() and loop through each line
            reader = f.read()
            words = process_file(reader)
            for word in words:
                data.append(word)
    print(find_most_common(data))

if __name__ == "__main__":
    start_search()



# finish answer and write better response