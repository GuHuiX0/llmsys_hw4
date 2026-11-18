---
license: apache-2.0
base_model: DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED
library_name: transformers
tags:
- qwen3.5
- uncensored
- coding
- agentic
- tool-use
- lora
- fine-tuned
- text-generation
language:
- en
pipeline_tag: text-generation
---

# Qwen3.5-9B Uncensored Coder

A LoRA fine-tune of [DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED](https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED) — an uncensored
("heretic") Qwen3.5-9B — trained on agentic-coding, tool-use and function-calling
traces to sharpen **coding + agent** ability while keeping the uncensored behaviour.

## Training

| | |
|---|---|
| Base | `DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED` (BF16) |
| Method | LoRA SFT (r=64, α=128, dropout 0.05) |
| Targets | `q/k/v/o_proj`, `gate/up/down_proj`, `in_proj_qkv`, `in_proj_z`, `out_proj` |
| Trainable params | 160.4M (1.68% of 9.57B) |
| Hardware | 1× NVIDIA H200 |
| Framework | transformers 5.17, peft 0.20, bf16, gradient checkpointing |
| Steps | 1500 |
| Effective batch | 8 × 4 |
| LR | 5e-05 (cosine, warmup 3%) |
| Max seq len | 1536 |
| Final train loss | ≈ 0.866 |

### Data

| Dataset | Rows used |
|---|---|
| `NousResearch/hermes-function-calling-v1` | 11,576 |
| `Solstice-AI/Complete-FABLE.5-traces-2M` (filtered) | 491,714 |
| **Total** | **≈ 503,290** |

Assistant-only loss masking with the native Qwen3.5 chat template (thinking blocks
handled automatically). The raw datasets are synthetic and contained a large family
of generic "reasoning" templates plus some model-identity contamination; rows were
aggressively filtered before training (see *Known limitations*).

## Test results

| Test | Result |
|---|---|
| Tool calling — single call | ✅ pass |
| Tool calling — multi-select (6 tools) | ✅ pass |
| Tool calling — coding agent | ✅ pass |
| Tool calling — parallel (2 calls) | ✅ pass |
| Tool calling — correctly declines when no tool needed | ✅ pass |
| Hermes XML format validity | ✅ strict-valid |
| Coding — LRU cache | ✅ pass |
| Coding — quicksort / longest palindrome | ✅ pass |
| Reasoning (bat & ball) | ✅ pass |
| Bash script (with thinking disabled) | ✅ pass |
| Web — vanilla HTML/CSS/JS | ✅ renders + interactive, 0 JS errors |
| Web — React 18 (CDN + Babel) | ✅ renders + useState works, 0 JS errors |
| Web — Vue 3 (CDN, Options API + computed) | ✅ renders + reactive, 0 JS errors |
| Uncensored — security research | ✅ answered (no refusal) |
| Uncensored — creative writing | ✅ answered (no refusal) |
| Long-context recall (8k → 256k) | ✅ verified at 8k, 32k, 64k, 131k, 192k, 256k |

## Usage

```python
from transformers import AutoModelForImageTextToText, AutoTokenizer

repo = "mshodiqul/qwen3.5-9b-uncensored"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForImageTextToText.from_pretrained(repo, torch_dtype="bfloat16", device_map="auto")

messages = [{"role": "user", "content": "Write a Python LRU cache with O(1) get/put."}]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

### Serving with vLLM

```bash
vllm serve mshodiqul/qwen3.5-9b-uncensored \
  --tool-call-parser qwen3_xml \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --max-model-len 262144
```

`--reasoning-parser qwen3` splits the thinking block into `reasoning_content`,
keeping the final answer clean.

### Tool calling

Pass tools through the chat template; the model emits the Qwen3.5
`<tool_call><function=...><parameter=...>` XML format:

```python
tools = [{"type": "function", "function": {
    "name": "get_weather",
    "description": "Get current weather for a city",
    "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]
text = tok.apply_chat_template(messages, tools=tools, tokenize=False, add_generation_prompt=True)
```

## Known limitations

- **Thinking-block contamination on long shell/script prompts.** With thinking
  *enabled*, long bash-script requests can pull the model into a generic
  "security analysis" template inherited from the synthetic data, producing an
  off-topic final answer. Workarounds: serve with `--reasoning-parser qwen3`
  (keeps thinking out of the answer) or disable thinking for shell-heavy tasks.
  Simple shell one-liners are unaffected.
- **Model identity.** Asked directly "who are you", the model may answer with a
  name inherited from the training data rather than the base model's identity.
- **Context window**: 262,144 tokens (native). Recall was empirically verified up
  to 256k with needle-in-haystack, but practical output length is a few thousand
  tokens.
- The vision tower is preserved but was **not** trained (text-only SFT).
- Uncensored behaviour is inherited from the base "heretic" model.
