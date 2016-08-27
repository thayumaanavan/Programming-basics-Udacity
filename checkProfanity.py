import urllib

def read_text():
    quotes=open("./movie_quotes.txt")
    contents=quotes.read()
    #print(contents)
    quotes.close()
    check_profanity(contents)


def check_profanity(text):
    conn=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=conn.read()
    #print(output)
    conn.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("doc is clear of profanity")
    else:
        print("error-could not scan the doc")
        
        
read_text()

