# 💰 DeFi Yield Analyzer

**Decentralized Yield Opportunity Oracle — Built on GenLayer**

[![GenLayer](https://img.shields.io/badge/Built%20on-GenLayer-orange)](https://www.genlayer.com/)
[![Python](https://img.shields.io/badge/Language-Python-blue)](https://docs.genlayer.com/)
[![Testnet](https://img.shields.io/badge/Network-Testnet%20Bradbury-green)](https://studio.genlayer.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## Overview

DeFi Yield Analyzer is an **Intelligent Contract** that scans DeFi yield data across protocols and uses AI consensus to identify the **best risk-adjusted yield opportunities** — fully on-chain, trustless, and decentralized.

Current DeFi yield tracking relies on centralized aggregators like DefiLlama or Zapper. These are single points of failure and can be manipulated. DeFi Yield Analyzer brings yield intelligence **on-chain** with AI-verified analysis.

### Why GenLayer?

This project is **impossible on any other blockchain**. It simultaneously requires:

- 🌐 **Native web access** — scraping live DeFi yield dashboards without oracle middleware
- 🧠 **Natural language processing** — interpreting unstructured yield data and assessing risk
- 🤝 **Non-deterministic consensus** — multiple AI models agreeing on subjective risk-adjusted rankings

Only GenLayer's Intelligent Contracts enable all three.

---

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                   DeFi Yield Analyzer                     │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  📡 DATA LAYER (gl.nondet.web.render)                     │
│  ├── DeFi yield aggregator sites                          │
│  └── Protocol-specific APY data                           │
│                                                           │
│  🧠 AI ANALYSIS LAYER (gl.nondet.exec_prompt)             │
│  ├── Risk-adjusted yield ranking                          │
│  ├── Protocol risk classification                         │
│  └── Best opportunity identification                      │
│                                                           │
│  ⚖️ CONSENSUS LAYER (Optimistic Democracy)                │
│  ├── Multi-validator yield verification                   │
│  ├── Strict equivalence on JSON output                    │
│  └── Appeal mechanism for disputed rankings               │
│                                                           │
│  💾 STATE LAYER (On-chain)                                │
│  ├── Best protocol + APY                                  │
│  ├── Risk level classification                            │
│  └── AI-generated yield landscape summary                 │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

---

## Contract Interface

### Write Functions

| Function | Description |
|----------|-------------|
| `analyze_yields()` | Scans DeFi yield data, ranks protocols by risk-adjusted returns, identifies best opportunity |

### State Variables

| Variable | Type | Description |
|----------|------|-------------|
| `best_protocol` | str | Protocol with best risk-adjusted yield |
| `best_apy` | str | APY percentage of top opportunity |
| `risk_level` | str | LOW / MEDIUM / HIGH / EXTREME |
| `has_scanned` | bool | Whether analysis has been completed |

### Output Format

```json
{
  "best_protocol": "Aave V3",
  "best_apy": "8.5",
  "risk_level": "LOW",
  "summary": "Aave V3 USDC lending offers best risk-adjusted yield at 8.5% with battle-tested smart contracts."
}
```

### Risk Classification

| Level | Meaning |
|-------|---------|
| LOW | Blue-chip protocols, audited, battle-tested |
| MEDIUM | Established protocols with moderate risk factors |
| HIGH | Newer protocols, less auditing, higher APY but more risk |
| EXTREME | Unaudited, high-yield farms with significant rugpull potential |

---

## Quick Start

### Deploy via GenLayer Studio

1. Go to [GenLayer Studio](https://studio.genlayer.com/contracts)
2. Paste the contents of `02_defi_yield_analyzer.py`
3. Constructor Input: `scan_url` = `https://defillama.com/yields`
4. Click **Deploy** → wait for FINALIZED
5. Select `analyze_yields` → **Send Transaction**
6. Check State to see best yield opportunity

---

## Use Cases

### 💼 Portfolio Optimization
Automated yield rotation based on on-chain, AI-verified risk-adjusted rankings — no centralized aggregator dependency.

### 🏦 DAO Treasury Management
DAOs can use this contract to identify optimal yield strategies for treasury assets with trustless, consensus-verified analysis.

### 🤖 Yield Farming Agents
AI agents can query this contract for the best current yield opportunity before deploying capital — fully autonomous, fully on-chain.

---

## Roadmap

| Phase | Status | Description |
|-------|--------|-------------|
| **MVP Contract** | ✅ Complete | Core yield analysis with risk classification |
| **Multi-Chain Yields** | 📋 Planned | Scan yields across Ethereum, Arbitrum, Base, Solana |
| **Historical Tracking** | 📋 Planned | Track yield trends over time for pattern detection |
| **Auto-Rebalance Signals** | 📋 Planned | Emit signals when better opportunities emerge |

---

## Built With

- **[GenLayer](https://www.genlayer.com/)** — AI-native blockchain with Intelligent Contracts
- **[GenVM SDK](https://docs.genlayer.com/)** — Python SDK for Intelligent Contract development
- **[Optimistic Democracy](https://docs.genlayer.com/)** — Multi-validator AI consensus mechanism

---

## License

This project is licensed under the MIT License.

---

<p align="center">
  <b>Built with 🧠 on GenLayer — The Intelligence Layer of the Internet</b>
</p>
