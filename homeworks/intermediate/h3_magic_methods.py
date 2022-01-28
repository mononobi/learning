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


class music_track():
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

        def __hash__(self):
            return hash(self.__name + str(self.__duration) + str(self.__year) + self.__song)

        def __eq__(self, other):
            if not isinstance(other, music_track):
                return False
            if __hash__(self) == __hash__(other):
                return True
            return False


my_track = music_track('hamegi Salam', 600 , ['Mahasti'], 1985, 'song')
your_track = music_track('hamegi Salam', 600 , ['Mahasti'], 1985, 'song')

print(hash(my_track))
print(hash(your_track))
print(my_track == your_track)















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
