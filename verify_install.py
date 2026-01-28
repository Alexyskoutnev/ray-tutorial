#!/usr/bin/env python
"""Verify Ray RLlib installation."""

import sys


def check_import(module_name: str, package_name: str = None) -> bool:
    """Check if a module can be imported."""
    try:
        module = __import__(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"  [OK] {package_name or module_name}: {version}")
        return True
    except ImportError as e:
        print(f"  [FAIL] {package_name or module_name}: {e}")
        return False


def main():
    print("=" * 50)
    print("Ray RLlib Installation Verification")
    print("=" * 50)

    all_ok = True

    print("\n1. Core packages:")
    all_ok &= check_import("ray")
    all_ok &= check_import("torch")
    all_ok &= check_import("numpy")

    print("\n2. Ray ecosystem:")
    try:
        from ray import rllib
        print("  [OK] ray.rllib")
    except ImportError as e:
        print(f"  [FAIL] ray.rllib: {e}")
        all_ok = False

    try:
        from ray import tune
        print("  [OK] ray.tune")
    except ImportError as e:
        print(f"  [FAIL] ray.tune: {e}")
        all_ok = False

    try:
        from ray import serve
        print("  [OK] ray.serve")
    except ImportError as e:
        print(f"  [FAIL] ray.serve: {e}")
        all_ok = False

    print("\n3. RL environments:")
    all_ok &= check_import("gymnasium")

    print("\n4. Visualization & monitoring:")
    all_ok &= check_import("matplotlib")
    all_ok &= check_import("tensorboard")

    print("\n5. Quick functionality test:")
    try:
        import ray
        import gymnasium as gym
        from ray.rllib.algorithms.ppo import PPOConfig

        ray.init(ignore_reinit_error=True, logging_level="ERROR")

        config = (
            PPOConfig()
            .environment("CartPole-v1")
            .env_runners(num_env_runners=0)
        )

        algo = config.build()
        print("  [OK] PPO algorithm builds successfully")

        algo.stop()
        ray.shutdown()
        print("  [OK] Ray shutdown cleanly")

    except Exception as e:
        print(f"  [FAIL] Functionality test: {e}")
        all_ok = False

    print("\n" + "=" * 50)
    if all_ok:
        print("All checks passed! Environment is ready.")
        print("=" * 50)
        print("\nStart learning:")
        print("  jupyter lab tutorials/01_fundamentals/01_rl_concepts.ipynb")
        return 0
    else:
        print("Some checks failed. Please review errors above.")
        print("=" * 50)
        return 1


if __name__ == "__main__":
    sys.exit(main())
