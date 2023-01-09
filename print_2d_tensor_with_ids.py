import torch

def print_2d_tensor_with_ids(tensor):
    assert len(tensor.shape) == 2

    n,m = tensor.shape
    
    lines = str(tensor).split('\n')
    # c= [x for x in c]
    lines_ = []
    for i,x in enumerate(lines):
        x = "{:02d} ".format(i) + x[8:]
        lines_.append(x)
    lines_[-1] = lines_[-1][:-2]
    len_ = int((len(lines_[0]) -3) / m) - 2  # 3 is "{:02d} " and 2 is "{:02d}"
    head = " "*3
    for i in range(m):
        len_prefix = len_//2
        len_sufix = len_ - len_prefix
        head += " " * len_prefix +  "{:02d}".format(i) + " " * len_sufix
    
    lines_ = [head] + lines_
    for x in lines_:
        print(x)


def main():

    # xx = torch.rand(size=(1,1))
    xx = torch.randint(0,91,size=(12,16))
    print_2d_tensor_with_ids(xx)

if __name__ == "__main__":
    torch.manual_seed(111)
    torch.set_printoptions(linewidth=160)
    demo()
