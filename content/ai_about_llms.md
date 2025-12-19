Title: AI About LLMs
Date: 2025-10-07
Category: AI
Slug: ai_about_llms
Summary: AI About LLMs

<br>

### Deploying LLMs Locally

#### Setup ollama for executing open source LLM
```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama2:latest
ollama run llama2
```

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
* https://docs.crewai.com/how-to/LLM-Connections/#azure-open-ai-configuration
* https://kaustavmukherjee-66179.medium.com/create-eexcute-crew-ai-agent-with-llama2-model-without-any-need-og-openai-key-def216cd5f4f
* https://thoughtbot.com/blog/how-to-use-open-source-LLM-model-locally
