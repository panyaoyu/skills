## functions.exec — 原始参数

~~~javascript
const r=await tools.exec_command({cmd:"rg --files /workspace/scratch/e8b4f9bdf816/read-paper-inputs/time-01/sources","workdir":"/workspace/scratch/e8b4f9bdf816","max_output_tokens":5000});text(r);
~~~

## functions.exec — 可见返回

~~~text
Script completed
Wall time 0.3 seconds
Output:
{"chunk_id":"0bcde2","wall_time_seconds":0.000030084,"exit_code":0,"original_token_count":20,"output":"/workspace/scratch/e8b4f9bdf816/read-paper-inputs/time-01/sources/catalog.md\n"}
~~~

## functions.exec — 原始参数

~~~javascript
text(await tools.exec_command({cmd:"cat /workspace/scratch/e8b4f9bdf816/read-paper-inputs/time-01/sources/catalog.md","workdir":"/workspace/scratch/e8b4f9bdf816","max_output_tokens":10000}));
~~~

## functions.exec — 可见返回

~~~text
Script completed
Wall time 0.3 seconds
Output:
{"chunk_id":"83cc00","wall_time_seconds":0.000023005,"exit_code":0,"original_token_count":311,"output":"# 工作区文献资料\n\n这些是封闭资料集内的来源全文摘要，日期和版本记录是本题给定事实。\n本资料不保证穷尽真实世界的文献；所有名称均为虚构。\n\n## S1 — Amber v1\n\n首次公开：2021-03-01。单通道测量在明亮场景 H 中平均绝对误差为 4 u；\n低照度场景 L 中误差较大。没有研究双通道方法。\n\n## S2 — Beryl v1\n\n首次公开：2022-02-10。双通道方法在明亮场景 H 中的误差为 2 u，\n对照单通道为 4 u，传感器预算相同。未测试低照度场景 L。\n\n## S3 — Beryl v2\n\n本版本公开：2023-01-20；同一文献的首次公开年份仍显示为 2022。\nv2 新增低照度场景 L 的结果：双通道误差 5 u，单通道误差 10 u。\n这项低照度结果不在 2022-02-10 的 v1 中。\n\n## S4 — Cobalt\n\n首次公开：2024-04-09。讨论并复测 Lumen 的低照度结果，在自己的固定样本集上\n报告双通道优于单通道。它直接引用 Lumen v1。\n\n## S5 — Dusk\n\n公开日期无法确定。资料声称双通道在低照度中有优势，没有可核验的版本历史。\n\n## S6 — Ember\n\n公开日期：2022-06-15。只知道日期，不知道具体时刻。独立报告低照度双通道结果。\n"}
~~~
