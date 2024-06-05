import torch, json
from nuc_model import *
from nuc_utils import *
import pandas as pd


class TFBind():
    def __init__(self):
        with open("./data/length.txt", "r") as infile:
            js = infile.read()
            dic = json.loads(js)
            dna_length_max = dic['dna_length_max']
            protein_length_max = dic['protein_length_max']
            self.max_length = dic['max_length']
        self.nuc_model = Nuc()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.nuc_model.load_state_dict(torch.load("./use_model/nuc_20.pth"))
        self.nuc_model.to(device)

    def is_combind(self, protein, dna):
        result = predict_target(protein, dna, self.nuc_model, self.max_length)
        if result == "能够结合":
            return "Combine"
        elif result == "不能够结合":
            return "Not Combine"


if __name__ == '__main__':
    tfbind = TFBind()
    # protein = input("please input protein:")
    # dna = input("please input dna:")
    print(tfbind.is_combind("MGLDDSCNTGLVLGLGLSPTPNNYNHAIKKSSSTVDHRFIRLDPSLTLSLSGESYKIKTGAGAGDQICRQTSSHSGISSFSSGRVKREREISGGDGEEEAEETTERVVCSRVSDDHDDEEGVSARKKLRLTKQQSALLEDNFKLHSTLNPKQKQALARQLNLRPRQVEVWFQNRRARTKLKQTEVDCEFLKKCCETLTDENRRLQKELQDLKALKLSQPFYMHMPAATLTMCPSCERLGGGGVGGDTTAVDEETAKGAFSIVTKPRFYNPFTNPSAAC", "CAAAATAATTGTT"))