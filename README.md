# SubtitleDoctorCN

面向中文字幕的本地 SRT 质量检查器。

## MVP

- 时间轴重叠检测
- 字幕持续时间检查
- 阅读速度检测
- 单行长度检查
- 中英文标点混用提示

## 运行

```bash
python main.py example.srt --max-cps 15 --max-line 22 -o report.json
```

## 测试

```bash
python -m unittest -v
```

## License

MIT
