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
		while lily_length(new_measures)> num_m:
			new_measures = new_measures.split()
			new_measures.pop()
			new_measures = ' '.join(new_measures)
			
		#use rests to make up the difference
		if lily_length(new_measures) < num_m:
			beat_short = num_m - lily_length(new_measures)
			print beat_short
			correction = ' r' + str(int(1/beat_short))
			print correction
			new_measures += correction
		
		print ([new_measures,lily_length(new_measures)])
		
		#allow for continued concatenation
		new_measures += '-end '
		
		#add it to the master record	
		self.lily_string += new_measures
		
	def outputFile(self,fileName):
		subprocess.call('cp template1.ly '+fileName+'.ly',shell=True)
		subprocess.call('sed -i "s/PianoMelody/'+self.lily_string+\
		'/g" '+fileName+'.ly', shell=True)
		subprocess.call('lilypond '+fileName+'.ly',shell=True)
		subprocess.call('timidity '+fileName+'.midi',shell=True)


def lily_length(lily_notes):
	note_lengths = []
	print lily_notes
	for note in lily_notes.split():
		print note
		note_lengths.append(float(re.sub("\D", "", note)))	
	return sum([1/x for x in note_lengths])

def init_markov():
	Key1_intro = MarkovChain("./markov1intro")
	Key1_intro.generateDatabase("g''4 des''8 c''4 g'8 bes'8 r4 bes'4. "+\
      "g''4 des''8 c''4 g'8 bes'8 r8 f'8 fis'8 g'8 ")
	
	Key1 = MarkovChain("./markov1")
	Key1.generateDatabase("f'4 bes'8 c''8 bes'8 g''8 des''8 "+\
	"g'8 bes'4. r4 r8 g'8 r1 aes'8 f'8 bes'8 aes'8 des''8 bes'8 "+\
	"ees''8 e''8 ees''8 des''8 bes'8 aes'8 f'8 des''4. bes4 des'''4."+\
	 "bes''4 r4 g''4 des''8 c''4 g'8 bes'8 r4 bes'4.")
	
	Key1_finisher = MarkovChain("./markov1finisher")
	Key1_finisher.generateDatabase("r8 e'''8 ees'''8 des'''8 bes''8 "+\
	"aes''8 f''8 e''8 ees''8 des''8 bes'8 aes'8 des''8 bes'8 "+\
	"aes'8 bes'8 ")
	
	Key2 = MarkovChain("./markov2")
	Key2.generateDatabase(" c''8 c''8 des''8 des''8 ees''4 e''8 f''8")
	
	Key4 = MarkovChain("./markov4")
	Key4.generateDatabase("g'8 bes'8 c''8 bes'8 des''8 c''8 bes'8 "+\
	"g'8 c''8 bes'4. r8 ")
	
	Key5 = MarkovChain("./markov5")
	Key5.generateDatabase("f''4 f''8 fis''8 fis''8 g''4 a''8 bes''8 r8 ")
	
	return {'I-intro':Key1_intro,'I':Key1,'II':Key2,'IV':Key4,'V':Key5,
	'I-finisher':Key1_finisher}
			
	
def main():
	markov_dict = init_markov()
	blues_melody = Melody(markov_dict)		
	blues_melody.addMeasures(4,'I-intro')
	blues_melody.addMeasures(2,'IV')
	blues_melody.addMeasures(2,'I')
	blues_melody.addMeasures(1,'II')
	blues_melody.addMeasures(1,'V')
	blues_melody.addMeasures(2,'I-finisher')
	blues_melody.addMeasures(4,'I')
	blues_melody.outputFile('test2')

main()
