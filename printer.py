import StringIO

def print_new_posts(list_to_print):
    for item in list_to_print:
        print str(item['time']) + " " + str(item['author'])
        print str(item['body'])
        print


