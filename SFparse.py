import pandas as pd

# Calculates average slope from .dat file
def parse_datafile(filename):
  print("-"*20 + filename + "-"*20)
  df = pd.read_csv(filename, comment='#', delim_whitespace=True, header=None)

  peak = df[4].idxmax()

  print("Peak velocity idx=%i val=%f" % (peak, df[4][peak]))

  # Calculates slope from dataframe
  def get_slope(df):
    df = df.reset_index()

    x = df[0][-1:]-df[0][0]
    y = df[4][-1:]-df[4][0]

    Delta_x = df[1][-1:]+df[1][0]
    Delta_y = df[5][-1:]+df[5][0]

    h = y/x

    Delta_h = h*(abs(Delta_x/x) + abs(Delta_y/y))

    return (float(h), float(Delta_h))

  h1, Delta_h1 = get_slope(df[:peak+1])
  h2, Delta_h2 = get_slope(df[peak:])

  print("Positive slope\t h1=%f\t Delta h1=%f" % (h1, Delta_h1))
  print("Negative slope\t h2=%f\t Delta h2=%f" % (h2, Delta_h2))

  h = (abs(h1)+abs(h2))/2
  Delta_h = (abs(Delta_h1)+abs(Delta_h2))/2

  print("Average slope\t h2=%f\t Delta h2=%f\n" % (h, Delta_h))

  return (h, Delta_h)


files = ['unnid1.dat', 'unnid2.dat', 'unnid3.dat', 'unnid4.dat']

for f in files:
  parse_datafile(f)
