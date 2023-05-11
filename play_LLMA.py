import argparse
import gym

from gym_macro_overcooked.macActEnvWrapper import MacEnvWrapper

TASKLIST = ["tomato salad", "lettuce salad", "onion salad", "lettuce-tomato salad", "onion-tomato salad", "lettuce-onion salad", "lettuce-onion-tomato salad"]

def play(env_id, grid_dim, task, map_type, n_agent, obs_radius, mode, debug):

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
        #               0        1       2        3     
        actionName = ["right", "down", "left", "up"]
    else:
        env = MacEnvWrapper(env)
        if map_type == "A":
            #               0          1              2             3            4               5              6                7             8          9     
            actionName = ["stay", "get tomato", "get lettuce", "get onion", "get plate 1", "get plate 2", "go to knife 1", "go to knife 2", "deliver", "chop"]
        else:
            #               0          1              2             3            4               5              6                7             8          9           10     
            actionName = ["stay", "get tomato", "get lettuce", "get onion", "get plate 1", "get plate 2", "go to knife 1", "go to knife 2", "deliver", "chop", "go to counter"]

    rewards = 0
    discount = 1
    step = 0

    obs = env.reset()     
    env.render()

    while(True):
        step += 1
        a = input("input:").split(" ")
        action = [int(a[0])]
        obs, reward, done, info = env.step(action)
        env.render()
        rewards += discount * reward[0]
        discount *= 0.99

        while not info['mac_done'][0]:
            obs, reward, done, info = env.step(action)
            env.render()
            rewards += discount * reward[0]
            discount *= 0.99
        print("------------------------------------------------------------------")
        print("step: ", step, "rewards: ", rewards)
        print("#############################################")
        print("Blue Agent Action: ", actionName[info['cur_mac'][0]])
        print("Action Done: ", info['mac_done'][0])
        print("Blue Agent Observation")
        print("tomato pos: ", obs[0][0:2]*7)
        print("tomato status: ", obs[0][2])
        print("lettuce pos: ", obs[0][3:5]*7)
        print("lettuce status: ", obs[0][5])
        print("onion pos: ", obs[0][6:8]*7)
        print("onion status: ", obs[0][8])            
        print("plate-1 pos: ", obs[0][9:11]*7)
        print("plate-2 pos: ", obs[0][11:13]*7)
        print("knife-1 pos: ", obs[0][13:15]*7)
        print("knife-2 pos: ", obs[0][15:17]*7)
        print("delivery: ", obs[0][17:19]*7)
        print("agent-1: ", obs[0][19:21]*7)
        print("#############################################")
        print("#############################################")
        print("#############################################")
        print("#############################################")
        print()
        print()
        print()


        if done:
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_id',                 action='store',        type=str,             default='Overcooked-LLMA-v1',    help='Domain name')
    parser.add_argument('--n_agent',                action='store',        type=int,             default=1,                     help='Number of agents')
    parser.add_argument('--grid_dim',               action='store',        type=int,  nargs=2,   default=[7,7],                 help='Grid world size')
    parser.add_argument('--task',                   action='store',        type=int,             default=6,                     help='The receipt agent cooks')
    parser.add_argument('--map_type',               action='store',        type=str,             default="A",                   help='The type of map')
    parser.add_argument('--obs_radius',             action='store',        type=int,             default=4,                     help='The radius of the agents')
    parser.add_argument('--mode',                   action='store',        type=str,             default="vector",              help='The type of the observation(vector/image)')    
    parser.add_argument('--debug',                  action='store',        type=bool,            default=False,                  help='Whehter print the debug information and render')                
   
    params = vars(parser.parse_args())
    play(**params)



