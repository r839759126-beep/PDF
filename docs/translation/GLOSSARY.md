# Terminology Glossary / 术语表

This glossary provides standard Chinese translations for cryptographic and lattice-based cryptography terms used in the Dilithium paper. It is synchronized with `config/terms_zh.yaml`.

## Usage / 使用说明

- **First occurrence**: Use "Chinese (English)" format
- **Subsequent uses**: Use Chinese only
- **Acronyms**: Keep in English (e.g., LWE, QROM)
- **Proper names**: Keep in English (e.g., Dilithium, Fiat-Shamir)

## Core Cryptographic Concepts / 核心密码学概念

| English | 简体中文 | Notes |
|---------|---------|-------|
| lattice | 格 | Mathematical structure |
| lattice-based cryptography | 基于格的密码学 | |
| post-quantum cryptography | 后量子密码学 | |
| quantum-resistant | 抗量子 | Also: 抗量子攻击 |
| digital signature | 数字签名 | |
| signature scheme | 签名方案 | |

## Lattice Problems / 格问题

| English | 简体中文 | Notes |
|---------|---------|-------|
| Learning With Errors | 带错学习 | Often keep as LWE |
| Module-LWE | Module-LWE | Keep in English |
| Ring-LWE | Ring-LWE | Keep in English |
| Short Integer Solution | 短整数解 | Often keep as SIS |
| Module-SIS | Module-SIS | Keep in English |

## Security Notions / 安全性概念

| English | 简体中文 | Notes |
|---------|---------|-------|
| existential unforgeability | 存在性不可伪造 | |
| strong unforgeability | 强不可伪造 | |
| chosen message attack | 选择消息攻击 | Often abbreviated CMA |
| EUF-CMA | EUF-CMA | Keep acronym |
| SUF-CMA | SUF-CMA | Keep acronym |
| security proof | 安全性证明 | |
| security reduction | 安全性规约 | |
| hardness assumption | 困难性假设 | |

## Proof Techniques / 证明技术

| English | 简体中文 | Notes |
|---------|---------|-------|
| Fiat-Shamir | Fiat-Shamir | Keep in English |
| Fiat-Shamir transform | Fiat-Shamir变换 | |
| Fiat-Shamir with aborts | 带中止的Fiat-Shamir | |
| random oracle | 随机预言机 | |
| random oracle model | 随机预言机模型 | Often abbreviated ROM |
| QROM | QROM | Keep acronym |
| quantum random oracle model | 量子随机预言机模型 | |
| rejection sampling | 拒绝采样 | Key technique in Dilithium |

## Mathematical Terms / 数学术语

| English | 简体中文 | Notes |
|---------|---------|-------|
| polynomial | 多项式 | |
| polynomial ring | 多项式环 | |
| ring | 环 | Algebraic structure |
| module | 模 | Algebraic structure |
| modulus | 模数 | |
| coefficient | 系数 | |
| norm | 范数 | |
| infinity norm | 无穷范数 | ‖·‖∞ |
| Euclidean norm | 欧几里得范数 | ‖·‖₂ |
| vector | 向量 | |
| matrix | 矩阵 | |

## Cryptographic Operations / 密码学操作

| English | 简体中文 | Notes |
|---------|---------|-------|
| hash function | 哈希函数 | |
| cryptographic hash | 密码哈希 | |
| commitment | 承诺 | |
| challenge | 挑战 | |
| response | 响应 | |
| encoding | 编码 | |
| decoding | 解码 | |
| compression | 压缩 | |
| decompression | 解压缩 | |

## Key Management / 密钥管理

| English | 简体中文 | Notes |
|---------|---------|-------|
| key generation | 密钥生成 | |
| key pair | 密钥对 | |
| secret key | 私钥 | Also: 秘密密钥 |
| public key | 公钥 | |
| signing key | 签名密钥 | |
| verification key | 验证密钥 | |

