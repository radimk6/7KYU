# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

# test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
# test.assert_equals(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"])
# test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])

def friend(x):
  friends_name = []
  for name in x:
    if len(name) == 4:
      friends_name.append(name)
  return friends_name


print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))