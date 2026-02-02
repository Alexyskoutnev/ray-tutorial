# Ray & RLlib Tutorial Series

A hands-on journey from Ray fundamentals to training a robot to walk.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            LEARNING PATH                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  00 Ray Core   01 RL Theory   02 RLlib    03 Envs   04-08 Production        │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐  ┌──────┐  ┌─────────────┐         │
│  │ Tasks   │   │ MDPs    │   │ PPO     │  │Custom│  │ Workflows   │         │
│  │ Actors  │-->│ DQN     │-->│ SAC     │->│ Gyms │->│ Distributed │         │
│  │ Objects │   │ Policy  │   │ A2C     │  │      │  │ Tune, Serve │         │
│  └─────────┘   └─────────┘   └─────────┘  └──────┘  └─────────────┘         │
│       │                                                    │                │
│       └────────────────────────────────────────────────────┘                │
│                                   │                                         │
│                                   v                                         │
│                         ┌─────────────────┐                                 │
│                         │  09 ROBOTICS    │                                 │
│                         │                 │                                 │
│                         │  Train a robot  │                                 │
│                         │  to walk!       │                                 │
│                         └─────────────────┘                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Module Overview

| Module | Topic | What You'll Learn |
|--------|-------|-------------------|
| **00** | [Ray Core](./tutorials/00_ray_core/) | Tasks, Actors, Object Store - the foundations |
| **01** | [RL Fundamentals](./tutorials/01_rl_fundamentals/) | MDPs, Q-learning, DQN, Policy Gradients |
| **02** | [RLlib Basics](./tutorials/02_rllib_basics/) | PPO, SAC, DQN - when to use what |
| **03** | [Custom Environments](./tutorials/03_custom_environments/) | Build your own Gymnasium environments |
| **04** | [Training Workflows](./tutorials/04_training_workflows/) | End-to-end training pipelines |
| **05** | [Distributed Training](./tutorials/05_distributed_training/) | Scale to multiple GPUs and nodes |
| **06** | [Hyperparameter Tuning](./tutorials/06_hyperparameter_tuning/) | Ray Tune for optimization |
| **07** | [Production Deployment](./tutorials/07_production_deployment/) | Ray Serve for model serving |
| **08** | [Industry Patterns](./tutorials/08_industry_patterns/) | Best practices & production tips |
| **09** | [Robotics Capstone](./tutorials/09_robotics_capstone/) | Train an Ant robot to walk with PPO |

## Quick Start

```bash
# 1. Create environment and install dependencies
uv sync

# 2. For robotics (Module 09)
uv pip install mujoco gymnasium[mujoco]

# 3. Start with Ray Core
uv run jupyter notebook tutorials/00_ray_core/01_ray_core_fundamentals.ipynb
```

## Recommended Learning Paths

```
For beginners (no RL experience):
  00 -> 01 -> 02 -> 03 -> 09

For ML practitioners (know RL basics):
  00 -> 02 -> 03 -> 05 -> 06 -> 09

For production engineers:
  00 -> 05 -> 06 -> 07 -> 08
```

## Prerequisites

- Python 3.9+
- Basic Python knowledge
- Some familiarity with NumPy
- No RL experience required (we start from scratch!)

## Key Concepts Covered

- **Ray Core**: Tasks, Actors, Object Store, distributed computing
- **Reinforcement Learning**: MDPs, value functions, policy optimization
- **Deep RL Algorithms**: DQN, PPO, SAC, A2C, IMPALA
- **Ray Ecosystem**: Ray Core, RLlib, Tune, Serve
- **Production Patterns**: Safety, monitoring, A/B testing
- **Industry Best Practices**: Reproducibility, versioning, deployment

## The Finale: Robot Locomotion

By the end, you'll train this:

```
                    ┌───┐
                   /│   │\
                  / │   │ \
                 /  └───┘  \
                /     │     \
             ──┘      │      └──
            /         │         \
           /          │          \
       ───┘           │           └───

      MuJoCo Ant: 4 legs, 8 joints, learns to walk!
```

## Resources

- [Ray Documentation](https://docs.ray.io/)
- [RLlib Documentation](https://docs.ray.io/en/latest/rllib/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [MuJoCo Documentation](https://mujoco.readthedocs.io/)

## License

MIT License - Feel free to use for learning and teaching.
