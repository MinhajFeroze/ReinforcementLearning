# -*- coding: utf-8 -*-
"""Sokoban_v3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xMXvlvplGDCyPN8ziIehFR_nPN_u23Pv
"""

!pip install gym

import gym
from gym import spaces
import numpy as np
from matplotlib import pyplot

class Sokoban(gym.Env):
  metadata = {"render_modes":["human"]}


  # Initialization Function
  #------------------------
  def __init__(self):

    self.state = [
            [5, 5, 5, 5, 5],
            [5, 1, 0, 0, 5], # Agent = 1
            [5, 0, 2, 0, 5], # Box = 2
            [5, 0, 9, 0, 5], # Goal = 9
            [5, 5, 5, 5, 5],
          ]
    
    self.action = [0, 1, 2, 3] # 2 - left, 3 - right, 0 - up, 1 - down 
    self.reward = 0
    self.done = False


  # self.reset Function
  #--------------------
  def reset(self):
    
    self.state = [
            [5, 5, 5, 5, 5],
            [5, 1, 0, 0, 5], # Agent = 1
            [5, 0, 2, 0, 5], # Box = 2
            [5, 0, 9, 0, 5], # Goal = 9
            [5, 5, 5, 5, 5],
          ]
    
    return self.state


  # Step Function
  #--------------
  def step(self, action):
    state = self.state
    new_state = state

    # ACTION = Left (2)
    if action == 2:
      for i in range (len(new_state)):
        for j in range (len(new_state)):
          if(new_state[i][j] == 1):

            # Goal State left of player
            if new_state[i][j-1] == 9:
              new_state[i][j] = 0
              new_state[i][j-1] = 1
              reward = 10
              self.done = True
              break

            # Empty space left of the player
            if new_state[i][j-1] == 0:
              new_state[i][j] = 0
              new_state[i][j-1] = 1
              self.reward = -1
              break

            # Wall left of the player
            elif new_state[i][j-1] == 5:
              self.reward = -5
              break

            # Box left of player
            elif new_state[i][j-1] == 2:
              # Empty space left of box
              if new_state[i][j-2] == 0:
                new_state[i][j-2] = 2
                new_state[i][j-1] = 1
                new_state[i][j] = 0
                self.reward = -0.5
                break
              
              # Wall left of box
              elif new_state[i][j-2] == 5:
                self.reward = -10
                self.reset()              
                self.done = True
                break

              # Goal State left of box
              elif new_state[i][j-2] == 9:
                new_state[i][j-2] = 5
                new_state[i][j-1] = 1
                new_state[i][j] = 0
                self.reward = 10
                self.done = True
                break

      return new_state, self.reward, self.done

    
    # ACTION = Right (3)
    elif action == 3:
      for i in range (len(new_state)):
        for j in range (len(new_state)):
          if(new_state[i][j] == 1): #checking agent

            # Goal State right of player
            if new_state[i][j+1] == 9:
              new_state[i][j] = 0
              new_state[i][j+1] = 1
              reward = 10
              self.done = True
              break

            # Empty space right of player
            if new_state[i][j+1] == 0:
              new_state[i][j] = 0
              new_state[i][j+1] = 1
              self.reward = -1

            # Wall right of player
            elif new_state[i][j+1] == 5:
              self.reward = -5

            # Box right of player
            elif new_state[i][j+1] == 2:
              print("coordinate",i,j) # -------------------PRINTING COORDINATE
              # Empty space right of box
              if new_state[i][j+2] == 0:
                print(i,j)
                new_state[i][j+2] = 2
                new_state[i][j+1] = 1
                new_state[i][j] = 0
                self.reward = -0.5
              
              # Wall right of box
              elif new_state[i][j+2] == 5:
                self.reward = -10
                self.reset()              
                self.done = True

              # Goal State right of box
              elif new_state[i][j+2] == 9:
                new_state[i][j+2] = 5
                new_state[i][j+1] = 1
                new_state[i][j] = 0
                self.reward = 10
                self.done = True
      
      return new_state, self.reward, self.done

    # ACTION = Up (0)
    elif action == 0:
      for i in range (len(new_state)):
        for j in range (len(new_state)):
          if(new_state[i][j] == 1):

            # Goal State above player
            if new_state[i-1][j] == 9:
              new_state[i][j] = 0
              new_state[i-1][j] = 1
              new_reward = 10
              self.done = True
              break

            # Empty space above player
            if new_state[i-1][j] == 0:
              new_state[i][j] = 0
              new_state[i-1][j] = 1
              self.reward = -1

            # Wall above player
            elif new_state[i-1][j] == 5:
              self.reward = -5

            # Box above player
            elif new_state[i-1][j] == 2:
              # Empty space above box
              if new_state[i-2][j] == 0:
                new_state[i-2][j] = 2
                new_state[i-1][j] = 1
                new_state[i][j] = 0
                self.reward = -0.5
              
              # Wall above box
              elif new_state[i-2][j] == 5:
                self.reward = -10
                self.reset()              
                self.done = True

              # Goal State above box
              elif new_state[i-2][j] == 9:
                new_state[i-2][j] = 5
                new_state[i-1][j] = 1
                new_state[i][j] = 0
                self.reward = 10
                print("Goal Reached!")
                self.done = True
      
      return new_state, self.reward, self.done

    # ACTION = Down (1)
    elif action == 1:
      for i in range (len(new_state)):
        for j in range (len(new_state)):
          if(new_state[i][j] == 1):

            # Goal State right of player
            if new_state[i+1][j] == 9:
              new_state[i][j] = 0
              new_state[i+1][j] = 1
              reward = 10
              self.done = True
              break

            # Empty space below player
            if new_state[i+1][j] == 0:
              new_state[i][j] = 0
              new_state[i+1][j] = 1
              self.reward = -1

            # Wall below player
            elif new_state[i+1][j] == 5:
              self.reward = -5

            # Box below player
            elif new_state[i+1][j] == 2:
              # Empty space below box
              if new_state[i+2][j] == 0:
                new_state[i+2][j] = 2
                new_state[i+1][j] = 1
                new_state[i][j] = 0
                self.reward = -0.5
              
              # Wall below box
              elif new_state[i+2][j] == 5:
                self.reward = -10
                self.reset()              
                self.done = True

              # Goal State below box
              elif new_state[i+2][j] == 9:
                new_state[i+2][j] = 5
                new_state[i+1][j] = 1
                new_state[i][j] = 0
                self.reward = 10
                print("Goal Reached!")
                self.done = True
      
      return new_state, self.reward, self.done
