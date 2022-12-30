def minimumWaitingTime2(queries):
  queries.sort(reverse=True)  # or any sorting algo
  return sum(i * n for i, n in enumerate(queries))
