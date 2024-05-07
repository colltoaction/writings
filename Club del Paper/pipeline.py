from discopy.frobenius import Box, Ty, Diagram, Spider, Id, Spider, Swap


d = Ty("data")
m = Ty("model")
tr_d = Ty("training data")
te_d = Ty("testing data")
a = Ty("accuracy")
mx = Ty("matrix")
split = Box("split", d, tr_d @ te_d)
train = Box("train", tr_d, m)
trainM1 = Box("train M1", tr_d, m)
trainM2 = Box("train M2", tr_d, m)
trainM3 = Box("train M3", tr_d, m)
test = Box("test", m @ te_d, a)
CPU = Box("CPU", tr_d, mx @ mx)
TPU = Box("TPU", mx @ mx, m)
GPU = Box("GPU", mx @ mx, m)
TPU2 = Box("TPU", mx @ mx @ mx @ mx, m)
pipeline1 = split >> train @ te_d >> Spider(1, 2, m) @ te_d >> m @ test
trainM123 = Spider(1, 3, tr_d) >> trainM1 @ trainM2 @ trainM3 >> Spider(3, 1, m)
pipeline2 = split >> trainM123 @ te_d >> Spider(1, 2, m) @ te_d >> m @ test
CPU_to_TPU = CPU >> TPU
CPU_to_GPU = CPU >> GPU
trainTPU = Spider(1, 2, tr_d) >> trainM1 @ (Spider(1, 2, tr_d) >> CPU_to_TPU @ CPU_to_TPU >> Spider(2, 1, m))
trainTPU2 = Spider(1, 2, tr_d) >> CPU_to_GPU @ (Spider(1, 2, tr_d) >> CPU @ CPU >> TPU2) >> Spider(2, 1, m)
pipeline3 = split >> trainTPU2 @ te_d >> Spider(1, 2, m) @ te_d >> m @ test

pipeline1.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="pipeline/1.png")
trainM123.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="pipeline/trainM123.png")
pipeline2.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="pipeline/2.png")
trainTPU.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="pipeline/trainTPU.png")
trainTPU2.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="pipeline/trainTPU2.png")
pipeline3.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="pipeline/3.png")
