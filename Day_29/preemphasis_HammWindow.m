clc;
close all;
clear;

[data,fs] = audioread('Voice sample\segment3_1.wav');
fd = 0.025;
frame = fd*fs;
data = data(2000:2000+frame);
preemph = [1 -0.95];

y = filter(preemph, 1, data);
subplot(2,1,1)
plot(data); hold on; plot(y,'r')
subplot(2,1,2)
plot(data); hold on; plot(hamming(length(data))); hold on; plot(hamming(length(data)).*data);