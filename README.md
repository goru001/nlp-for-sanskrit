# NLP for Sanskrit

This repository contains State of the Art Language models and Classifier for
 Sanskrit, which is an ancient Indian language.

The models trained here have been used in [Natural Language Toolkit for Indic Languages
 (iNLTK)](https://github.com/goru001/inltk) 

## Dataset

#### Created as part of this project
1. [Sanskrit Wikipedia Articles](https://www.kaggle.com/disisbig/sanskrit-wikipedia-articles)

2. [Sanskrit Shlokas Dataset](https://www.kaggle.com/disisbig/sanskrit-shlokas-dataset)

## Results

#### Language Model Perplexity

| Architecture/Dataset | Sanskrit Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  ~6  |
|  TransformerXL |  ~3  |

#### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | Kappa Score |
|:--------:|:----:|:----:|
| Sanskrit Shlokas Dataset |  84.3  |  76.1  |

#### Visualizations
 
##### Embedding Space

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-sanskrit/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-sanskrit/master/language-model/embedding_projector_transformer_config.json)  |


## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1y53xqcqjy-IF2G-inyG4wHAjDGGDpqBv)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1BHtMYpnNB_VJmnzs4wQ1yiIg0coWzEcB)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1erLu1YiSqJxiqNz8ibS0m9VH2sjEB51R)