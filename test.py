import argparse
import gym

from gym_macro_overcooked.macActEnvWrapper import MacEnvWrapper


from PIL import Image
TASKLIST = ["tomato salad", "lettuce salad", "onion salad", "lettuce-tomato salad", "onion-tomato salad", "lettuce-onion salad", "lettuce-onion-tomato salad"]

def play(env_id, grid_dim, task, map_type, n_agent, obs_radius, mode, debug):

    n_agent = 3
    mode = "image"
    map_type = "C"
    grid_dim = [9, 9]
    rewardList = {"subtask finished": 10, "correct delivery": 200, "wrong delivery": -5, "step penalty": -0.1}
    env_params = {'grid_dim': grid_dim,
                    'task': TASKLIST[task],
                    'rewardList': rewardList,
                    'map_type': map_type,
                    'n_agent': n_agent,
                    'obs_radius': obs_radius,
                    'mode': mode,
                    'debug': debug
                }
    env = gym.make(env_id, **env_params)

    if env_id == "Overcooked-v1":
        #               0        1       2        3     4   
        actionName = ["stay", "right", "down", "left", "up"]
    else:
        env = MacEnvWrapper(env)
        if map_type == "A":
            #               0          1              2             3            4               5              6                7             8          9      10       11      12     13
            actionName = ["stay", "get tomato", "get lettuce", "get onion", "get plate 1", "get plate 2", "go to knife 1", "go to knife 2", "deliver", "chop", "right", "down", "left", "up"]
        else:
            #               0          1              2             3            4               5              6                7             8          9           10          11       12      13     14
            actionName = ["stay", "get tomato", "get lettuce", "get onion", "get plate 1", "get plate 2", "go to knife 1", "go to knife 2", "deliver", "chop", "go to counter", "right", "down", "left", "up"]

    rewards = 0
    discount = 1
    step = 0

    obs = env.reset() 
    frame = env.render()    

    im = Image.fromarray(frame)
    #im.show()
    im.save("image/3_agent_" + str(map_type) + "_9.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_id',                 action='store',        type=str,             default='Overcooked-v1',    help='Domain name')
    parser.add_argument('--n_agent',                action='store',        type=int,             default=3,                     help='Number of agents')
    parser.add_argument('--grid_dim',               action='store',        type=int,  nargs=2,   default=[7,7],                 help='Grid world size')
    parser.add_argument('--task',                   action='store',        type=int,             default=6,                     help='The receipt agent cooks')
    parser.add_argument('--map_type',               action='store',        type=str,             default="A",                   help='The type of map')
    parser.add_argument('--obs_radius',             action='store',        type=int,             default=2,                     help='The radius of the agents')
    parser.add_argument('--mode',                   action='store',        type=str,             default="vector",              help='The type of the observation(vector/image)')    
    parser.add_argument('--debug',                  action='store',        type=bool,            default=True,                  help='Whehter print the debug information and render')                
   
    params = vars(parser.parse_args())
    play(**params)



