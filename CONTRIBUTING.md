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

1. 更新 `content/data/recommended-skills.json` 或对应 `content/catalog/` 文档；工具子栏目只编辑 `content/data/tools/index.json` 与 `content/data/tools/<category>.json`，然后运行生成器。
2. 如果修改仓库内 Skill，保持目录名、frontmatter `name` 和触发描述一致。
3. 更新 `CHANGELOG.md` 和核验日期。
4. 运行：

   ```bash
   python tooling/scripts/validate_catalog.py
   python tooling/scripts/build_catalog.py --check
   python tooling/scripts/check_links.py
   git diff --check
   ```

5. 不要在评估阶段执行候选 Skill 自带的脚本。

Tools 的 `content/catalog/tools/` 和 `site/tools/` 是生成文件。运行 `python tooling/scripts/build_catalog.py` 更新，不要分别手工维护三份相同条目。

## 描述写法

描述应回答“什么时候用、解决什么问题、有什么边界”。避免“强大”“生产级”“最佳”等没有证据的表述。实机未运行时明确写 `not-run`。
