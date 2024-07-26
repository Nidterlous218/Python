def make_album(artist, album_title, number_of_tracks):
    """Builds a dictionary describing a music album."""
    save_album = {'artist': artist.title(), 'album_title': album_title.title(), 'number_of_tracks': number_of_tracks}
    return save_album

while True:
    print("\nPlease insert the details of the album")
    print("Enter 'q' to exit the loop")
    artist = input("\nArtist: ")
    if artist == 'q':
        break

    album_title = input("Album: ")
    if album_title == 'q':
        break
    
    number_of_tracks = input("Number of tracks: ")

    if number_of_tracks == "":
        number_of_tracks = 0
    
    album = make_album(artist, album_title, str(number_of_tracks))
    print(album)