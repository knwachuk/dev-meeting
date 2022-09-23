import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as py 

def truth_viz(perceived truth, 
ground_truth =None, spacing=5, ratio=1/5,
offset =10, image=False):


    cat_pos = {cat: (i*3)+2 for i, cat in 
    enumerate(perceived_truth["Category 
    Tag"].unique())}

    x = np.linspace(1, int(perceived_truth
    ["Time (Seconds)"].max()), int
    (perceived_truth["Time (Seconds)"].max
    ()/spacing))
