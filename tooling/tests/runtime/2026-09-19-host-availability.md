# 2026-09-19 测试主机可用性检查

- 检查环境：仓库维护任务所在的 Windows 主机
- 检查命令：`Get-Command pi, opencode, npx, node`
- 可用：Node.js、npx
- 不可用：Pi CLI、OpenCode CLI

因此，本次更新只完成了固定源码、许可证、数据结构、安装语法、页面和 CI 检查，没有执行 Pi/OpenCode 实机加载与行为测试。所有相关 `runtime_pi` 与 `runtime_opencode` 字段继续保持 `not-run`。

安装任一 CLI 后，应按照 [`tooling/tests/runtime/README.md`](README.md) 的模板测试“应该触发”和“不应触发”两类案例，再更新对应状态和证据路径。
