def solution(area):
  areas = []
  while area:
    areas.append(int(area**0.5)**2)
    area -= areas[-1]
  return areas
