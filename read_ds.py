
def read_ds(fname):
    with open(fname) as f:
        content = f.readlines()
    rows, columns, vehicles, num_rides, bonus, steps = [int(s) for s in content[0].split(" ")]
    rides = []
    for i in range(0, num_rides):
      start_x, start_y, end_x, end_y, early_start, latest_end = [int(s) for s in content[i+1].split(" ")]
      rides.append({
          'start': [start_x, start_y],
          'end': [end_x, end_y],
          'early_start': early_start,
          'latest_end': latest_end
      })
    return rides
