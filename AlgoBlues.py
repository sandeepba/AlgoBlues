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
	Key1 = MarkovChain("./markov")
	Key1.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	Key2 = MarkovChain("./markov")
	Key2.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	Key3 = MarkovChain("./markov")
	Key3.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	Key4 = MarkovChain("./markov")
	Key4.generateDatabase("g4 des8 c4. g8 bes8 r8 bes4. "+\
	"g4 des8 c4. g8 bes8 r8 bes4. r2 r8 f8 fis8 g4")
	
	return {'I':Key1,'II':Key2,'III':Key3,'IV':Key4}
	 
def improv_section(section_key):
	mcSax = MarkovChain("./markov")	
	mcSax.generateDatabase(
	"g4 des8 c4. g8 bes8 r8 bes4. r2 g4 des8 c4. g8 bes8 r2 r8 f8 fis8 g4 bes8 c8 b8 des8 c8 bes8 g c8 bes4. r2 r8 g8 c8 c8 d8 d8 ees4 e8 f4 f8 fis8 fis8 g4 a8 bes8"
	)
	write_to_file({'piano':'r1',
				   'sax':mcSax.generateString()+mcSax.generateString()
				   +mcSax.generateString()+mcSax.generateString()
				   +mcSax.generateString()+mcSax.generateString()},
				   'test7.ly')
	
def main():
	init_markov()
	
		
	
main()
