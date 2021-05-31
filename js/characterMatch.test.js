const { expect, test } = require("@jest/globals")

const ana = require("./characterMatch")

test('Returns a boolean: ', () => {
  expect(typeof(ana.isCharacterMatch("test", "tast")))
  .toBe("boolean")
})

test('charm / march anagram: ', () => {
  expect(ana.isCharacterMatch("charm", "march"))
  .toBe(true)
})

test('zach / attack not an anagram: ', () => {
  expect(ana.isCharacterMatch("zach", "attack"))
  .toBe(false)
})

test('Confirm anagram check is case insensitive: ', () => {
  expect(ana.isCharacterMatch("CharM", "mARch"))
  .toBe(true)
})



test(" `Anna Madrigal` and `A man and a girl` are anagrams: ", () => {
  expect(ana.isCharacterMatch("Anna Madrigal", "A man and a girl"))
  .toBe(true)
})