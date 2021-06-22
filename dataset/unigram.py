def unigram(tokens):
  model = collections.defaultdict(lambda: 0.01)
  for f in tokens:
    try:
      model[f] += 1
    except KeyError:
      model [f] = 1
      continue
  N = float(sum(model.values()))
  for word in model:
    model[word] = model[word]/N
  return model

#computes perplexity of the unigram model on a testset  
def perplexity(testset, model):
  testset = testset.split()
  perplexity = 1
  N = 0
  for word in testset:
      N += 1
      perplexity = perplexity * (1/model[word])
  perplexity = pow(perplexity, 1/float(N)) 
  return perplexity