clc;
clear;
close all;

[data,fs] = audioread('Voice sample\3.wav');
length(data) % data length before silence removal
data_r = silence_removal(data, fs);
length(data_r) % data length after silence removal
subplot(2,1,1)
plot(data)
subplot(2,1,2)
plot(data_r)