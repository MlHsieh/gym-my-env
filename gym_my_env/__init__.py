from gym.envs.registration import register

register(
    id='CartPole-v3',
    entry_point='gym_my_env.envs:CartPoleEnv',
    max_episode_steps=200,
    reward_threshold=25.0,
)