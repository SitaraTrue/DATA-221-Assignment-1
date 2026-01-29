# Pandas DataFrame with Computed Column

import pandas as pd

data = {
    "A": [1,2,2,1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Converting data in dictionary form to tabular
data_frame = pd.DataFrame.from_dict(data)

# Adding new column derived from columns A and B
data_frame = data_frame.assign(AB = [3.1, 8.4, 3.0, 6.3])
print(data_frame)