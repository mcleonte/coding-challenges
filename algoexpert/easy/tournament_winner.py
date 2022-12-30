# O(n) O(n)
def tournamentWinner(competitions, results):
  totals = {}
  for c, r in zip(competitions, results):
    w = c[1 - r]
    try:
      totals[w] += 3
    except KeyError:
      totals[w] = 3
  winner, score = "", 0
  for k, v in totals.items():
    if v > score:
      score = v
      winner = k
  return winner
