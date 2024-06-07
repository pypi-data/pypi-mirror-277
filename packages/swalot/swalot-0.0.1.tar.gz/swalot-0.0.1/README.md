## Installation

You can install the Memory Protector package using pip:

```bash
pip install swalot
```


## Usage

Simply import and wrap training code:
```python
import swalot as sw

with sw.protext():
    """
    use CUDA tensor calculation here as usual.
    All RAM will be protected automatically!
    e.g.
    """
    # a = torch.randn(1000, 1000, 600).cuda()
```