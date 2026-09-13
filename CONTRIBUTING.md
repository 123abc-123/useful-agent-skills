# 贡献指南

## 提交一个候选 Skill

请提供以下信息：

- Skill 名称和原始 GitHub 仓库；
- 具体 `SKILL.md` 路径；
- 它解决的真实工作问题；
- 许可证和最近核验 commit；
- 脚本、网络、凭据和高权限行为；
- Pi 与 OpenCode 的安装或适配情况；
- 是否有实际运行记录和可复现结果。

安装量、star 或社交平台推荐只能作为发现线索。新增精选项必须回到原始仓库复核，并按照 [评分规则](SCORING.md) 记录判断。

## 修改流程

1. 更新 `data/recommended-skills.json` 或对应 `catalog/` 文档。
2. 如果修改仓库内 Skill，保持目录名、frontmatter `name` 和触发描述一致。
3. 更新 `CHANGELOG.md` 和核验日期。
4. 运行：

   ```bash
   python scripts/validate_catalog.py
   python scripts/check_links.py
   git diff --check
   ```

5. 不要在评估阶段执行候选 Skill 自带的脚本。

## 描述写法

描述应回答“什么时候用、解决什么问题、有什么边界”。避免“强大”“生产级”“最佳”等没有证据的表述。实机未运行时明确写 `not-run`。
