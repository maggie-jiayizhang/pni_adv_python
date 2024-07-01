# Information about the dataset
- This dataset is extracted from the data published in Daie et al. 2021 (*Nat Neuro*). In the original study, the researchers recorded neurons from mouse left anterolateral motor cortex (ALM) while the animals were executing a delayed decision-making task.
- The extracted dataset contains both neural recordings and animal choice for a number of trials. For a mouse `x`, all data are stored in the `data` directory, with format string `recording_{x}.npy`
- For each mouse, 4 data matrices are stored in its `recording_{x}.npy` file:
  - "L", "R" : each contains neural recordings of mouse `x` on *left* or *right* trials. Both are of dimension: n_time_points x n_neurons x n_trials.
  - "CL", "CR": each contains a boolean value of whether the animal's choice was correct on a given *left* or *right* trial. Both are of dimensions: n_trials x 1.
- In addition, `recording_{x}.npy` stores the timing of the audio stimulus and go cue (under "go_cue" and "stim").
