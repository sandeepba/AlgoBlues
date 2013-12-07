\score {
  \new Staff <<
    \new Voice {
      \set midiInstrument = #"Electric Grand Piano"
      \voiceOne
      \time 4/4
      PianoMelody
       
    }
  \new Staff 
    \new Voice {
      \set midiInstrument = #"Electric Grand Piano"
      \voiceTwo
      \new Chordnames {
      <bes d f aes>\longa
      <ees g bes des>\breve
      <bes d f aes>\breve
      <c ees g bes>1
      <f a c ees>1
      <bes d f aes>\breve
      <bes d f aes>\longa
      <ees g bes des>\breve
      <bes d f aes>\breve
      <c ees g bes>1
      <f a c ees>1
      <bes d f aes>\breve
      }
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
      tempoWholesPerMinute = #(ly:make-moment 120 4)
    }
  }
}
