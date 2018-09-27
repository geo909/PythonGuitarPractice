#!/bin/python2
"""
Input example:
python2 thisprogram.py 2 2 4 2 2
Each number declares how many of the corresponding exercises are produced

If there is no input, then there is a helpful prompt.
"""
# Set those for Aebersold's patterns
Maj251Patterns=range(1,9)
Min251Patterns=range(1,9)

import sys
import os
from collections import OrderedDict
from Generate_guitar_exercises_definitions import *

# Dictionary as follows:
#   { Function name : [description,number of exercises],
#     ...
#   }
# In other words, for x in  the exercises
# - x is the function 
# - Exercise[x][0] is the description
# - Exercise[x][1] is the number of exercises 

Exercises=OrderedDict([   
    (BilliesBounce,["Billie's bounce",0]),
    (IIVIVI_improvlines,["2-5-1-6 Improv lines",0]),
    (ScalePracticeTechniques,["Scale practice technique",0]),
    (IIVILineExample,["2-5-1 Line examples",0]),
    (ApproachBluesInF,["Approach: Blues in F",0]),
#    (Scale,["Scales",0]),
#    (Triad,["Triads",0]),
#    (Moving_treble,["Moving trebles",0]),
#    (Diatonic_chords_within_a_CAGED_form,["Diatonic chords",0]),
    (II_V_I_Aebersold_patterns,["Aebersold II-V-I patterns",0]),
#    (Sight_reading_studies,["Sight-reading (Leavitt)",0]),
#    (Technique_patterns,["Technique: patterns",0]),
#    (Technique_right_hand_fingers,["Technique: right hand fingers",0]),
#    (Technique_right_hand_picking,["Technique: right hand picking",0])
]) 

# Input prompt
Input_prompt=""
for e in Exercises:
    Input_prompt+= '%d. %s\n' % (Exercises.keys().index(e)+1,Exercises[e][0])
Input_prompt+="    --- Press <C-c> to exit, or enter numbers of exercises separated by spaces.\n\n"

# Set some variables according to whether we are doing latex or not
TexMode=False
ExtraArgs=1 # Number of input strings other than exercise numbers
if len(sys.argv) > 1:
    if sys.argv[1] in ["-t","--tex-mode"]:
       TexMode=True
       ExtraArgs=2
       AebDict=dict()
       MyTitle = raw_input("Enter title (press return for \"Guitar exercises\"): ")

# Setting how many times we do each exercise
if len(sys.argv)==len(Exercises)+ExtraArgs:     # User gave arguments correctly
    TimesEachExercise=[int(i) for i in sys.argv[ExtraArgs:]]
else: # No user input or input not given correctly
    InputNums = raw_input(Input_prompt)
    TimesEachExercise = [int(i) for i in InputNums.split() if i.isdigit()] 
    while len(TimesEachExercise) != len(Exercises):
        print "\nSomething was wrong, try again: "
        InputNums = raw_input()
        TimesEachExercise = [int(i) for i in InputNums.split() if i.isdigit()] 
for e in Exercises:
    i=Exercises.keys().index(e)
    Exercises[e][1]=TimesEachExercise[i]

List_of_exercises=[]
for e in Exercises:
    # The following is a special case, since we need the scans
    if e.__name__=='II_V_I_Aebersold_patterns':
        for i in range(Exercises[e][1]):
            AebOutput=e(Maj251Patterns,Min251Patterns)
            AebExercise=AebOutput[0]
            AebPatternLabel=AebOutput[1]
            if TexMode:
                AebDict[AebPatternLabel]=AebDict.get(AebPatternLabel,0)+1
                s = '\t\item %s \label{%s-%d}\\dotfill$\square$\n' % (AebExercise,AebPatternLabel,AebDict[AebPatternLabel])
            else:
                s = AebOutput[0]
            List_of_exercises.append(s)
    # If you have any other special exercises, elif them here
    # Continuing with radom regular exercises
    else:
        for i in range(Exercises[e][1]):
            if TexMode:
                s = '\t\item %s\\dotfill$\square$\n' % (e())
            else:
                s = e()
            List_of_exercises.append(s)

random.shuffle(List_of_exercises)

if TexMode:
    # Overview of exercises
    IncludedExercises="\\section*{Overview}\n\\begin{itemize}\n"
    for e in Exercises:
        if Exercises[e][1]>0:
            IncludedExercises+='\item %s: %d\n' % (Exercises[e][0],Exercises[e][1])
    IncludedExercises+="\\end{itemize}"

    # Take care of the figures, if any
    IIVIFiguresParagraph= ""
    if Exercises[II_V_I_Aebersold_patterns][1]>0: # There exist Aebersold 251 exercises
        Items_for_251_figures=[]
        for pattern in AebDict:
            s="\\item Used in \\cref{"
            for i in range(AebDict[pattern]-1):
                s+='%s-%d,' % (pattern,i+1)
            s+= '%s-%d}' % (pattern,AebDict[pattern])
            s+= "\n\\newline\\newline\n"
            s+= '\\includegraphics[width=0.8\\linewidth]{scans251/%s.png}' % (pattern)
            Items_for_251_figures.append(s)

        IIVIFiguresParagraph= "\n\\section*{II-V-I patterns}\n"
        IIVIFiguresParagraph+= "\\begin{itemize}\n" 
        for i in Items_for_251_figures:
            IIVIFiguresParagraph+=i
        IIVIFiguresParagraph+= "\n\\end{itemize}\n" 

    TexOutput=""
    TexOutput+="\documentclass[letterpaper]{article}\n"
    TexOutput+="\usepackage[top=1in, left=1.2in, right=1.2in, bottom=1.5in]{geometry}\n"
    TexOutput+="\usepackage{amssymb,graphicx,enumitem,cleveref}\n"
    TexOutput+="\crefname{enumi}{exercise}{exercises}\n"
    if MyTitle:
        TexOutput+='\\title{%s}\n\date{\\vspace{-3em}\\today}\n' % (MyTitle)
    else:
        TexOutput+="\\title{Guitar exercises}\n\date{\\vspace{-3em}\\today}\n"
    TexOutput+="\n\\author{}\n"
    TexOutput+="\\begin{document}\n"
    TexOutput+="\\maketitle\n"
    TexOutput+=IncludedExercises
    TexOutput+="\n\\section*{Exercises}"
    TexOutput+="\\begin{enumerate}\n"
    for e in List_of_exercises:
        x=e.replace("flat","$\\flat$")
        x=x.replace("#","$\\sharp$")
        TexOutput+=x
    TexOutput+="\\end{enumerate}\n"
    
    TexOutput+=IIVIFiguresParagraph
    TexOutput+="\n\\end{document}\n"

    f = open("Tex/GuitarExercises.tex", "w")
    f.write(TexOutput)
    f.close()

    for i in range(3):
        os.system("sh -c 'cd Tex && pdflatex -interaction=nonstopmode GuitarExercises.tex'")
    os.system("sh -c 'cd Tex && zathura GuitarExercises.pdf &'")


else:
    for e in List_of_exercises:
        print e.replace("flat","b")


