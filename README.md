# NLP for Sanskrit

This repository contains State of the Art Tokenizer, Language model and Classifier for Sanskrit, which is an ancient Indian language.

## Dataset

* Download [Sanskrit Wikipedia Articles Dataset](https://drive.google.com/open?id=1nfV1EDHgPvrsrA1Jubt-C4wBRRFlQzsJ) (22,273 articles) which I scraped, cleaned and
used to train the language model

* Download [Sanskrit Shlokas Dataset](https://drive.google.com/open?id=1EHTuDUOx-AgIcHHwBfXJMyhpdgr-KcWd) which I scraped and used to train 
the classifier

## Results

#### Language Model

* Perplexity of language model: ~6 (on 30% validation set)

#### Classifier

* Accuracy of classification model: ~70%
* Kappa score of classification model: ~56

## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1y53xqcqjy-IF2G-inyG4wHAjDGGDpqBv)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1BHtMYpnNB_VJmnzs4wQ1yiIg0coWzEcB)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1erLu1YiSqJxiqNz8ibS0m9VH2sjEB51R)