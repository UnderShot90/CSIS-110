#Author:#Ryan Frates
#Class:CSIS 110
#Due Date:Feb 18, 2023
#Purpose:to play heart and soul
#heres is the link to the actual song: https://musescore.com/guestinpiano/heart_and_soul_easy
from music import *
myScore = Score("Heart and Soul", 110)

piano1Part = Part(PIANO, 0)
piano2Part = Part(PIANO, 1)
trumpetPart = Part(TRUMPET, 2)
piano3Part = Part(PIANO, 3)
piano4Part = Part(PIANO, 4)
piano5Part = Part(PIANO, 5)
piano6Part = Part(PIANO, 6)

piano1Phrase = Phrase()
pitches1 =   [C4,C4,C4,REST,C4,B3,A3,B3,C4,D4]
durations1 = [QN,QN,HN,EN  ,EN,EN,EN,EN,EN,QN]
pitches2 =   [E4,E4,E4,REST,E4,D4,C4,D4,E4,F4]
durations2 = [QN,QN,HN,EN  ,EN,EN,EN,EN,EN,QN]
pitches3 =   [G4,C4,REST,A4,G4,F4,E4,D4,C4,REST]
durations3 = [HN,HN,EN  ,EN,EN,EN,QN,QN,QN,EN]
pitches4 =   [B3,A3,REST,G3,F3,REST,G3,A3,B3]
durations4 = [EN,QN,EN,  EN,QN,EN  ,EN,QN,QN]



piano1Phrase.addNoteList(pitches1, durations1)
piano1Phrase.addNoteList(pitches2, durations2)
piano1Phrase.addNoteList(pitches3, durations3)
piano1Phrase.addNoteList(pitches4, durations4)

Mod.repeat(piano1Phrase,4)
piano1Part.addPhrase(piano1Phrase)
   

pitches1 =   [C3,A2,F2,G2]
durations1 = [HN,HN,HN,HN]
piano2Phrase = Phrase()
piano2Phrase.addNoteList(pitches1, durations1)

Mod.repeat(piano2Phrase,8)
piano2Part.addPhrase(piano2Phrase)




pitches1 =   [REST,C4,D4,A3,REST,C4,B3,A3,B3,C4,D4]
durations1 = [EN,EN,EN,EN, HN+EN,    EN,EN,EN,EN,EN,EN]
pitches2 =   [REST,E4,E4,E4,REST,E4,D4,C4,D4,E4,F4]
durations2 = [EN,QN,QN,HN,EN  ,EN,EN,EN,EN,EN,QN]
pitches3 =   [G4,C4,REST,A4,G4,F4,E4,D4,C4,REST]
durations3 = [HN,HN,EN  ,EN,EN,EN,QN,QN,QN,EN]
pitches4 =   [B3,A3,REST,G3,F3,REST,G3,A3,B3]
durations4 = [EN,QN,EN,  EN,QN,EN  ,EN,QN,QN]
trumpetPhrase = Phrase()
trumpetPhrase.addNoteList(pitches1,durations1)
trumpetPhrase.addNoteList(pitches2, durations2)
trumpetPhrase.addNoteList(pitches3, durations3)
trumpetPhrase.addNoteList(pitches4, durations4)
trumpetPart.addPhrase(trumpetPhrase)





pitches1 =   [C3,[E3,G3],A2,[E3,C3],F2,[A2,C3],G2,[B2,D3] ]
durations1 = [QN,QN,     QN,QN,     QN,QN,     QN,QN]

piano3Phrase = Phrase ()
piano3Phrase.addNoteList(pitches1, durations1)
piano3Phrase.setStartTime(64.0) 
Mod.repeat(piano3Phrase,8)
piano3Part.addPhrase(piano3Phrase)


pitches1 =   [[C5,C4],[C5,C4],[C5,C4],REST,[C5,C4],[B4,B3],[A4,A3],[B4,B3],[C5,C4],[D5,D4]]
durations1 = [QN,      QN,    HN,     EN, EN,       EN,     EN,     EN,     EN,    QN]
pitches2 =   [[E5,E4],[E5,E4],[E5,E4],REST,[E5,E4],[D5,D4],[C5,C4],[D5,D4],[E5,E4],[F5,F4]]
durations2 = [QN,      QN,    HN,     EN, EN,       EN,     EN,     EN,     EN,    QN]
pitches3 =   [[G5,G4],[C5,C4],REST,[A5,A4],[G5,G4],[F5,F4],[E5,E4],[D5,D4],[C5,C4],REST,[B4,B3],[A4,A3],REST,[G4,G3],[F4,F3],REST,E4,D4]
durations3 = [HN,      HN,    EN,   EN,    EN,      EN,     QN,     QN,     QN,    EN,  EN,      QN    ,EN,   EN,     QN,    QN,  QN,QN]
piano4Phrase = Phrase ()
piano4Phrase.addNoteList(pitches1, durations1)
piano4Phrase.addNoteList(pitches2, durations2)
piano4Phrase.addNoteList(pitches3, durations3)

piano4Phrase.setStartTime(128.0) 
piano4Part.addPhrase(piano4Phrase)

pitches1 =   [C3,[E3,G3],[E3,G3],A2,[E3,C3],[E3,G3],F2,[A2,C3],[A2,C3],G2,[B2,D3],[B2,D3]]
durations1 = [QN,EN,     EN,     QN, EN,     EN,   QN, EN,      EN,    QN, EN,    EN]

piano5Phrase = Phrase ()
piano5Phrase.addNoteList(pitches1, durations1)
piano5Phrase.setStartTime(128.0) 
Mod.repeat(piano5Phrase,4)
piano5Part.addPhrase(piano5Phrase)



myScore.addPart(trumpetPart)
myScore.addPart(piano1Part)
myScore.addPart(piano2Part)
myScore.addPart(piano3Part)
myScore.addPart(piano4Part)
myScore.addPart(piano5Part)

Play.midi(myScore)
#View.notation(myScore) 
#the program didn't like all of the inputs I was giving it and now veiw.notation no longer works
#But it probably wasnt going to help anyways it was a giant mess it also cause a ton of processsing error even more than there already is
