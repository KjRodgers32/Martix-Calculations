import numpy as np

def calculate(list):
  if(len(list) < 9):
    raise ValueError("List must contain nine numbers.")
  else:
    n_list = np.reshape(list,(3,3))

    calculations = {
      'mean': [np.mean(n_list, axis = 0).tolist(),np.mean(n_list, axis = 1).tolist(),np.mean(n_list).tolist()],
      'variance': [np.var(n_list, axis = 0).tolist(),np.var(n_list, axis = 1).tolist(),np.var(n_list).tolist()],
      'standard deviation': [np.std(n_list, axis = 0).tolist(),np.std(n_list, axis = 1).tolist(),np.std(n_list).tolist()],
      'max': [np.max(n_list, axis = 0).tolist(),np.max(n_list, axis = 1).tolist(),np.max(n_list).tolist()],
      'min': [np.min(n_list, axis = 0).tolist(),np.min(n_list, axis = 1).tolist(),np.min(n_list).tolist()],
      'sum': [np.sum(n_list, axis = 0).tolist(),np.sum(n_list, axis = 1).tolist(),np.sum(n_list).tolist()]
    }





    return calculations