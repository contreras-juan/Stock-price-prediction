import numpy as np

def create_sequence(dataset):
  sequences = []
  labels = []

  start_idx=0

  for stop_idx in range(50, len(dataset)):

    sequences.append(dataset[start_idx:stop_idx])
    labels.append(dataset[stop_idx])

    start_idx+=1

  return (np.array(sequences), np.array(labels))