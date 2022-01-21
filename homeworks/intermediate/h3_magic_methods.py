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

    - when we sum two play lists, it should return a play list object with
      all the tracks of both play lists (removing duplicates).

    - when we sum a play list with a music track, it should return a play list object
      with the music track added to it (if it's not already added)

    - a function to add new tracks to the play list (if it's not already added)

    - a function to play the play list, and print the song of each track.

* consider all available options when implementing, and use the
  correct option (property, attribute, access levels, ...)

happy coding :)
"""
