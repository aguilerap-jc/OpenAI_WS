import gym

#https://gym.openai.com/docs/

def examples(desired_example):
	env = gym.make(desired_example)
	env.reset()
	for i in range(10):
		for _ in range(1000):
			env.render()
			env.step(env.action_space.sample())
		env.reset()
	env.close()

if __name__ == "__main__":
	cart_pole = "CartPole-v0"
	mountain_car = "MountainCar-v0"
	MsPacman = "MsPacman-v0"
	Hopper = "Hopper-v1" 

	#examples(cart_pole)
	#examples(mountain_car)
	examples(MsPacman)
	#examples(Hopper)
