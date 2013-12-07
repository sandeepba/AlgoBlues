\score {
  \new Staff <<
    \new Voice \relative c'' {
      \set midiInstrument = #"tenor sax"
      \voiceOne
      \key g \major
      \time 4/4
      r1-"Saxophone" 
      SaxNotes
    }
  \new Staff 
    \new Voice \relative c'' {
      \set midiInstrument = #"Electric Grand Piano"
      \voiceTwo
      r1-"Electric Grand Piano" 
      PianoNotes
    }
  >>
  \layout { }
  \midi {
    \context {
      \Staff
      \remove "Staff_performer"
    }
    \context {
      \Voice
      \consists "Staff_performer"      
    }
    \context {
      \Score
      tempoWholesPerMinute = #(ly:make-moment 72 2)
    }
  }
}
