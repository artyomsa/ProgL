# ProgL
containes 5 files. Setup CMakeLists to create chanelsinterpolation.pyd. 
This module has only one method - interploate(list img, list linearfunction). 
Img - special matrix, created from bayer pattern of image. 
It containes only chanel value of pixel(another equale zero), example - SamV.txt. 
Linearfuction containes values for multiplication with nearest neghbors of pixel, 
sum of this multiplications gives one of unknown chanel value, 
example of this matrix - LinearRegression.txt. Test.py uses module, and prints time of work. 
I don't push python module, because it is lots of code. It's working time is 13.72, cpp module time less then 0.4.