# temp = Sokoban()
# temp.step(3)
# temp.step(1)

#def sarsa_on_policyTD(self, alpha, eps, T, E):
   # for episode in (E):
    #  state = env.reset()
     # action = eps_greedy()

def sarsa(env, alpha, eps, E):
    w = np.zeros(4)
    y = []
    z = []
    for i in range(E):
      
      state = env.reset()
      action = eps_greedy(env, state, w, eps)
      
      print("Episode: ",i)

      done = False
      while not done:
        s_p, r, status = env.step(action)
        # print(status)
        if status == True:
          w += alpha*(r - q_hat(state, action, w)) * x_s_a(state, action) # Gradient x_s_a
          done = True
          state = env.reset()
          env.status = False
          
        else:
          a_p = eps_greedy(env, s_p, w, eps)
          w += alpha*(r + 0.9 * q_hat(s_p, a_p, w) - q_hat(state, action ,w)) * x_s_a(state, action)
          print("episode-",i)
          action = a_p
          state = s_p
      z.append(i)

      x = []
      for i in range(len(env.action)):
        x.append(q_hat(env.state, i, w))
      y.append(np.max(x))
    pyplot.plot(z,y)
    pyplot.show
    return

    # return state,action             
def q_hat(state, action, w):
    return np.dot(w, x_s_a(state, action))

def x_s_a(state, a):
    x = 0
    y = 0

    for i in range(len(state)):
      for j in range(len(state)):
        if state[i][j] == 1:
          x = i
          y = j
        else:
          pass

    feature_vector = [1, x, y, x + y] 
    
    return np.array(feature_vector)

def eps_greedy(env, state, w, eps):
    r =  np.random.random()
    if r > eps:
      max_a = 0
      max_a_v = 0
      for a in range(0,4):
        v = q_hat(state, a, w)
        max_a = a
        max_a_v = v
      return max_a
    else:
      return np.random.randint(0,4)



temp = Sokoban()
final = sarsa(temp, 0.01, 0.8, 1000)

