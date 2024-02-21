from tqdm import tqdm
import time

def demo1():
    outer_loop = range(10)
    inner_loop = range(5)

    for i in tqdm(outer_loop,desc="outer_loop",position=0,ncols=160,leave=True):  # leave  means NOT disappear
        for j in tqdm(inner_loop,desc="inner_loop",position=1,ncols=150,leave=False): # leave=False means disappear=True
            time.sleep(0.5)
    



def demo2():
    epochs = 5
    len_loader = 10
    total_step = epochs * len_loader


    pbar_global = tqdm(total=total_step,desc="global iter", position=0, leave=True)
    pbar_local = tqdm(total=len_loader,desc="per epoch iter", position=1, leave=False)

    done_epochs = 0
    for it in range(total_step):
        time.sleep(0.5)

        pbar_global.update()
        pbar_local.update()
        if (it+1) % len_loader == 0:
            done_epochs +=1
            pbar_local.reset()
        
        
    
    pbar_global.close()
    pbar_local.close()


def demo3():
    epochs = 5
    len_loader = 10
    total_step = epochs * len_loader


    pbar_global = tqdm(total=epochs,desc="global epochs", position=0, leave=True)
    pbar_local = tqdm(total=len_loader,desc="per epoch iter", position=1, leave=True)

    done_epochs = 0
    for it in range(total_step):
        time.sleep(0.5)

        
        pbar_local.update()
        if (it+1) % len_loader == 0:
            done_epochs +=1
            pbar_global.update()
            pbar_local.reset()
    
    pbar_global.close()
    pbar_local.close()

if __name__ == "__main__":
    # demo1()
    demo3()
