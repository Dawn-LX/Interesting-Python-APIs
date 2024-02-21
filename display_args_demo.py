def display_args(args):
    '''
    args can be `argparse.Namespace`, or simply a dict
    '''
    if hasattr(args,"__dict__"):
        args = args.__dict__
    
    txt = "\n"
    max_name_len = max(len(arg_name) for arg_name in args.keys())
    for arg_name in args.keys():
        arg_value = args[arg_name]  # getattr(args,arg_name)
        arg_type = type(arg_value)
        txt += "{:{L}}:\t{} {}\n".format(arg_name,arg_value,arg_type,L=max_name_len+1)
    
    return txt

def dict_demo():
    pr = {"scores":[0.9,0.5,0.7,0.8],"act_names":["stand","sit","hug","hold"],"path":"test_APIs/xx.py","number":1897}
    print(display_args(pr))

def args_demo():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str,default="model_path")
    # NOTE that we not specify `args.working_dir` at testing time, and `working_dir` is determined by `args.model_path`

    
    parser.add_argument('--topk', type=int,default=1,help="select topk most similar txt_emb for each denoised token")
    parser.add_argument('--seed2', type=int,default=999,help="seed for evaluate time, i.e., determine the initial Gaussian noise")
    parser.add_argument('--vocab_path', type=str,default="vocabularies/vocab_BERT_verbs2741.json")
    parser.add_argument('--act2syn_path', type=str,default="vocabularies/act2syn_by_WordNet.json")
    parser.add_argument('--visual_emb_dir', type=str,default="feature_extraction/HicoDet_UnionRegionEmbds")
    parser.add_argument('--visual_pca_path', type=str)
    parser.add_argument('--step', type=int, help='if less than diffusion training steps, like 1000, use ddim sampling')
    
    parser.add_argument('--clip_denoised', action="store_true")
    parser.add_argument('--save_json', action="store_true")
    parser.add_argument('--add_sim_for_gounding', action="store_true")
    
    parser.add_argument('--top_p', type=int, default=-1, help='top p used in sampling, default is off')
    parser.add_argument('--clamp_step', type=int, default=10, help='x_0 ~ x_clamp_step, use denoised_fn')

    parser.add_argument('--vocab_for_eval', type=str,default="bert",choices=["bert","act2syn","act"])

    args = parser.parse_args()

    print(display_args(args))
    # print(type(args))

if __name__ == "__main__":
    # args_demo()
    dict_demo()
