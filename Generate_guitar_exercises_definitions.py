import random
from random import randint

Forms=['C','A','G','E','D']
Keys= ['A', 'Aflat', 'B', 'Bflat', 'C', 'D', 'Dflat', 'E', 'Eflat', 'F', 'F#', 'G', 'Gflat','C#','Cb']
FullKeys= ['A', 'A#', 'Aflat', 'B', 'B#', 'Bflat', 'C', 'C#', 'Cflat', 'D', 'D#', 'Dflat', 'E', 'E#', 'Eflat', 'F', 'F#', 'Fflat', 'G', 'G#', 'Gflat']
FourNoteChordsQualities=['maj7','7','m7','m7flat5']
TriadQualities=['','m','dim','aug']
Asc_OR_Desc=["ascending","descending"]
MaybeTwelveFret=[".",", above the 12th fret."]
TriadWays=(['fifth',1],['third',2],['root',3],['fifth',4],['third',5],['root',6])
Patterns=['1234','13','123456','135','16']
MajorModes=['ionian','dorian','frygian','lydian','mixolydian','aeolian','locrian']

########## February 2017 #####
def BilliesBounce():
    what=random.choice(["Theme","Solo"])
    return 'Study Billie\'s bounce: %s' % (what)

def IIVIVI_improvlines():
    exercnum=random.choice(range(1,6))
    form=random.choice(Forms)
    return 'Play line example %d in %s form over Dm7 G7 Cmaj7 A7' % (exercnum,form)

def ScalePracticeTechniques():
    exercnum=random.choice(range(1,7))
    form=random.choice(Forms)
    return 'Practice scale technique %d in %s form' % (exercnum,form)

def IIVILineExample():
    exercnum=random.choice(range(1,6))
    return 'Study line example %d over descending II-V-I\'s' % (exercnum)

def ApproachBluesInF():
    chorus=random.choice(range(1,3))
    return 'Approach - Blues in F: focus on chorus %d' % (chorus)

########## Below: old exercises

def Technique_right_hand_picking():
    return "Play the chromatic scale for 5 minutes focusing on the picking"

def Sight_reading_studies():
    return "Do 5 minutes of sight-reading from Leavitt"

def Technique_right_hand_fingers():
    typeofrighthand=random.choice(['thumb-finger exchange', 'pima arpeggio', 'free stroke (a+p)mim'])
    return '3 minutes of right-hand: %s' % (typeofrighthand)

def Technique_patterns():
    pattern=random.choice(Patterns)
    form=random.choice(Forms+["three-note per string "+i for i in MajorModes])
    fret=random.choice(range(16))
    AorD=random.choice(Asc_OR_Desc)
    exercise='Play pattern %s using the %s form in fret %d, %s.' % (pattern,form,fret,AorD)
    return exercise
    

def Scale():
    key=random.choice(Keys)    
    mode=random.choice(MajorModes+["Melodic minor"])
    AorD=random.choice(Asc_OR_Desc)
    finger=randint(1,4)
    stringnum=randint(1,6)
    where=random.choice(MaybeTwelveFret)

    exercise='Play %s %s %s. Start with finger %d on string %d%s' % (key,mode,AorD,finger,stringnum,where)
    return exercise

def Triad():
    key=random.choice(FullKeys)    
    quality=random.choice(TriadQualities)    
    starting=random.choice(TriadWays)
    AorD=random.choice(Asc_OR_Desc)
    where=random.choice(MaybeTwelveFret)

    exercise='Play the triad for %s %s %s. Start with the %s at string %d%s' % (key,quality,AorD,starting[0],starting[1],where)
    return exercise

def Moving_treble():
    key=random.choice(Keys)    
    AorD=random.choice(Asc_OR_Desc)
    quality=random.choice(FourNoteChordsQualities)    
    otherquality=random.choice(FourNoteChordsQualities)    

    exercise='Play the moving treble for %s. Start by %s in %s and do the other way in %s.' % (key,AorD,quality,otherquality)
    return exercise

def Diatonic_chords_within_a_CAGED_form():
    key=random.choice(Keys)    
    form=random.choice(Forms)
    where=random.choice(MaybeTwelveFret)

    exercise='Play the diatonic chords for %s major within its %s form%s' % (key,form,where)
    return exercise

def II_V_I_Aebersold_patterns(MajPatterns,MinPatterns):
    key=random.choice(Keys)    
    quality=random.choice(["major", "minor"])
    if quality=="major":
        aebersoldpattern=random.choice(MinPatterns)
    else:
        aebersoldpattern=random.choice(MajPatterns)
    exercise='Play %s II-V-I pattern %d for %s across the fretboard' % (quality,aebersoldpattern,key)
    return (exercise,quality+str(aebersoldpattern))
    # second looks like maj2, min58, etc (for latex labels)
