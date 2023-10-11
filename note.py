import musicalbeeps
PITCH = 'ABCDEFGR'
ACCIDENTAL = ['sharp', 'flat', 'natural']

class Note:
    """ A class that store information about a melody.

    Attributes: duration, pitch, octave, accidental
    """
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    def __init__(self, duration, pitch, octave = 1, accidental = 'natural'):
        """ (float, str, int, float) -> Note
        Creates a new Note object with the given duration, pitch, octave and accidental.
        
        >>> note = Note(0.5, "C", 2, "natural")
        >>> note.pitch
        'C'
        
        >>> note = Note(0.5, "C", 2, "Flat")
        Traceback (most recent call last):
            raise AssertionError("Invalid accidental input.")
            AssertionError: Invalid accidental input.
            
        >>> note = Note(0.5, "C", 8, "flat")
        Traceback (most recent call last):
            raise AssertionError("Invalid octave.")
            AssertionError: Invalid octave.
        """
        
        if type(duration) != float or duration <= 0:
            raise AssertionError("Invalid duration")
        
        if type(pitch) != str or not pitch.isupper() or pitch not in PITCH:
            raise AssertionError("Invalid pitch.")
        
        if type(octave) != int or octave not in range(1,8):
            raise AssertionError("Invalid octave.")
        
        if type(accidental) != str or accidental.isupper() or accidental not in ACCIDENTAL:
            raise AssertionError("Invalid accidental input.")
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        
    def __str__(self):
        """ () -> str
        Returns a string format 'DURATION PITCH OCTAVE ACCIDENTAL'.
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        
        >>> note = Note(1.0, "C", 6, "sharp")
        >>> print(note)
        1.0 C 6 sharp
        
        >>> note = Note(1.0, "R")
        >>> print(note)
        1.0 R 1 natural
        """
        list_note = []
        list_note.append(str(self.duration))
        list_note.append(self.pitch)
        list_note.append(str(self.octave))
        list_note.append(self.accidental)
        note = " ".join(list_note)
        return note
    
    def play(self, player):
        """ (player obj) -> NoneType
        Takes a player object as input and pass the note string and duration to
        the play_note method.
        """
        if self.pitch == 'R':
            note_string = 'pause'
        else:
            if self.accidental == 'natural':
                note_string = self.pitch+str(self.octave)
            elif self.accidental == 'sharp':
                note_string = self.pitch+str(self.octave)+'#'
            else:
                note_string = self.pitch+str(self.octave)+'b'
        player.play_note(note_string, self.duration)

        
        
        
        
        
