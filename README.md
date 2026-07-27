# X402 Payment Gateway

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Chains](https://img.shields.io/badge/Chains-RH%20%7C%20BSC%20%7C%20EVM-lightgrey)](configs/)

**Sell agent output, get paid in U**

Self-hosted x402 gateway for AI agent services: EIP-712 proof verification, Binance Pay facilitator settlement, async job store, S3 delivery.

## Quick start

```bash
git clone https://github.com/cervemone/x402-payment-gateway.git
cd x402-payment-gateway
pip install -r requirements.txt   # or: npm install
python -m src.main --help
```

## Layout

```
  src/
  handlers/
  jobs/
  storage/
  tests/
  docs/
  scripts/
  configs/
  examples/
  deploy/
  benchmarks/
  abi/
```

## Related

- `stock-token-index` — the registry this repo builds on
- `stock-analyst-agent` — the agent that consumes this data
- `rh-stock-token-sdk` — SDK for Robinhood Chain stock tokens

## License

MIT
