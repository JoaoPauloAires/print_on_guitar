import urllib, re, os

# CONSTANTS

extract_rows = re.compile(r'<tr>.+?</tr>', re.DOTALL)
get_title    = re.compile(r'title.+?</a')
between      = re.compile(r'>.+?<')
get_th       = re.compile(r'<th.+?</th', re.DOTALL)
get_song     = re.compile(r'[A-Z0-9][A-Za-z\-\' 0-9\.]+')
url          = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_Iron_Maiden'

def get_html():
# return the html from the URL

    html_text = urllib.urlopen(url)
    return html_text.read()

def extract_songs(html_text):
    rows = extract_rows.findall(html_text)

    songs = []

    for row in rows:
        if select_name.findall(row):
            th = get_th.findall(row)
            if th:
                title = get_title.findall(th[0])

                if title:
                    middle = between.findall(title[0])
                    if middle:
                        result = get_song.findall(middle[0])
                        if result:
                            songs.append(result[0])
                else:
                    result = get_song.findall(th[0])
                    if result:
                        songs.append(result[0])    
    return songs

if __name__ == "__main__":

    html_text = get_html()    

    name = raw_input("Insert the musician name (Paul Di'Anno, Dave Murray, Bruce Dickinson, Steve Harris, Adrian Smith, Janick Gers, Blaze Bayley, and Nicko McBrain): ")
    select_name  = re.compile(name)
    save = input("Do you want to save the music list in a file? 0 for 'no' and 1 for 'yes': ")

    songs = extract_songs(html_text)

    if not save:
        print "\n" + name + " has a total of " + str(len(songs)) + " musics.\n"
        
        for song in songs:
            print "- " + song
    else:
        file_name = raw_input("Please, insert the file name: ")
        folder_name = "Lists of musics"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        song_list = open(folder_name + "/" + file_name + ".txt", 'w')

        song_list.write(name + "'s musics (" + str(len(songs)) + "):\n\n")

        for song in songs:
            song_list.write("- " + song + "\n")
