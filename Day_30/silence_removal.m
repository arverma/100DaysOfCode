function [data_r] = silence_removal(data, fs)

data = data / abs(max(data));

f_d = 0.025;
frames = framing(data, fs, f_d);% it is like 0% overlap with rectangular window

% Short term autocorrelation and taking 1 coeff. value i.e. at lag 1 
r = size(frames);
stac = zeros(1,r(2));

for k = 1:r(1)
t = frames(k,:);
ac = zeros(1, length(t));
for i = 0:length(t)-1
    sum1 = 0;
    for j = 1:length(t)-i
        s = t(j)*t(j+i);
        sum1 = sum1 + s;
    end
    ac(i+1) = sum1;
end
% temp(k) = ac(1);
stac(k) = ac(2); % taking second coeff. built in function gives normalized
% autocorrelation (it is autocorr at lag 1)
end

% short term auto corr. (stac)
stac = stac./max(stac); %normalize the data

f_size = round(f_d * fs);
stac_wave = 0;
for j = 1 : length(stac)
    l = length(stac_wave);
    stac_wave(l : l + f_size) = stac(j);
end

fr_ws = frames(stac >= 1e-4,:); % frames without silence
data_r = reshape(fr_ws',1,[]);
