import musicalbeeps
from note import Note

class Melody:
    """ A class that store information about a melody.
    
    Attributes: title(str), author(str), notes(list<Note>)
    """
    def __init__(self, filename):
        """ (str) -> Melody
        Creates a new Melody object with the given title, author and notes.
        
        >>> melody = Melody("birthday.txt")
        >>> melody.title
        'Happy Birthday'
        
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> len(hotcrossbuns.notes)
        17
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.author
        'Nikolay Nekrasov, Hirokazu Tanaka'
        """
        if type(filename) != str:
            raise AssertionError("Filename must be of class str.")
        
        fobj = open(filename, 'r')
        melody = fobj.read()
        list_melody = melody.split("\n")
        self.title = list_melody[0]
        self.author = list_melody[1]
        sequences = []
        for element in list_melody[2:]:
            list_element = element.split(" ")
            sequences.append(list_element)
            
        notes = []
        repeated_notes = []
        reps = 0
        i = 0
        for i in range(len(sequences)):
            if 'R' in sequences[i]:
                sequences[i].insert(2, '1')
                sequences[i].insert(3, 'natural')
                note = Note(float(sequences[i][0]), str(sequences[i][1]),\
                int(sequences[i][2]), str(sequences[i][3]))
            if 'R' not in sequences[i]:
                note = Note(float(sequences[i][0]), str(sequences[i][1]),\
                int(sequences[i][2]), str(sequences[i][3].lower()))
            
            if sequences[i][4] == 'true' and reps == 0:
                repeated_notes.append(note)
                reps += 1
            elif sequences[i][4] == 'false' and reps == 1:
                repeated_notes.append(note)
            elif sequences[i][4] == 'true' and reps == 1:
                repeated_notes.append(note)
                
                for w in range(len(repeated_notes)):
                    repeated_note = repeated_notes[w]
                    repeated_note = Note(repeated_note.duration, repeated_note.pitch, \
                    repeated_note.octave, repeated_note.accidental)
                    repeated_notes.append(repeated_note)
                
                for n in repeated_notes:
                    notes.append(n)
                
                repeated_notes = []
                reps = 0
            else:
                notes.append(note)
        reps += 1
        self.notes = notes
        fobj.close()
                
                          
    def play(self, player):
        """ (player obj) -> Nonetype
        Takes a player object as an input and calls the play method on each Note
        object of the notes instance attribute.
        """
        for i in self.notes:
            i.play(player)
                
    def get_total_duration(self):
        """ () -> float
        Returns total duration of the song as a float.
        
        >>> melody = Melody("birthday.txt")
        >>> melody.get_total_duration()
        13.0
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.get_total_duration() 
        25.799999999999944
        
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.get_total_duration()
        8.0
        """
        total_duration = 0.0
        for i in self.notes:
            total_duration += i.duration
        return total_duration
    
    #Helper function
    def octave_min_max(self, octave):
        """ (int) -> bool
        Returns True if octaves in notes are the minimum or maximum octave.
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.octave_min_max(1)
        False
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.octave_min_max(7)
        False
        
        >>> birthday = Melody("birthday.txt")
        >>> birthday.octave_min_max(7)
        False
        """
        for i in self.notes:
            if type(octave) != int and (octave <= 1 or octave >= 7): 
                raise AssertionError("Invalid octave.")
            elif i.pitch == 'R':
                continue
            elif i.octave == octave:
                return True
        return False
                
    def lower_octave(self):
        """ () -> bool
        Returns True and every pitch in the melody lowered by 1. Returns False if
        pitch in melody is 1.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.lower_octave()
        True
        >>> tetris.notes[10].octave
        4
        
        >>> weasel = Melody("weasel.txt")
        >>> weasel.lower_octave()
        True
        >>> weasel.notes[3].octave
        3
        """
        for i in self.notes:
            if self.octave_min_max(1):
                return False
            elif i.pitch == 'R':
                continue
            else:
                i.octave -= 1
        return True
    
    def upper_octave(self):
        """ () -> bool
        Returns True and every pitch in the melody increased by 1. Returns False if
        pitch in melody is 1 or 7.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.upper_octave()
        True
        >>> tetris.notes[10].octave
        6
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.upper_octave()
        True
        >>> fur_elise.notes[10].octave 
        4
        """
        for i in self.notes:
            if self.octave_min_max(7):
                return False
            else:
                i.octave += 1
        return True
    
    def change_tempo(self, tempo):
        """ (float) -> NoneType
        Takes on positive float as input and returns nothing.
        
        >>> melody = Melody("birthday.txt")
        >>> melody.change_tempo(0.5)
        >>> melody.get_total_duration()
        6.5
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.change_tempo(0.5)
        >>> fur_elise.get_total_duration() 
        12.9
        
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.change_tempo(1)
        Traceback (most recent call last):
        AssertionError: Invalid tempo input.
        """
        if type(tempo) != float or tempo <= 0:
            raise AssertionError("Invalid tempo input.")
        else:
            for i in self.notes:
                i.duration*=tempo
