# Chinese Translation Style Guide
# 中文翻译风格指南

This guide provides conventions and best practices for translating cryptographic academic papers into Simplified Chinese (简体中文).

## General Principles / 总体原则

### 1. Accuracy First / 准确性第一
- Preserve technical meaning exactly
- Do not simplify or omit technical details
- When in doubt, keep the English term with Chinese explanation

### 2. Readability / 可读性
- Use natural Chinese sentence structure
- Break long sentences into shorter ones when appropriate
- Maintain logical flow and coherence

### 3. Consistency / 一致性
- Use the glossary (GLOSSARY.md) for standard translations
- Be consistent within the document
- Follow established conventions in Chinese cryptography literature

## Terminology / 术语

### Keep in English / 保留英文
The following should generally remain in English:

1. **Proper names**: Dilithium, NIST, Fiat-Shamir
2. **Acronyms**: LWE, SIS, CMA, EUF-CMA, QROM
3. **Algorithm names**: SHA-3, AES
4. **Standard symbols**: O(n), Pr[·]
5. **Programming terms**: hash, bit, byte

### Translate / 翻译
The following should be translated:

1. **Common concepts**: signature (签名), key (密钥), security (安全性)
2. **Academic terms**: proof (证明), theorem (定理), construction (构造)
3. **General verbs**: generate (生成), verify (验证), compute (计算)

### Hybrid Format / 混合格式
For important technical terms, use: **Chinese (English)**

Example:
- "模块带错学习问题 (Module-LWE)"
- "随机预言机模型 (Random Oracle Model, ROM)"

Use this format:
- On first occurrence of a term in each section
- For terms that may be unfamiliar to readers
- In section headings for clarity

## Punctuation / 标点符号

### Chinese Punctuation / 中文标点
Use Chinese punctuation marks in Chinese text:

- 句号：。(period, not .)
- 逗号：，(comma, not ,)
- 顿号：、(enumeration comma)
- 冒号：：(colon)
- 分号：；(semicolon)
- 问号：？(question mark)
- 感叹号：！(exclamation mark)
- 引号：""（double quotes）or ''（single quotes）
- 括号：（）(parentheses)
- 书名号：《》(book/paper title marks)

### Western Punctuation / 西文标点
Keep Western punctuation for:

- Mathematical expressions: f(x), [0, 1], {a, b, c}
- English terms in parentheses: (e.g., LWE)
- Code or pseudocode
- References: [1], [Smith2020]

### Spacing / 空格
Add spaces between Chinese and Western text:

✓ Correct: "我们使用 SHA-3 哈希函数"
✗ Incorrect: "我们使用SHA-3哈希函数"

✓ Correct: "参数 n = 256"
✗ Incorrect: "参数n=256"

## Numbers and Units / 数字和单位

### Numbers / 数字
- Use Arabic numerals: 1, 2, 100, 1000
- For large numbers, use comma separators: 1,000,000
- Percentages: 95% (not 95％)

### Mathematical Notation / 数学符号
- Keep original notation: n, q, κ, λ
- Use standard mathematical symbols unchanged
- Translate surrounding text but keep formulas in English

Example:
```
设 n 为安全参数，q ≡ 1 (mod 2n) 为素数模数。
(Let n be the security parameter and q ≡ 1 (mod 2n) be a prime modulus.)
```

## Sentence Structure / 句子结构

### Active vs. Passive Voice / 主动语态与被动语态
- Chinese prefers active voice
- Convert passive constructions when natural

English: "The signature is verified by checking..."
Chinese: "通过检查...来验证签名" (Active: verify the signature by checking...)

### Academic Tone / 学术语气
Use formal academic language:

- 我们 (we) instead of 咱们
- 提出 (propose) instead of 弄出
- 证明 (prove) instead of 说明

### Paragraph Breaks / 段落划分
- Preserve original paragraph structure
- May combine very short paragraphs if they form one logical unit
- May split overly long paragraphs for readability

## Special Sections / 特殊章节

### Abstract / 摘要
- Concise and self-contained
- Include all key contributions
- Translate paper title at the beginning

### Introduction / 引言
- Maintain the logical flow
- Keep citations in original format: [1], [2, 3]

### Mathematical Proofs / 数学证明
- Keep mathematical notation unchanged
- Translate prose explanations
- Preserve proof structure (lemmas, theorems)

### References / 参考文献
- Keep references in original English
- Do not translate paper titles or author names

## Examples / 示例

### Example 1: Technical Paragraph

**English:**
"Dilithium is a digital signature scheme based on the hardness of lattice problems over module lattices. It is one of the selected algorithms in NIST's post-quantum cryptography standardization process."

**Chinese:**
"Dilithium 是一种基于模格上格问题困难性的数字签名方案。它是 NIST 后量子密码标准化过程中入选的算法之一。"

### Example 2: Mathematical Content

**English:**
"Let q be a prime with q ≡ 1 (mod 2n). We work in the ring R_q = Z_q[X]/(X^n + 1)."

**Chinese:**
"设 q 为素数且满足 q ≡ 1 (mod 2n)。我们在环 R_q = Z_q[X]/(X^n + 1) 中工作。"

### Example 3: Algorithm Description

**English:**
"The algorithm proceeds as follows: First, sample a random vector y. Then, compute w = Ay."

**Chinese:**
"算法执行过程如下：首先，采样一个随机向量 y。然后，计算 w = Ay。"

## Quality Checklist / 质量检查清单

Before submitting a translation:

- [ ] All technical terms match the glossary
- [ ] Chinese punctuation used correctly
- [ ] Spacing correct between Chinese and Western text
- [ ] Mathematical notation preserved
- [ ] Paragraph structure maintained
- [ ] Academic tone consistent
- [ ] No obvious grammar errors
- [ ] Meaning faithful to original

## References / 参考资源

### Chinese Cryptography Terminology
- 中国密码学会术语委员会
- GB/T 25069-2010 《信息安全技术 术语》

### Translation Tools
- Glossary: docs/translation/GLOSSARY.md
- Term database: config/terms_zh.yaml

### Style Guides
- 现代汉语规范字典
- 中文技术文档写作规范

---

For questions or suggestions about this style guide, please open an issue or submit a pull request.
