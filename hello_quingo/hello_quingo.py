#!/usr/bin/env python
# coding: utf-8

# # hello_quingo
# 
# jupyter中使用Path来做获取当前文件的路径似乎报错，因此更换为了os.path

# In[9]:


from pathlib import Path
import os
from quingo import quingo_interface as qi

# qi.set_compiler("mlir")
# qi.connect_backend("pyqcisim_quantumsim")
print(type(os.getcwd()))
qu_file = Path(os.getcwd()) / "kernel.qu"
# 调用 qu_file 中的 bell_state 函数
if qi.call_quingo(qu_file, "bell_state"):
    print(qi.read_result)
else:
    print("error")


# quingo 的 .qu 文件不支持中文字符
# %%
