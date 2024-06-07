# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
  vowels = "aeiou"
  vowel_count = 0
  for x in sentence:
    if x in vowels:
      vowel_count += 1
  return vowel_count

print(get_count("abrakadabra"))