fs = 16000;               % sampling frequency (Hz)
nfft = 2^12;              % fft size (number of frequency bins)
K = nfft/2+1;             % length of each filter
M = 23;                   % number of filters

hz2mel = @(hz)(1127*log(1+hz/700)); % Hertz to mel warping function
mel2hz = @(mel)(700*exp(mel/1127)-700); % mel to Hertz warping function

% Design mel filterbank of M filters each K coefficients long,
% filters are uniformly spaced on the mel scale between 0 and Fs/2 Hz
[ H1, freq ] = trifbank( M, K, [0 fs/2], fs, hz2mel, mel2hz );

% Design mel filterbank of M filters each K coefficients long,
% filters are uniformly spaced on the mel scale between 300 and 3750 Hz
[ H2, freq ] = trifbank( M, K, [300 3750], fs, hz2mel, mel2hz );

% Design mel filterbank of 18 filters each K coefficients long, 
% filters are uniformly spaced on the Hertz scale between 4 and 6 kHz
[ H3, freq ] = trifbank( 18, K, [0 8]*1E3, fs, @(h)(h), @(h)(h) );

hfig = figure('Position', [25 100 800 600], 'PaperPositionMode', ...
                  'auto', 'Visible', 'on', 'color', 'w'); hold on; 
subplot( 3,1,1 ); 
plot( freq, H1 );
xlabel( 'Frequency (Hz)' ); ylabel( 'Weight' ); set( gca, 'box', 'off' ); 

subplot( 3,1,2 );
plot( freq, H2 );
xlabel( 'Frequency (Hz)' ); ylabel( 'Weight' ); set( gca, 'box', 'off' ); 

subplot( 3,1,3 ); 
plot( freq, H3 );
xlabel( 'Frequency (Hz)' ); ylabel( 'Weight' ); set( gca, 'box', 'off' );