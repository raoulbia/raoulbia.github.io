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


## GPU Assessment:

  | Metric   | Value | Assessment             |
  |----------|-------|------------------------|
  | GPU Util | 88%   | Good, not bottlenecked |
  | Temp     | 68°C  | Normal                 |
  | Power    | 56W   | Moderate               |

  Speed factors (not learning rate):

  | Parameter         | Current    | Could Speed Up?                      |
  |-------------------|------------|--------------------------------------|
  | local_batch_size  | 1          | Increase to 2-4 if memory allows     |
  | global_batch_size | 16         | Means 16 gradient accumulation steps |
  | seq_length        | 2048       | Lower if your data is shorter        |
  | Precision         | bf16-mixed | Already optimal                      |

  88% utilization is solid. The main bottleneck is local_batch_size: 1 - you're processing 1 sample at a time with 16 accumulation steps. With 128GB unified
  memory, you could likely increase to local_batch_size: 2 or 4 to speed things up ~2-4x.

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

