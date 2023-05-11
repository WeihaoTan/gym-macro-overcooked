from gym.envs.registration import register

register(
    id='Overcooked-v1',
    entry_point='gym_macro_overcooked.overcooked_V1:Overcooked_V1',
)

register(
    id='Overcooked-MA-v1',
    entry_point='gym_macro_overcooked.overcooked_MA_V1:Overcooked_MA_V1',
)

register(
    id='Overcooked-LLMA-v1',
    entry_point='gym_macro_overcooked.overcooked_LLMA_V1:Overcooked_LLMA_V1',
)

