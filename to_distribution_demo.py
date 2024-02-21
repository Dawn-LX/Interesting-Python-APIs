import torch
import matplotlib.pyplot as plt

def to_distribution(xx,n_interval=100,boundary=[0,1],to_ratio=False):
    assert len(xx.shape) == 1
    s,e = boundary
    t_range = torch.linspace(s,e,n_interval)

    dis_matrix = torch.abs(xx[:,None] - t_range[None,:])  #(n,T)
    tid = torch.argmin(dis_matrix,dim=-1)  # (n,)
    count = torch.bincount(tid)
    if len(count) < len(t_range):
        count = torch.constant_pad_nd(count,pad=(0,len(t_range)-len(count)),value=0)
    
    if to_ratio:
        count = count.float() / count.sum()
    return t_range,count


def to_distribution2(xx,n_interval=100,boundary=[0,1],to_ratio=False):
    assert len(xx.shape) == 1
    s,e = boundary
    t_range = torch.linspace(s,e,n_interval)

    dis_matrix = torch.abs(xx[:,None] - t_range[None,:])  #(n,T)
    mask = dis_matrix == torch.min(dis_matrix,dim=-1)[0][:,None]  # (n,T)
    count = mask.sum(dim=0)  # (T,)
    if to_ratio:
        count = count.float() / count.sum()
    
    return t_range,count

# xx = torch.tensor([0.2,0.2,0.6,0.5,0.3])
xx = torch.randn(size=(10000,))
t,c = to_distribution(xx,boundary=[-3,3])

plt.plot(t,c)
plt.show()
