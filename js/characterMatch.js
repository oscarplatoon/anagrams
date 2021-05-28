
function isCharacterMatch(string1, string2) {
  if ((Array.from(string1.toLowerCase().replace(/\s/g, '')).sort()) == ((Array.from(string2.toLowerCase().replace(/\s/g, '')).sort()))); {
    return true
  }
  return false
}

isCharacterMatch('CH Haa  TT', 'tchataht')

