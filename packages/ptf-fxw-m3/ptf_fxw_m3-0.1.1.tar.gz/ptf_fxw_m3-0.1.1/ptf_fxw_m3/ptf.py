import numpy as np
import pandas as pd 
# import matplotlib.pyplot as plt
import torch
from torch import nn
from torch import optim
# from scipy.io import loadmat
from torch.utils.data import DataLoader,TensorDataset 
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
device='cpu'
print(f'Current_Device:  {device}')
torch.set_default_dtype(torch.float64)
def cal_M3(input):
    class FNN_test(nn.Module):
        def __init__(self,input_size,hidden_size,output_size,layers,**kwargs) -> None:
            super(FNN_test,self).__init__(**kwargs)
            self.input_size=input_size
            self.hideen_size=hidden_size
            self.seq=nn.Sequential()
            for i in range(layers):
                input_size=self.input_size if i ==0 else hidden_size
                self.seq.append(nn.Linear(input_size,self.hideen_size))
                self.seq.append(nn.ReLU())
            self.seq.append(nn.Linear(self.hideen_size,output_size))
            self.seq.append(nn.Sigmoid())
        
        def forward(self,x):
            '''x[batch_size,x_num]'''
            out=self.seq(x)
            out2=torch.zeros(out.shape)
            out2[:,[0]]=-3+2.77815125038364*out[:,[0]]
            out2[:,[1]]=0.004321374+1.17176988527304*out[:,[1]]
            out2[:,[2]]=-2+2.17609125905568*out[:,[2]]
            out2[:,[3]]=-0.698970004336019+0.628388930050312*out[:,[3]]
            out2[:,[4]]=-4+8*out[:,[4]]
            out2[:,[5]]=-4+8*out[:,[5]]
            return out2
    FNN=FNN_test(input_size=4,hidden_size=200,output_size=6,layers=3)
    FNN.to(device=device)
    FNN.load_state_dict(torch.load("M3_H3.pth"))
    Tex_list=torch.tensor([input],dtype=torch.float64)

    with torch.no_grad():  # Predict
        FNN.eval()
        out_para=FNN(Tex_list)
    out_para=pd.DataFrame(10**out_para)
    return out_para