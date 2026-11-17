# Whisper small — CTranslate2 INT8

This folder contains the multilingual Whisper small model with INT8 weights for faster-whisper.
The weights are plain base64 split into seven files below GitHub's 100 MiB file limit.

From the repository root, restore the weights with Python 3.8 or newer:

```sh
python faster-whisper-small-int8/decode.py
```

On Linux/macOS, use `python3` if needed. This command requires no extra packages.
It verifies every part and the reconstructed `model.bin`. Keep all parts and support files together.

Install faster-whisper in your application environment:

```sh
pip install faster-whisper
```

Then load the folder from the repository root:

```python
from faster_whisper import WhisperModel

model = WhisperModel(
    "faster-whisper-small-int8",
    device="cpu",
    compute_type="int8",
    local_files_only=True,
)
segments, info = model.transcribe("audio.wav")
for segment in segments:
    print(segment.text)
```

Included: model.bin.b64.part0000 through part0006, config.json, tokenizer.json,
vocabulary.txt, decode.py, manifest.json, validation.json, SHA256SUMS, and LICENSE.txt.

The base64 decodes to unchanged CTranslate2 INT8 weights from
[rhasspy/faster-whisper-small-int8](https://huggingface.co/rhasspy/faster-whisper-small-int8/tree/a94e151d8147ce851767640f24b3e854cf60def7).
Tokenizer: [Systran/faster-whisper-small](https://huggingface.co/Systran/faster-whisper-small/tree/536b0662742c02347bc0e980a01041f333bce120).
License: MIT; see LICENSE.txt. The model was tested with offline faster-whisper inference.
The split base64 was decoded again and verified before this folder was committed.
