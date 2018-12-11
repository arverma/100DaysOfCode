%%
close all;
clc;
clear;
%% ----------Reading Audio Signal (Hindi, contains 10 words; Counting 0 to 9)
[data, fs] = audioread('Voice sample\3.wav');
data = data./max(data); % Normalization
subplot(2,1,1)
plot(data)
%% ------------Framing + Energy---------------------
f_duration = 0.025;
f_size = f_duration * fs;

energy = [];
j = 1;
% With 50% Overlap
for i = f_size/2+1: f_size/2: length(data)
    if(i+f_size < length(data))
        frame = data(i-f_size/2:i+f_size/2); % taking datas inbetween the word "tin": 1000:1000+f_size
        %fprintf('%d \t %d\n',i-f_size/2, i+f_size/2)
        energy(j) = sum(frame.^2);
        j = j + 1;
    end
end
subplot(2,1,2)
plot(energy)
%%