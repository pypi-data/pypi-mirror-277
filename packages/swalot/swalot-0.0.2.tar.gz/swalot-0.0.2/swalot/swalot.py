import torch
import GPUtil
import numpy as np
from rich import print
from functools import partial, update_wrapper



class MemoryProtector:
    def __init__(self, reserved_cache=256, device=0):
        self.device = device
        self.reserve_tensor = None
        self.res_cache = reserved_cache    # save x MB for others as default
        self.protecting_mb = 0
        self.device_list = []
        self.device = "cuda:0"
        # self.smooth_mode = False

        self.protect()

    def protect(self):
        """Reserves (total free memory - self.res_cache) MB of memory on the GPU."""
        free_memory = GPUtil.getGPUs()[self.device].memoryFree
        reserve_mb = max(0, free_memory - self.res_cache)  # Reserve as much as possible, minus the res_cache

        if self.reserve_tensor is not None:
            # Free existing reserved memory before reallocating
            self.free_memory()

        # Convert MB to number of float32 elements (4 bytes each)
        reserve_elements = int(reserve_mb * 1024 * 1024 / 4)
        # self.reserve_tensor = cp.empty(reserve_elements, dtype=cp.float32)
        self.reserve_tensor = torch.from_numpy(np.empty(reserve_elements, dtype=np.float32)).to(self.device)


        self.protecting_mb = reserve_mb
        # print("Protecting RAM: {} MB".format(reserve_mb))
        print("[bold cyan][Info][/bold cyan][bold magenta] | swat:[/bold magenta] Protecting RAM: [bold green]{} MB[/bold green]".format(reserve_mb))


    def free_memory(self):
        self.reserve_tensor = None
        # cp.get_default_memory_pool().free_all_blocks()
        torch.cuda.empty_cache()

    def restore(self):
        self.protect()


class AutoMemoryProtector:
    def __init__(self, protector):
        self.protector = protector
        self.original_cuda = torch.Tensor.cuda

    def __enter__(self):
        # Create a new method 'custom_cuda' and update the wrapper to match the original 'cuda' method
        def custom_cuda(tensor, *args, **kwargs):
            try:
                return self.original_cuda(tensor, *args, **kwargs)
            except RuntimeError as e:
                if 'CUDA out of memory' in str(e):
                    if(self.protector.protecting_mb <= 0):
                        # print("It actually no memory...")
                        raise e
                    # print("Oops... Should be CUDA out of memory. But we have secret {} MB!".format(self.protector.protecting_mb))
                    self.protector.free_memory()
                    result = self.original_cuda(tensor, *args, **kwargs)
                    self.protector.restore()
                    return result
                else:
                    raise

        # 保持 custom_cuda 函数的签名和文档字符串与原始的 torch.Tensor.cuda 方法一致
        update_wrapper(custom_cuda, self.original_cuda)

        # 通过 custom_cuda.__get__(None, torch.Tensor) 手动绑定 custom_cuda 方法到 torch.Tensor 类
        torch.Tensor.cuda = custom_cuda.__get__(None, torch.Tensor)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        torch.Tensor.cuda = self.original_cuda