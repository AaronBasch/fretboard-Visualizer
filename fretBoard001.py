notes = ['A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
fretBoard = {}
standardTuning = ['E', 'A', 'D', 'G', 'B', 'E']
dadfbe = ['D', 'A', 'D', 'F#', 'B', 'E']
major = [0,4,7]
minor = [0,3,7]
major7 = [0,4,7,11]
minor7 = [0,3,7,10]
major9 = [0,4,7,11,14]
minor9 = [0,3,7,10,14]

def listNotes(startNote, chord):
    chordNotes = []
    for note in notes:
        if note == startNote.upper():
            noteIndex = notes.index(note)
            break
    for i in chord:
        chordNotes.append(notes[noteIndex + i])
    return chordNotes

def fretBoardTuner(stringList):
    for s in range(1,7):
        for note in notes:
            if note == stringList[s-1]:
                noteIndex = notes.index(note)
                fretBoard[s] = notes[noteIndex:noteIndex+12]

fretBoardTuner(dadfbe)

def fretBoardVisualizer(startNote, chord, startString, fret, stringAmount):
    fretBoardVisual = []
    for i in range(6):
        fretBoardVisual.append([])
        for f in range(12):
            fretBoardVisual[i].append('-')
            
    
    
    for s in range(stringAmount):
        for r in range(4):
            try:
                if fretBoard[s+1+startString][fret+r] in listNotes(startNote, chord):
                    fretBoardVisual[s+startString][fret+r-1] = fretBoard[s+1+startString][fret+r]
                    break
            except:
                break

    print(fretBoardVisual[0])
    print(fretBoardVisual[1])
    print(fretBoardVisual[2])
    print(fretBoardVisual[3])
    print(fretBoardVisual[4])
    print(fretBoardVisual[5])    
        
fretBoardVisualizer('A', major, 0, 3, 6)
