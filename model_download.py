from modelscope import snapshot_download
import os

# 确保目标目录存在
cache_dir = '/root/.ssh/deepseek_project'
os.makedirs(cache_dir, exist_ok=True)  # 自动创建目录（如果不存在）

# 下载模型
model_dir = snapshot_download(
    'qwen/Qwen1.5-7B-Chat',
    cache_dir=cache_dir,
    revision='master'
)

print(f"模型已下载到：{model_dir}")

# 在下载目录下创建py文件
new_file = os.path.join(model_dir, "api.py")
with open(new_file, 'w') as f:
    f.write("# My custom script")
print(f"已创建文件：{new_file}")

