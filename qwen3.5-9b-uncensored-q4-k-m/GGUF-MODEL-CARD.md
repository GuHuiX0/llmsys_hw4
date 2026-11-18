---
base_model: mshodiqul/qwen3.5-9b-uncensored
language:
- en
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- qwen3.5
- uncensored
- coding
- agentic
- tool-use
- lora
- fine-tuned
- text-generation
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
<!-- ### quants:  x-f16 Q4_K_S Q2_K Q8_0 Q6_K Q3_K_M Q3_K_S Q3_K_L Q4_K_M Q5_K_S Q5_K_M IQ4_XS -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
static quants of https://huggingface.co/mshodiqul/qwen3.5-9b-uncensored

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#qwen3.5-9b-uncensored-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-GGUF/resolve/main/qwen3.5-9b-uncensored.mmproj-Q8_0.gguf) | mmproj-Q8_0 | 0.7 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-GGUF/resolve/main/qwen3.5-9b-uncensored.mmproj-f16.gguf) | mmproj-f16 | 1.0 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-GGUF/resolve/main/qwen3.5-9b-uncensored.Q4_K_S.gguf) | Q4_K_S | 5.5 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-GGUF/resolve/main/qwen3.5-9b-uncensored.Q8_0.gguf) | Q8_0 | 9.6 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-GGUF/resolve/main/qwen3.5-9b-uncensored.f16.gguf) | f16 | 18.0 | 16 bpw, overkill |

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)

And here are Artefact2's thoughts on the matter:
https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9

## FAQ / Model Request

See https://huggingface.co/mradermacher/model_requests for some answers to
questions you might have and/or if you want some other model quantized.

## Thanks

I thank my company, [nethype GmbH](https://www.nethype.de/), for letting
me use its servers and providing upgrades to my workstation to enable
this work in my free time.

<!-- end -->
