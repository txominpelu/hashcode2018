
rows, columns, vehicles, num_rides, bonus, steps = [int(s) for s in input().split(" ")]
rides = []
for i in range(0, num_rides):
  start_x, start_y, end_x, end_y, early_start, latest_end = [int(s) for s in input().split(" ")]
  rides.append({
      'start': [start_x, start_y],
      'end': [end_x, end_y],
      'early_start': early_start,
      'latest_end': latest_end
  })
  
