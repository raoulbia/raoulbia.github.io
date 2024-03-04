Title: AI About LLMs
Date: 2024-01-02
Category: AI
Slug: ai_about_llms
Summary: AI About LLMs
<br>

### Finetuning LLMs
* there are a lot of different tokenizers and a tokenizer is really associated with 
a specific model for each model as it was trained on it. And if you give the wrong tokenizer to your model, it'll 
be very confused because it will expect different numbers to represent different sets of letters 
and different words. So make sure you use the right tokenizer.

* The AutoTokenizer class from the Transformers library by HuggingFace automatically finds the right tokenizer or for your 
model when you just specify what the model is. So all you have to do is put the model and name in.

```
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-70m")
```


### Resources

* [deeplearning.ai - Finetuning LLMs](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/)
