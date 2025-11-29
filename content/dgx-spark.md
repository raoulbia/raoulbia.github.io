Title: DGX Spark
Date: 2025-11-17
Category: AI
Slug: dgx_spark
Summary: DGX Spark Misc.

## Fine-tuning Options on DGX Spark (GB10, 128GB unified memory)

  | Option                | Framework         | Pros                                                       | Cons                           |
  |-----------------------|-------------------|------------------------------------------------------------|--------------------------------|
  | NeMo + LoRA (current) | NVIDIA NeMo       | Official NVIDIA support, optimized for DGX, proven working | Complex setup, container-based |
  | Unsloth               | HuggingFace-based | 2x faster, 60% less memory, simple API                     | Less NVIDIA optimization       |
  | Axolotl               | HuggingFace-based | YAML config, many techniques (LoRA, QLoRA, full)           | Medium complexity              |
  | HuggingFace PEFT      | Transformers      | Most popular, huge community                               | Manual optimization needed     |
  | LLaMA-Factory         | HuggingFace-based | Web UI, no-code option                                     | Less control                   |


## Misc
```
docker start vllm-server
docker logs -f --tail 50 vllm-server
```
## ~/.ssh/config
````
Host dgx-spark
    HostName 192.168.1.xx
    User <user-name>
    IdentityFile ~/.ssh/<name-of-pub-ssh-key>
    IdentitiesOnly yes
    LocalForward 8000 localhost:8000
    LocalForward 11434 localhost:11434
````

## SSH Tunnel
`ssh -N -L 8000:localhost:8000 -L 12434:localhost:12434 user@spark-e123.local`

## Example Roo Code configuration for vLLM:

* API Provider: `OpenAI Compatible`
* Base URL: `http://localhost:8000/v1`
* API Key: `not-required`
* Model: `Qwen/Qwen2.5-Coder-14B-Instruct`

