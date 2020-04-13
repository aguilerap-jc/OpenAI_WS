import gym

#https://gym.openai.com/docs/

def cart_pole():
    #Start the environment
    env = gym.make("CartPole-v0")
    env.reset()

    #Open a file to save the logs
    f = open("Cart_Pole.txt","a")    

    for i_episode in range(100):

        obs = env.reset()
        for t in range(100):

            env.render()
            action = env.action_space.sample()
            obs,reward, done, info = env.step(action)

            # Write the properties of the simulation on a file
            f.write(str(obs) + " " + str(reward) +" "+ str(done) +" "+ str(info) + "\n")

            if done:
                print("Episode finished after {} timestamp".format(t+1))
                break
 
    env.close()
    f.close()

'''
    Spaces Function: Explains how to the the information of an action_space
    and why it's important to create general functions
    
    This introspection can be helpful to write 
    generic code that works for many different 
    environments. 
    Box and Discrete are the most common Spaces. 
    You can sample from a Space or check that something 
    belongs to it:
'''
def spaces():
    env = gym.make('CartPole-v0')
    '''
    The Discrete space allows a fixed range of non-negative numbers, 
    so in this case valid actions are either 0 or 1
    '''
    print(env.action_space)
    '''
    The Box space represents an n-dimensional box, 
    so valid observations will be an array of 4 numbers. 
    We can also check the Box’s bounds:
    '''

    print(env.observation_space)

if __name__ == "__main__":

    #spaces()
    cart_pole()