## Signature Operations / 签名操作

| English | 简体中文 | Notes |
|---------|---------|-------|
| signing | 签名 | Verb: to sign |
| verification | 验证 | Verb: to verify |
| signature generation | 签名生成 | |
| signature verification | 签名验证 | |
| signer | 签名者 | |
| verifier | 验证者 | |

## Sampling / 采样

| English | 简体中文 | Notes |
|---------|---------|-------|
| sampling | 采样 | |
| uniform sampling | 均匀采样 | |
| Gaussian sampling | 高斯采样 | |
| rejection sampling | 拒绝采样 | |
| distribution | 分布 | |
| uniform distribution | 均匀分布 | |

## Implementation / 实现

| English | 简体中文 | Notes |
|---------|---------|-------|
| implementation | 实现 | |
| optimization | 优化 | |
| performance | 性能 | |
| efficiency | 效率 | |
| throughput | 吞吐量 | |
| latency | 延迟 | |
| benchmarking | 基准测试 | |

## Security Threats / 安全威胁

| English | 简体中文 | Notes |
|---------|---------|-------|
| attack | 攻击 | |
| adversary | 对手/攻击者 | |
| side-channel attack | 侧信道攻击 | |
| timing attack | 时序攻击 | |
| constant-time | 常数时间 | Mitigation technique |
| fault attack | 故障攻击 | |

## Standards / 标准

| English | 简体中文 | Notes |
|---------|---------|-------|
| NIST | NIST | Keep acronym |
| standardization | 标准化 | |
| specification | 规范 | |
| parameter set | 参数集 | |
| security level | 安全级别 | |

## Academic Sections / 学术章节

| English | 简体中文 | Notes |
|---------|---------|-------|
| abstract | 摘要 | |
| introduction | 引言 | |
| preliminaries | 预备知识 | |
| related work | 相关工作 | |
| construction | 构造 | |
| security analysis | 安全性分析 | |
| implementation | 实现 | |
| evaluation | 评估 | |
| conclusion | 结论 | |
| references | 参考文献 | |
| acknowledgments | 致谢 | |
| appendix | 附录 | |

## Academic Terms / 学术术语

| English | 简体中文 | Notes |
|---------|---------|-------|
| theorem | 定理 | |
| lemma | 引理 | |
| corollary | 推论 | |
| proof | 证明 | |
| definition | 定义 | |
| proposition | 命题 | |
| algorithm | 算法 | |
| protocol | 协议 | |
| scheme | 方案 | |
| construction | 构造 | |

## Usage Examples / 使用示例

### Example 1: First Mention
"Dilithium 是一种基于模格上带错学习问题 (Module Learning With Errors, Module-LWE) 困难性的数字签名方案。"

### Example 2: Subsequent Mention
"Module-LWE 问题的困难性保证了方案的安全性。"

### Example 3: Technical Description
"签名方案使用 Fiat-Shamir 变换将交互式证明系统转换为非交互式数字签名。"

### Example 4: Mixed Context
"该方案在随机预言机模型 (Random Oracle Model, ROM) 下具有存在性不可伪造性 (EUF-CMA)。"

## Notes on Translation / 翻译注意事项

1. **Consistency**: Always use the same translation for the same term within a document
2. **Context**: Some terms may have different translations depending on context
3. **Updates**: This glossary is a living document; suggest improvements via pull requests
4. **Acronyms**: Generally keep English acronyms (LWE, CMA, NIST) but provide Chinese on first use
5. **Proper Names**: Keep algorithm names (Dilithium, SHA-3) and researcher names in English

## Maintenance / 维护

This file is manually synchronized with `config/terms_zh.yaml`. When updating:

1. Edit both files to maintain consistency
2. Add usage examples for complex terms
3. Document any context-dependent variations
4. Keep terms in alphabetical order within sections

---

For questions or term suggestions, please open an issue in the repository.
