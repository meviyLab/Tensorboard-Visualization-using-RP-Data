# Tensorboard-Visualization-using-RP-Data
Visualization of unsupervised data (Meviy Rapid Prototype data) using Tensorboard

**Development Overflow:**
![overflow](https://github.com/meviyLab/Tensorboard-Visualization-using-RP-Data/assets/62593581/804640a1-b11f-4ab3-b23f-66d146c5d6d0)

STEP 1: Training Phase:
●　Rapid design data (教師付きデータ) is used as training data.
●　The data is used to train a Graph Neural Network (GNN) model.
●　The GNN model is created using the Rapid design training data.

STEP 2 : Testing Phase:

●　Rapid prototype data (教師なしデータ) is used for testing.
●　The GNN model is applied to the Rapid prototype data.
●　The GNN model extracts a feature vector from the Rapid prototype data.
●　The feature vector is used to compare and find the similarity between different sets of Rapid prototype data.

In summary, the Rapid design data is used to train a GNN model, and the model is then used to extract feature vectors from Rapid prototype data for the purpose of finding similarities between different sets of data.

1. Datasets
●　Random Rapid Prototype data
●　Total data  : 500
●　Total class : 5 class and each class contains 100 data.
●　Time take to convert step to graph data (500 data) : 14min 46sec
●　Time taken to load graph data for feature extraction : 7min 29.2sec

２． Sprite Image (500 png images)
![image-2023-6-9_13-56-47](https://github.com/meviyLab/Tensorboard-Visualization-using-RP-Data/assets/62593581/1af2351e-2105-474a-ab74-7a51f1bd6785)


３．Tensorboard Visualization
![qq](https://github.com/meviyLab/Tensorboard-Visualization-using-RP-Data/assets/62593581/b7ed7cba-cb6d-45e8-85a3-54ce49cd8d68)
