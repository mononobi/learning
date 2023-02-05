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

    def __init__(self, name: str, duration, year, genre, singers=None, song=''):

        # TODO: check for input argument type match

        # Q : what is the good design to control the duplicate name, or hash? on init? or by handler?

        self.name = name.title()
        self.duration = duration
        # self._singers = singers
        # if self.singers is None:
        #     self._singers = []
        self.singers = singers
        self.year = year
        self.song = song
        self.genre = genre
        self._test = None

    def test(self, value):
        self._test = value

    def get_test(self):
        return self._test
    # @property
    # def name(self):
    #     return self._name

    # @property
    # def duration(self):
    #     return self._duration

    # @property
    # def year(self):
    #     return self._year

    # @property
    # def genre(self):
    #     return self._genre

    @property
    def song(self):
        return self._song

    @song.setter
    def song(self, content):
        if isinstance(content, str):
            self._song = content
        else:
            print('Bad song content')

    # alt1:
    # Q: who should catch this on initialization?
    #   raise Exception('Bad song content!')

    @property
    def singers(self):
        return self._singers

    @singers.setter
    def singers(self, list1):
        if isinstance(list1, list):
            self._singers = list1
        else:
            self._singers = []

    def __hash__(self):
        return hash(f'{self.name}{self.duration}{self.year}{self.song}')

    # why in lesson mono made other comparisons?
    def __eq__(self, other):
        if not isinstance(other, MusicTrack):
            return False

        return hash(self) == hash(other)

    def __add__(self, other):
        if isinstance(other, MusicTrack):
            return PlayList(self, other)
        else:
            raise TypeError()

    def __str__(self):
        singers = ' - '.join(self.singers)
        return f'<{self.name} * {self.year} * {singers} * {self.duration}>'


class PlayList:
    """A class for playlist of one or more MusicTracks."""

    def __init__(self, *music_track, name=None):
        if not name:
            name = f'Unknown Playlist'
        self.name = name
        self._tracks = list(music_track)
        self._duration = 0
        for track in music_track:
            self._duration += track.duration

    # @property
    # def name(self):
    #     return self._name

    @property
    def tracks(self):
        return self._tracks

    @property
    def duration(self):
        return self._duration

    def __hash__(self):
        # Maybe this result is not unique.
        return hash(tuple(self.tracks))

    def __eq__(self, other):
        if not isinstance(other, PlayList):
            return False

        return hash(self) == hash(other)

    def __str__(self):
        return '\n'.join([str(item) for item in self.tracks])

    def __add__(self, other):
        tracks = []
        tracks.extend(self.tracks)
        if isinstance(other, PlayList):
            tracks.extend(other.tracks)
            # Q: why this does not work:
            # new_tracklist = self.tracks.extend(other.tracks)
        elif isinstance(other, MusicTrack):
            tracks.append(other)
        else:
            # todo maybe better type of Exception can be raised. search
            raise TypeError()

        return PlayList(*tracks)

    def add_new(self, track):
        # Q: Is it ok?
        self.tracks.append(track)

    def play(self):
        print(f'From playlist {self.name} playing: ')
        for track in self.tracks:
            print(f'Now: {track.name}: {track.song}')


# Q: How can we automatically combine the name of instance and attribute of object?


mt_1 = MusicTrack('Unforgiven', 360, 1987, 'Trash Metal', singers=['Metallica'])
mt_2 = MusicTrack('Saaghi', 200, 1980, 'Persian Pop', singers=['Ahmad Azad', 'Siroos'])
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
