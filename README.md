# DST_final_project
The code is based on the repository: https://github.com/pvlachas/RNN-RC-Chaos. Please refer this repo for code requirements. Please also read the paper "data-driven forecasting of high-dimensional chaotic systems with long-short term memory networks" (also added in the repo) to get familiar with the ideas.

- Update Ziqiu:
1. already embedded PSC.py code into several files and implemented what PSC.py want us to calculate, see commit changes
2. add "smoothing_sigma" and "cutoff" as hyper-parameters when run .bash script
3. besides figures the origin code provides, I add spectrum_compare, see figure "spectrum_comparison_{}.png" (forget to use plt.legend(), so the labels is not visible) and print "POWER SPECTRUM ERROR" for each experiment
4. next step would be continuously fine-tune parameters

- Update Christoph:

1. Task 1 already finished (but could also be made more detailed...)
2. generated notebook (GettingFamiliarWithData.ipynb) to understand test and training data shape and data itself of lorenz data
3. In order to test whether task 2 is finished/works, a sinosoidal time series (test and train) data was generated in /Data/Test-Task02
	- i started to write something about task 02
4. I tried several hyperparameters for training lorenz-63 and lorenz-96:
	- found an acceptable lorenz-63 training using all dimensions and a smaller learning rate (published it)
	- for lorenz-96 dataset using all dimensions is good and also smaller learning rate (one magnitude lower), but the results are still only "meh"

