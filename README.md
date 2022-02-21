# DST_final_project
The code is based on the repository: https://github.com/pvlachas/RNN-RC-Chaos. Please refer this repo for code requirements. Please also read the paper "data-driven forecasting of high-dimensional chaotic systems with long-short term memory networks" (also added in the repo) to get familiar with the ideas.

- Update 21.02 by Ziqiu:
1. I use LSTM as our model and the code works with the requirement of python 3.7 and tensorflow 1.14
2. I implemented part of task 03 using two given datasets: for example, if you want to train a model on data Lorenz-63, go to the folder ./Experiments/Lorenz-63/Local and command: bash 03_RNNStatefull_LSTM.sh
3. Two models of task03 still need to be fine-tune, especially for Lorenz-96 model
4. not be able to find satisfying values for the power spectrum smoothing factor and
the cutoff
