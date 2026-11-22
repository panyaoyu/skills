# 中英双向术语表

每行记录一个概念。先根据原句含义选择词条，需要区分词义时参照「备注」。备注留空表示该概念无需额外说明。

- 中译英时采用「English」列的写法。英译中时采用「中文」列的写法；该列为英文时保留英文。
- 「英文不要用」和「中文不要用」只约束译文中表达本行概念的用词。若原文使用了其中的词，先辨明词义；确指本行概念时，采用目标语言的规范写法。仅凭词形相同，不能判定用词有误。

例如，任务要求的目标值称为「规格」，英文用 specification。只有在指 Aspen Plus 的「设计规定」工具时，才应避免用 specification，采用 design spec。

只收译法不固定会造成误解的词：同一个概念用了不同译法，读者可能以为是不同的东西；或者一个译法容易和另一个概念混淆。化工标准术语和普通词不收。

| 中文 | English | 英文不要用 | 中文不要用 | 备注 |
|---|---|---|---|---|
| 任务描述 | task description | prompt | 题目 | 说明任务要求的文字 |
| 报告文件 | report file | report | 报告 | 指文件本身，如 Aspen Plus 导出的 `.rep` 文件 |
| 流股 | stream | flow | 物流 | 化工流程中的流股，如进料流股、产品流股 |
| 设备 | block | unit, equipment | 模块、块、单元 | Aspen Plus 流程图中的设备模型 |
| 物性方法 | property method | thermodynamic model, property package | | |
| 流程 | flowsheet | process | | 由设备和流股组成的模拟流程 |
| 严格模型 | rigorous model | mechanistic model | | 与简捷模型相对，不同于机理模型 |
| 简捷模型 | shortcut model | simplified model | 简化模型 | 与严格模型相对 |
| 有效相态 | valid phases | effective phase | | |
| 气相分率 | vapor fraction | vaporization fraction | 气化分率 | |
| 规格 | specification | spec | | 任务描述要求的目标值 |
| 设计规定 | design spec | specification | | Aspen Plus 中用来达到目标值的工具 |
| 调节变量 | manipulated variable | adjusted variable | | |
| 基准 | basis | reference | | 如指定组成时选用的摩尔基准或质量基准 |
| 动力学因子 | kinetic factor | rate factor | | LHHW 速率方程分子中的速率常数项 |
| 推动力项 | driving force term | | 驱动力项 | LHHW 速率方程分子中的可逆反应浓度项 |
| 吸附项 | adsorption term | | | LHHW 速率方程分母中求和的一项 |
| 吸附表达式 | adsorption expression | | | LHHW 速率方程的整个分母 |
