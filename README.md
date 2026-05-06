# HF Deploy Demo

GitHub → Hugging Face Space 自动部署模板。

## 工作原理

1. 推送代码到 GitHub `main` 分支
2. GitHub Actions 自动触发
3. 将代码同步到 HF Space
4. HF Space 自动构建部署

## 配置

1. 在 GitHub 仓库 Settings → Secrets and variables → Actions 中添加：
   - `HF_TOKEN`: Hugging Face Access Token（需要 write 权限）

2. 修改 `.github/workflows/deploy-hf.yml` 中的 HF Space 地址：
   ```
   git remote add hf https://<YOUR_HF_USERNAME>:$HF_TOKEN@huggingface.co/spaces/<YOUR_HF_USERNAME>/<SPACE_NAME>
   ```

## 使用

```bash
# 克隆仓库
git clone https://github.com/arwei944/hf-deploy-demo.git
cd hf-deploy-demo

# 修改 app.py 后推送
git add .
git commit -m "update app"
git push
```

推送后 GitHub Actions 会自动将代码部署到 HF Space。

## HF Space

- [hf-deploy-demo](https://huggingface.co/spaces/arwei944/hf-deploy-demo)
