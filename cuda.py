import torch

print(torch.cuda.is_available())  # check if CUDA is available
print(torch.version.cuda)  # check the version of CUDA
print(torch.backends.cudnn.version())  # check the version of cuDNN

