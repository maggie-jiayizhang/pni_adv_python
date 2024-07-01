# Information about the dataset
The actual data file (`recording_0.npy`) can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1TOpoUXyNcO3XrBJ5ie64_v_ZoQkSaptX?usp=sharing) -- not included because it's too large for git. You can download it into your `week1/data` folder!

- This dataset is extracted from the data published in Daie et al. 2021 (*Nat Neuro*). In the original study, the researchers recorded neurons from mouse left anterolateral motor cortex (ALM) while the animals were executing a delayed decision-making task.
- The extracted dataset contains both neural recordings and animal choice for a number of trials. For a mouse `x`, all data are stored in the `data` directory, with format string `recording_{x}.npy`
- For each mouse, 4 data matrices are stored in its `recording_{x}.npy` file:
  - "L", "R" : each contains neural recordings of mouse `x` on *left* or *right* trials. Both are of dimension: n_time_points x n_neurons x n_trials.
  - "correct_L_trials", "correct_R_trials": each contains a boolean value of whether the animal's choice was correct on a given *left* or *right* trial (note: a "left" trials means the audio tone given indicates left, regardless of the animal's decision). Both are of dimensions: n_trials x 1.
- In addition, `recording_{x}.npy` stores the timing of the audio stimulus and go cue (under "go_cue" and "stim").
