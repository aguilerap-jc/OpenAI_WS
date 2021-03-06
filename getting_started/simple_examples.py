import gym

#https://gym.openai.com/docs/

'''
	examples function:
	Start a specific example with 
	random simulations samples and seeds 
'''
def examples(desired_example):
	env = gym.make(desired_example)
	env.reset()
	for i in range(10):
		for _ in range(1000):
			env.render()
			env.step(env.action_space.sample())
		env.reset()
	env.close()

'''
	cart_pole: Runs a basic example from the OpenAI gym functions
	that shows some of the properties that can be aquired during a simulation.
'''
def cart_pole_example():
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

#Available Environments
#https://gym.openai.com/envs/#classic_control

def gym_registry():
    print(gym.envs.registry.all())

if __name__ == "__main__":
	cart_pole = "CartPole-v0"
	mountain_car = "MountainCar-v0"
	MsPacman = "MsPacman-v0"
	Hopper = "Hopper-v1" 

	examples(cart_pole)
	#cart_pole_example()
	#spaces()
	#gym_registry()