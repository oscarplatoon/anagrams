exports.isCharacterMatch = function(string1, string2) {

  // For this challenge you will make a program that takes in two different strings and see if the invidual letter or number characters in a string match in both strings. For example, 'abcde2' can be rearranged to 'c2abed'.
  
  // take out all spaces for both strings, and uppercase
  let noSpaceStr1 = string1.split(' ').join('').toUpperCase()
  let noSpaceStr2 = string2.split(' ').join('').toUpperCase()
  console.log(noSpaceStr1)
  console.log(noSpaceStr2)

  // return false if str2.length is longer than str1.length
  if (noSpaceStr2.length > noSpaceStr1.length) {
    return false
  }

  //loop through string 1 and use the .includes()

  for (let i = 0; i < noSpaceStr1.length; i++) { 
   
    if (!noSpaceStr1.includes(noSpaceStr2[i])) return false
    
  }// return true if passes all the .includes
  return true
};


// console.log(this.isCharacterMatch('this is string 1', 'this is string 1'))
// console.log(this.isCharacterMatch('zach', 'attack'))
// console.log(this.isCharacterMatch('Anna Madrigal', 'A man and a girl'))