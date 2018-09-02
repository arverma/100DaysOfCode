function test_double = gamma_c(test,g)
  test_double = im2double(test);
  test_double = (test_double).^g;
end