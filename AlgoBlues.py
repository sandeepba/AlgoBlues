#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from pymarkovchain import MarkovChain

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
	print markov_dict['I'].generateString()
	print markov_dict['II'].generateString()
	print markov_dict['III'].generateString()
	print markov_dict['IV'].generateString()
		
	
main()
