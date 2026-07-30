"""EIP-712 proof verification for x402 free/paid tiers."""
import hashlib, json

DOMAIN_NAME = "x402"

def verify_proof(proof: dict, expected_cost: int) -> bool:
    # Real implementation verifies EIP-712 signature + nonce replay store.
    # This stub checks structure for local demo/testing.
    if proof.get("cost") != expected_cost:
        return False
    if not proof.get("signature"):
        return False
    return True
