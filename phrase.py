def part(word,phrase):
  w = len(word)
  count = 0
  for i in range (len(phrase)):
    if phrase[i:(i + w)] == word:
      count +=1
  print(count)
part("ro","toto to totoro")