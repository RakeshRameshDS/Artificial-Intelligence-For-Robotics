% Init
measurements = [1,2,3];
x = [0;0];
P = [1000 0; 0 1000]; %Initial Covariance
A = [1 1; 0 1];
H = [1 0];
C = [1 0; 0 1];
R = [1];

size_measurement = size(measurements);

for i=1:size_measurement(2)
   
   K = P*H'/(H*P*H' + R);
   y = measurements(i) - H*x
   x = x + K*y;
   P = (eye(2)-K*H)*P;
    
   x =  A*x
   P = A*P*A'
   
end