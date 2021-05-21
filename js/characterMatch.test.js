const isCharacterMatch = require('./characterMatch');

test('returns a bool', () => {
  expect(typeof isCharacterMatch('a', 'b')).toBe("boolean");
})

test('works for all lowercase', () => {
  expect(isCharacterMatch('charm', 'march')).toBe(true);
})

test('correctly fails', () => {
  expect(isCharacterMatch('zach', 'attack')).toBe(false);
})

test('works with capital letters', () => {
  expect(isCharacterMatch('CharM', 'mARcH')).toBe(true);
})

test('works with numbers', () => {
  expect(isCharacterMatch('abcde2', 'c2abed')).toBe(true);
})