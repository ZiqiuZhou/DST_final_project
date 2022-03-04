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
4. TODO, train model with Test-Task02 and look whether spectrum is meaningful or not ...

