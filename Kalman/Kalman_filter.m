%Init Variables
measurements = [1,2,3];
x = [0;0];
P = [1000 0; 0 1000];
u = [0;0];
F = [1 1; 0 1];
H = [1 0];
R = [1];
I = eye(2);

size_measurement = size(measurements);

for i=1:size_measurement(2)
   
   %Measurement
   y = measurements(i) - H*x;
   S = H*P*H' + R
   K = P*H'*pinv(S);
   x = x + K*y;
   P = (I - K*H)*P;
   
   %Motion
   x = F*x + u
   P = F*P*F'
   
end