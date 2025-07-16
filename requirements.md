# requirements

- pandoc >= 3.5
- MiKTeX >= 4.12
- CUDA 12.4
- Microsoft C++ Build Tools (compilers)

- python == 3.10

## python libs

### freeze

- `pip freeze` > [requirements.txt](requirements.txt)

**install (win):**

<!-- `pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124` -->

1. `cd ./modules/REINVENT4/`
2. `python install.py cu124`
3. `cd ../..`
4. `pip install -r requirements.upd`

### updatable

[requirements.upd](requirements.upd)
