import torch
from utils_func import unique_with_idx_nd

mat = torch.randint(0,2,size=(20,3))
uniq_mat,index_map = unique_with_idx_nd(mat)
print(index_map,len(index_map))  # len == N_uniq
for i,imp in enumerate(index_map):
    for j in imp:
        assert torch.all(uniq_mat[i] == mat[j])

uniq_mat,inverse_indices, counts = torch.unique(mat,return_inverse=True,return_counts =True,dim=0)
print(inverse_indices,len(inverse_indices))  # len == N
assert torch.all(uniq_mat[inverse_indices] == mat)
