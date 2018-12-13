function [frame] = framing(data, fs, f_duration)
f_size = f_duration * fs;
n = floor(length(data)/f_size);

frame = zeros(n,f_size);
temp = 0;
for i = 1: n
    if temp+f_size <= length(data)
        frame(i,:) = data(temp+1:temp+f_size);
        temp = temp + f_size;
    end
end