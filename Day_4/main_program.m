clc;
%clear;
close all;


%Read Image
test = imread('logo.png');

subplot(3,5,1)
imshow(test);

%Red Image
subplot(3,5,2)
imshow(test(:,:,1));
title('Red');

%Green Image
subplot(3,5,3)
imshow(test(:,:,2));
title('Green');

%Blue Image
subplot(3,5,4)
imshow(test(:,:,3));
title('Blue');

%Image without Blue
subplot(3,5,5)
test_noblue = test;
test_noblue(:,:,3) = 0; 
imshow(test_noblue);
title('-Blue');

%Image without Green
subplot(3,5,6)
test_nogreen = test;
test_nogreen(:,:,2) = 0; 
imshow(test_nogreen);
title('-Green');

%Image without Red
subplot(3,5,7)
test_nored = test;
test_nored(:,:,1) = 0; 
imshow(test_nored);
title('-Red');

%Image without Blue and Green
subplot(3,5,8)
test_nobg = test;
test_nobg(:,:,2:3) = 0; 
imshow(test_nobg);
title('-(Blue + Green)');

%Image without Blue and Red
subplot(3,5,9)
test_nobr = test;
test_nobr(:,:,[1,3]) = 0; 
imshow(test_nobr);
title('-(Blue + Red)');

%Image without Red and Green
subplot(3,5,10)
test_norg = test;
test_norg(:,:,1:2) = 0; 
imshow(test_norg);
title('-(Red + Green)');


%Gamma Correction function written in different file

%gamma = 0.8
subplot(3,5,11)
temp = gamma_c(test,0.8);
imshow(temp);
title('gamma = 0.8');

clear temp;

%gamma = 0.6
subplot(3,5,12)
temp = gamma_c(test,0.6);
imshow(temp);
title('gamma = 0.6');

%gamma = 0.4
subplot(3,5,13)
temp = gamma_c(test,0.4);
imshow(temp);
title('gamma = 0.4');

%gamma = 0.2
subplot(3,5,14)
temp = gamma_c(test,0.2);
imshow(temp);
title('gamma = 0.2');

%gamma = 0.00000009
subplot(3,5,15)
temp = gamma_c(test,0.0000009);
imshow(temp);
title('gamma = 0.0000009');
