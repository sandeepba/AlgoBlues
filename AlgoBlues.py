#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import re
from pymarkovchain import MarkovChain

class Melody:
	def __init__(self,markov_dict):
		self.markov_dict = markov_dict
		self.lily_string = ""
	
	def addMeasures(self,num_m,key_m):
		new_measures = ""
		long_enough = False
		
		#generate a string that is long enough 
		while long_enough == False:
			new_measures += self.markov_dict[key_m].generateString()+' '
			if lily_length(new_measures) >= float(num_m):
				long_enough = True
			
		#trim it down to the right size
		while lily_length(new_measures)>2:
			new_measures = new_measures.split()
			new_measures.pop()
			new_measures = ' '.join(new_measures)
		
		#add it to the master record	
		self.lily_string += new_measures
		print self.lily_string
		print lily_length(self.lily_string)

def lily_length(lily_notes):
	note_lengths = []
	for note in lily_notes.split():
		note_lengths.append(float(re.sub("\D", "", note)))	
	return sum([1/x for x in note_lengths])
	
def write_to_file(instrumentNotes,fileName):
	print instrumentNotes['piano']
	subprocess.call('cp template1.ly '+fileName,shell=True)
	subprocess.call(
	'sed -i "s/SaxNotes/'+instrumentNotes['sax']+'/g" '+fileName,
	shell=True)
	subprocess.call(
	'sed -i "s@PianoNotes@'+instrumentNotes['piano']+'@g" '+fileName,
	shell=True)
	subprocess.call('lilypond '+fileName,shell=True)

def init_markov():
	Key1 = MarkovChain("./markov1")
	Key1.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	Key2 = MarkovChain("./markov2")
	Key2.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	Key3 = MarkovChain("./markov3")
	Key3.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	Key4 = MarkovChain("./markov4")
	Key4.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	return {'I':Key1,'II':Key2,'III':Key3,'IV':Key4}
			
	
def main():
	markov_dict = init_markov()
	blues_melody = Melody(markov_dict)		
	blues_melody.addMeasures(2,'I')

main()
