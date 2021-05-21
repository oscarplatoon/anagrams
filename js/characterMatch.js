function isCharacterMatch(string1, string2) {
  let stringArray1 = string1.split("");
  let stringArray2 = string2.split("");

  let lowerCaseArray1 = stringArray1.map(x => x.toLowerCase())
  let lowerCaseArray2 = stringArray2.map(x => x.toLowerCase())

  lowerCaseArray1.sort();
  lowerCaseArray2.sort();

  if (lowerCaseArray1.length !== lowerCaseArray2.length) {
    return false
  }

  for (i = 0; i < lowerCaseArray1.length; i++) {
    if (lowerCaseArray1[i] !== lowerCaseArray2[i]) return false;
  }

  return true;
}

isCharacterMatch('CharM', 'mARcH')

module.exports = isCharacterMatch;