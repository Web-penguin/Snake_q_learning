# AI in videogames project

### Report by snake game project

Author: Artyom Sakhabutdinov, group 145

### Using technologies: ###
  - Python
  - Pygame
  - Tensorflow
  - OpenCV

### Game rules ###

At the beginning of the game, we have a one dot - square 1x1 on the table of 20x20, which located in the center - (10; 10).It's our snake. Also, we spawn an apple on the random postition of the table, which is not marked as our snake. Snake can not bump into walls(but in this version, self collision is allowed). If snake doing something like that forbidden rule, game over have comming. Aim of the game for snake - eat as much apples as possible. And in addition, we have only increasing apples - when snake ate an apple, the length of the snake will increase to 1 square.

### Algorithm ###

I've used Q-learning algorithm with the following rewards: 
 - for bump into wall gives -1
 - for eating an apple gives +1
 - on every step, which didn't lead to result action after 250 non-result actions I give reward = -0.02. 

### Experiments and result ###

The best result I've ever seen was ten apples per one life on epsilon ~0.7, then after this small success, snake started bump into walls and couldn't eat a couple of apples. Also was different experiments with image preprocessing, reward changes, conversion from 4 actions to 5(with doing nothing or move in last direction) and return, but nothing helps to achieve a great success. It is possible, that 2 million steps is small and in some cases snake was untrained.