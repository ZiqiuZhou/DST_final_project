#!/bin/bash

cd ../../../Methods

for RDIM in 1
do
for SS in 100
do
for SL in 8
do
for KP in 1.0
do
python3.7 RUN.py rnn_statefull \
--mode all \
--display_output 1 \
--system_name Lorenz-63 \
--write_to_log 1 \
--N 100000 \
--N_used 50000 \
--RDIM $RDIM \
--noise_level 1 \
--rnn_cell_type lstm \
--unitary_cplex 1 \
--unitary_capacity 2 \
--regularization 0.0 \
--scaler standard \
--initializer xavier \
--sequence_length $SL \
--dropout_keep_prob $KP \
--zoneout_keep_prob $KP \
--hidden_state_propagation_length 300 \
--prediction_length 4 \
--rnn_activation_str tanh \
--rnn_num_layers 1 \
--rnn_size_layers $SS \
--subsample 1 \
--batch_size 32 \
--max_epochs 100 \
--num_rounds 3 \
--overfitting_patience 20 \
--training_min_epochs 1 \
--learning_rate 0.001 \
--train_val_ratio 0.8 \
--iterative_prediction_length 200 \
--num_test_ICS 2 \
--reference_train_time 1 \
--buffer_train_time 0.2 \
--retrain 0 \
--smoothing_sigma 1 \
--frequency_cutoff 5000 # in 1/length
done
done
done
done



