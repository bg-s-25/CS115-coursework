'''
Created on Nov 12, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 10
'''

import sys

SAMPLE_FILE_CONTENT = \
'''dave:alanis Morrisset, Khaled, Michael Jackson
sue:Kate Bush,Nirvana,Michael Jackson'''
loaded_users = [] # list of strings containing users
loaded_artists = [] # list of lists, each has artists for each user
current_user = ''
current_user_index = -1

def read_print_user_prefs(filename):
    ''' Assume filename is path to an existing file in the format above; 
    read each user name and a list of the user's preferences '''
    input_file = open(filename, 'r')
    for line in input_file: # one line at a time
        user, artists = line.split(':')
        artists = artists.split(',')
        for i in range(len(artists)):
            artists[i] = artists[i].strip()
        user = user.strip()
        loaded_users.append(user)
        loaded_artists.append(artists)
        # print(user + ' : ' + str(artists))
    input_file.close() # close file

def write_prefs(filename):
    ''' Open existing or new file named filename; 
    write all user names and preferences for each user to it '''
    output_file = open(filename, 'w')
    lines = ''
    for i in range(len(loaded_users)):
        pending_prefstring = loaded_users[i] + ':'
        for j in range(len(loaded_artists[i])):
            pending_prefstring += loaded_artists[i][j] + ','
        pending_prefstring = pending_prefstring[:-1] # removes trailing comma
        if i < len(loaded_users) - 1:
            lines += pending_prefstring + '\n'
        else:
            lines += pending_prefstring
    lines = lines.split('\n') # split into lines, for sake of example; lines is a list of strings
    for line in lines:
        output_file.write(line + '\n')
    output_file.close()
    
def prompt_prefs(new_user = False):
    ''' Prompt user for artist preferences; will keep prompting until empty string is entered; 
    set new_user parameter to True if the user is new (will be added to loaded_users) '''
    inputartist = 'a'
    new_artists = []
    while inputartist != '':
        inputartist = input('Enter an artist that you like (Enter to finish): ')
        if inputartist != '': new_artists.append(inputartist)
    new_artists = sort(new_artists)
    if new_user:
        loaded_users.append(current_user)
        loaded_artists.append(new_artists)
    else:
        for i in range(len(loaded_users)):
            if loaded_users[i] == current_user:
                loaded_artists[i] = new_artists
    
def recommendations():
    ''' Find recommendations for the current user using artists from other users that have 2 or more artists in common 
    while ignoring private users and users with the same exact preferences; display recommended artists in alphabetical order '''
    recs = []
    for i in range(len(loaded_users)):
        if loaded_users[i] == current_user or loaded_users[i][-1] == '$': continue # exclude data from private users
        for itm in loaded_artists:
            if sort(itm) == sort(loaded_artists[current_user_index]):
                # exactly the same preferences, ignore
                continue
            common_artists = 0
            for artist in itm:
                if artist in loaded_artists[current_user_index]:
                    common_artists += 1
            if common_artists >= 2:
                for artist in itm:
                    if artist not in recs: recs.append(artist)
    if recs == []:
        print('No recommendations available at this time')
        return
    sorted_recs = sort(recs)
    for artist in sorted_recs:
        print(artist)

def popular_artists(showhowpopular = False):
    ''' Find the most popular artist(s) based on the number of users who are interested in the artist; 
    if parameter showhowpopular is True, display the number of hits for the most popular artist(s); 
    if parameter showhowpopular is False, display the name of the artist(s) who has/have the most hits '''
    artist_hits = []
    for i in range(len(loaded_artists)):
        for artist in loaded_artists[i]:
            if loaded_users[i][-1] == '$': continue # exclude data from private users
            if artist_hits == []:
                artist_hits.append([artist, 1])
            else:
                for j in range(len(artist_hits)):
                    if artist == artist_hits[j][0]:
                        artist_hits[j][1] += 1
                        break
                    if j == len(artist_hits) - 1: artist_hits.append([artist, 1])
    if artist_hits == []:
        print('Sorry, no artists found')
        return
    artist_hits = sort_basedonindex(artist_hits, 1)
    artist_hits.reverse()
    init_hits = artist_hits[0][1]
    if showhowpopular == True:
        print(init_hits)
    else:
        sorted_top_artists = []
        for itm in artist_hits:
            if itm[1] == init_hits: sorted_top_artists.append(itm[0])
        sorted_top_artists = sort(sorted_top_artists)
        for artist in sorted_top_artists:
            print(artist)
                
def most_likes():
    ''' Find the user(s) with the most liked artists; display the names of the user(s) with the most liked artists in alphabetical order '''
    sorted_likes_users = []
    for i in range(len(loaded_users)):
        if loaded_users[i][-1] == '$': continue # exclude data from private users
        sorted_likes_users.append([len(loaded_artists[i]), loaded_users[i]])
    sorted_likes_users = sort_basedonindex(sorted_likes_users, 0)
    sorted_likes_users.reverse()
    init_likes = sorted_likes_users[0][0]
    sorted_top_users = []
    for itm in sorted_likes_users:
        if itm[0] == init_likes: sorted_top_users.append(itm[1])
    sorted_top_users = sort(sorted_top_users)
    for user in sorted_top_users:
        print(user)
        
def save_quit():
    ''' Save preferences and write them to a file '''
    write_prefs('musicrecplus.txt')

def show_menu():
    ''' Display the menu and prompt the user for a menu option '''
    inputmenu = input('Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n')
    while inputmenu != '':
        if inputmenu == 'e':
            prompt_prefs(False)
            show_menu()
        elif inputmenu == 'r':
            recommendations()
            show_menu()
        elif inputmenu == 'p':
            popular_artists()
            show_menu()
        elif inputmenu == 'h':
            popular_artists(True)
            show_menu()
        elif inputmenu == 'm':
            most_likes()
            show_menu()
        elif inputmenu == 'q':
            write_prefs('musicrecplus.txt')
            sys.exit(0)
        else:
            show_menu()
    show_menu()
        
def sort(lst):
    ''' Return sorted list lst '''
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def sort_basedonindex(lst, index):
    ''' Return sorted list lst according to the values in its index index '''
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i][index] > lst[j][index]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
    
# START - read preferences from file and prompt for user name
try:    
    read_print_user_prefs('musicrecplus.txt')
except IOError as error:
    # print(error)
    pass # ignore and prompt for user name
    
current_user = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
if current_user in loaded_users:
    for i in range(len(loaded_users)):
        if loaded_users[i] == current_user:
            current_user_index = i
    show_menu()
else:
    current_user_index = len(loaded_users)
    prompt_prefs(True)
    show_menu()
