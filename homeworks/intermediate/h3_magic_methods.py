# -*- coding: utf-8 -*-
"""
1. implement a class representing a music track:

* music track should have common attributes such as (you can add more if you want):

    - name
    - duration (in seconds)
    - singers (it's a list)
    - year
    # Q: what exactly is song meant to be?
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


# Q: why import runs teston...??


# Q : Why should I make attribute a private here?
#     When we use a property instead of attribute? we can make all attributes private and give getter method...
#     Should I define attributes on initialization or by setter later?


# todo change the attributes to _x (why not __x? for other class extensions)
#  and give them property or other access methods.


class MusicTrack:
    """ A class that represents a music track that has some functionalities."""

    def __init__(self, name, duration, year, genre, singers=None, song=''):

        # TODO: check for input argument type match

        # Q : what is the good design to control the duplicate name, or hash? on init? or by handler?

        self._name = name.title()
        self._duration = duration
        if singers is None:
            singers = []
        self._singers = singers
        self._year = year
        self._song = song
        self._genre = genre

    @property
    def name(self):
        return self._name

    @property
    def duration(self):
        return self._duration

    @property
    def year(self):
        return self._year

    @property
    def song(self):
        return self._song

    @property
    def genre(self):
        return self._genre

    @property
    def singers(self):
        return self._singers

    @song.setter
    def song(self, content):
        if isinstance(content, str):
            self._song = content
        else:
            print('Bad song content')

        # alt1:
        # Q: who should catch this?
        #   raise Exception('Bad song content!')

        # alt2:
        # try:
        #     self._song = content
        # except Exception:
        #     print('Bad song content!')

    def __hash__(self):
        return hash(self.name + str(self.duration) + str(self.year) + self.song)

    # why in lesson mono made other comparisons?
    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, MusicTrack):
            new_track_list = [self, other]
            PlayList.new_playlist_counter += 1
            return PlayList(f'new playlist {PlayList.new_playlist_counter}', new_track_list)
        else:
            raise TypeError

    def __str__(self):
        singers = ''
        for singer in self.singers:
            singers += singer + '-'
        singers = singers[:-1]
        printable = f'<{self.name} * {self.year} * {singers.upper()} * {self.duration}>'
        return printable


class PlayList:
    """A class for playlist of one or more MusicTracks."""

    new_playlist_counter = 0

    def __init__(self, name, mt_list):
        self._name = name
        self._tracks = list(dict.fromkeys(mt_list))
        self._duration = 0
        for mt in mt_list:
            self._duration += mt.duration

    @property
    def name(self):
        return self._name

    @property
    def tracks(self):
        return self._tracks

    @property
    def duration(self):
        return self._duration

    def __hash__(self):

        # Maybe this result is not unique.
        new_hash = 0
        for mt in self.tracks:
            new_hash += mt.__hash__()
        return new_hash

    def __eq__(self, other):
        if hash(self.tracks) == hash(other):
            return True
        else:
            return False

    def __str__(self):
        printable = ''
        for mt in self.tracks:
            printable += mt.__str__() + '\n'
            # If I wanted to make a single string?
        return printable

    def __add__(self, other):
        return self.__return_addition(other)

    def __return_addition(self, other):
        """facilitator function to use in add functions in PlatList class."""
        if isinstance(other, PlayList):
            new_tracklist = self.tracks + other.tracks
            # Q: why this does not work:
            # new_tracklist = self.tracks.extend(other.tracks)
        elif isinstance(other, MusicTrack):
            new_tracklist = self.tracks + [other]
        else:
            # todo maybe better type of Exception can be raised. search
            raise TypeError
        # Q: this does not work on more than one "+"
        PlayList.new_playlist_counter += 1
        return PlayList(f'new playlist{PlayList.new_playlist_counter}', new_tracklist)

    def add_new(self, track):
        # Q: Is it ok?
        new_obj = self.__return_addition(track)
        self.__dict__.update(new_obj.__dict__)

    def play(self):
        print(f'From playlist {self.name} playing: ')
        for track in self.tracks:
            print(f'Now: {track.name}: {track.song}')


mt_1 = MusicTrack('Unforgiven', 360, 1987, 'Trash Metal', singers=['Metallica'])
mt_2 = MusicTrack('Saaghi', 200, 1980, 'Persian Pop', singers=['Ahmad Azad'])
print(mt_1)

# prevents duplicate?
pl_1 = mt_1 + mt_1
print(pl_1)

# check for "+":
pl_2 = mt_1 + mt_2
print(pl_2)

mt_3 = MusicTrack('Reveal', 180, 1999, 'POP')
pl_2 = mt_1 + mt_2 + mt_3
print(pl_2)

pl_1.add_new(mt_2)
pl_2 = mt_2 + mt_3
print(pl_1)
print(pl_2)

pl_3 = pl_1 + pl_2
print(pl_3)

mt_1.song = 'New blood joins this earth...'
pl_3.play()

mt_1.song = 12
pl_3.play()

mt_3.song = 'Reveal, when you ...'
pl_3.play()