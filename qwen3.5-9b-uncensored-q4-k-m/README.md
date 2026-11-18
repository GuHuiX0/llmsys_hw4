# Qwen3.5 9B Uncensored - GGUF Q4_K_M

These are the GGUF weights from the upstream model, encoded as plain base64.
The base64 is split into 150 parts, each at most 48 MiB. Keep all parts together.

From the repository root, decode with Python 3.8 or newer:

```sh
python qwen3.5-9b-uncensored-q4-k-m/decode.py
```

On Linux/macOS use python3 if needed. No extra Python packages are required.
The decoder checks every part and the reconstructed model against SHA-256.
The restored file is qwen3.5-9b-uncensored.Q4_K_M.gguf in this folder.
Allow 5.63 GB of additional disk space for the decoded GGUF.

Source: https://huggingface.co/mradermacher/qwen3.5-9b-uncensored-GGUF/resolve/ad62a6aa367341aa47262e20259c12956a98fad4/qwen3.5-9b-uncensored.Q4_K_M.gguf

The weights are redistributed unchanged under Apache-2.0; see LICENSE.txt and the model cards.
validation.json records the source checksum, GGUF header, and verification of decoding the Git objects.
Inference was not run as part of this upload.
