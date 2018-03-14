# NLP and Text Summarization
This is a collection of my exploration in the NLP domain specifically around text summarization

My work sofar explore extractive approach to text summarization.

## Getting Started
I will recommend working on this within a virtual python environment. If you are in one you can simply run

```bash
pip install -r requirements.txt
```

The requirements file contains way more dependencies thatn you'll need. It's laziness on my part to have just not cleaned this up along the way.

I leverage NLTK in base_summarizer.py and you will need to do something like below in python repl to download 'stopwords' and 'punkt' (for tokenization

```bash
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
>>> exit()
```

I would love your feedback and welcome pull/merge requests. I have been mindful to credit where I have leveraged someone else's code.


