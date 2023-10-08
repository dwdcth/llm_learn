# llm_learn


- [鲁迅风格的聊天机器人](luxun_style.py) 使用ai21，也可以使用 openai 需要 15 美元
- [训练Bloom 1b4 中文LoRA](notebook/bloom_1b4_zh_lora.ipynb) &ensp; [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CuE-Wukxmib5KjnfY0c3GI223aLnsVBY?usp=sharing)
- [词向量和句向量对比](notebook/词向量和句向量.ipynb) &ensp; [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ltEV9dgB-BqdzIdisqYgEvrlv1_iwWQi?usp=sharing)




词向量和句向量对比结果：

| 句子                                | shibing624/text2vec-base-chinese | silk-road/luotuo-bert | GanymedeNil/text2vec-large-chinese | sentence-transformers/paraphrase-multilingual-MinilM-L12-v2 | w2v-light-tencent-chinese | 手工w2v-light-tencent-chinese | text-embedding-ada-002 | text-similarity-davinci-001 | text-search-ada-doc-001 | Llama  |
| ----------------------------------- | -------------------------------- | --------------------- | ---------------------------------- | ----------------------------------------------------------- | ------------------------- | ----------------------------- | ---------------------- | --------------------------- | ----------------------- | ------ |
| 今天天气很好/今天天气很差           | 0.8692                           | 0.9549                | 0.7792                             | 0.3938                                                      | 0.9778                    | 0.9204                        | 0.9297                 | 0.864                       | 0.9744                  | 0.8367 |
| 今天天气很好/今天天气晴朗，万里无云 | 0.6644                           | 0.9327                | 0.5236                             | 0.7946                                                      | 0.9019                    | 0.7687                        | 0.9159                 | 0.905                       | 0.8902                  | 0.5833 |
