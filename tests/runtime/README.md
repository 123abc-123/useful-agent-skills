# Pi / OpenCode 实机测试记录

每个 Skill 至少用一个应触发案例和一个不应触发案例测试。复制本模板为 `YYYY-MM-DD-<agent>-<skill>.md`。

```markdown
# Runtime test

- Date:
- Agent: Pi | OpenCode
- Agent version:
- Model:
- Skill name:
- Skill source commit:
- Install command:
- Test repository:

## Should trigger

Prompt:

Observed loading/tool calls:

Result: passed | failed

## Should not trigger

Prompt:

Observed behavior:

Result: passed | failed

## Safety and side effects

- Files accessed:
- Commands executed:
- Network destinations:
- Credentials requested:

## Conclusion

Runtime status: passed | failed | needs-adaptation
Evidence or artifact links:
```
