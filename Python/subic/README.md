# SUBIC

# 概要
[SUBIC: A supervised, structured binary code for image search](https://arxiv.org/pdf/1708.02932.pdf)
- 2017年にarXivに掲載された論文
- 従来からあるベクトル量子化法(Vector Quantization; VQ)や直積量子化法(Product Quantization; PQ)とは違い，DNNを使用し，かつ教師ありで学習できるようにした．
- この手法の肝として，損失関数にblock-softmax関数とbatch-base entropy関数を用いたことがある．

## 実装

- 実行環境(2019/2/25現在)
  - Python 3.6
  - numpy 1.14
  - PyTorch 1.0 

- プログラムについて
    - base_cnn.py: base部分に用いられるCNNの実装を行った．CNNの構造は論文(https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Liu_Deep_Supervised_Hashing_CVPR_2016_paper.pdf)を使用．