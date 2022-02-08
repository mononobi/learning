# -*- coding: utf-8 -*-
"""
1. implement a class representing a music track:

* music track should have common attributes such as (you can add more if you want):

    - name
    - duration (in seconds)
    - singers (it's a list)
    - year
    - song (it must be a random string representing the real sound stream)

* music track should have these functionalities:

    - when making the hash of a music track, it must be generated
      using name, duration, year and song.

    - when comparing two music tracks for equality, it should return True
      if the name, duration, year and song of both tracks are equal.

    - when we sum two music tracks, it should return a play list object containing both tracks.

    - when printing a music track, it should print in this format:
      <NAME * YEAR * DASH_SEPARATED_SINGERS * DURATION>
 """
import homeworks.intermediate.utils as utils
import random


class MusicTrack:
    def __init__(self, name, duration, singers, year, song):
        utils.assert_positive_number(duration)
        utils.is_list(singers)
        utils.assert_valid_year(year)
        self.__name = name
        self.__duration = duration
        self.__singers = singers
        self.__year = year
        self.__song = song

    @property
    def name(self):
        return self.__name

    @property
    def duration(self):
        return self.__duration

    @property
    def singers(self):
        return self.__singers

    @property
    def year(self):
        return self.__year

    @property
    def song(self):
        return self.__song

    def __hash__(self):
       ## return hash(self.__name + str(self.__duration) + str(self.__year) + self.__song) # no need for str und concat
       return hash((self.__name, self.__duration, self.__year, self.__song))

    def __eq__(self, other):
        if not isinstance(other, MusicTrack):
            return False
        if not (hash(self) == hash(other)):
            return False
        return True

    def __add__(self, other):
        if not isinstance(other, MusicTrack):
            raise Exception('Only music tracks can be added up')
        ##track1 = dict(Name=self.__name, duration=self.__duration, singers=self.__singers, Year=self.__year, song=self.__song)
        ##track2 = dict(Name=other.__name, duration=other.__duration, singers=other.__singers, Year=other.__year, song=other.__song)
        ##return track1, track2
        return self, other # first learn music playlist and then do it

    def __str__(self):
        singers_str = '-'.join(sorted(self.__singers))
        message = '<{NAME} * {YEAR} * {DASH_SINGERS} * {DURATION}>'
        return message.format(NAME=self.__name, YEAR=self.__year, DASH_SINGERS=singers_str, DURATION=self.__duration)


my_track = MusicTrack('hamegi Salam', 600 , ['Mahasti'], 1985, 'song')
your_track = MusicTrack('hamegi Salam', 600 , ['Mahasti'], 1985, 'song')
my_track2 = MusicTrack('Sal Sal in chand sal', 600 , ['Hayede', 'Ebi'], 1980, ''.join(random.choice('abcde') for _ in range(4)))

##print(isinstance(my_track, MusicTrack))
##print(isinstance(your_track, MusicTrack))
print(hash(my_track))
print(hash(your_track))
print(my_track == your_track)
print(my_track + my_track2)
print(my_track)
print(my_track2)


"""
2. implement a class representing a play list:

* play list should have common attributes such as (you can add more if you want):

    - tracks (it's a list)
    - duration (total duration of all tracks)

* play list should have these functionalities:

    - when making the hash of a play list, it must be generated using
      the hash of all its tracks.

    - when comparing two play lists for equality, it should return True
      if both play lists have the same tracks.
      (do not use loop for detection, think about what you've learned on the last session).

    - when we sum two play lists, it should return a new play list object with
      all the tracks of both play lists (removing duplicates).

    - when we sum a play list with a music track, it should return a new play list object
      with all the tracks of original play list and the music track added
      to it (if it's not already added).

    - a function to add new tracks to the play list (if it's not already added)

    - a function to play the play list, and print the song of each track.

    - when printing a play list, it should print in this format:
    1. <NAME * YEAR * DASH_SEPARATED_SINGERS * DURATION>
    2. <NAME * YEAR * DASH_SEPARATED_SINGERS * DURATION>
    3. <NAME * YEAR * DASH_SEPARATED_SINGERS * DURATION>
    4. ...

* consider all available options when implementing, and use the
  correct option (property, attribute, access levels, ...)

happy coding :)
"""

class Playlist:
    def __init__(self, tracks):
        self._duration = 0
        utils.is_list(tracks)
        for index, track in enumerate(tracks):
            if not isinstance(track, MusicTrack):
                raise Exception('Object ' + str(index+1) + ' of the list is not a music track!')
            self._duration += track.duration
        self._tracks = tracks

    @property
    def duration(self):
        return self._duration

    @property
    def tracks(self):
        return self._tracks

    @staticmethod
    def add_music_track(self, new_track):
        if not isinstance(new_track, MusicTrack):
            raise Exception('Only music tracks are allowed in playlists')
        if not (new_track in self._tracks):
            self._tracks.append(new_track)






#my_playlist = Playlist([my_track, your_track])
#print(my_playlist.duration)


