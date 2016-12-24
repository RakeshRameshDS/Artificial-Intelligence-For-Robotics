
%Init
t = 0.1;
A = [1 0 t 0; 0 1 0 t; 0 0 1 0; 0 0 0 1]; 

%measurements = [5.,10.;6.,8.;7.,6.;8.,4.;9.,2.;10.,0.];
%initial_xy = [4.,12.];

%measurements = [1,4;6,0;11,-4;16,-8];
%initial_xy = [-4,8];

measurements = [2,17;0,15;2,13;0,11];
initial_xy = [1,19];

x = [initial_xy(1);initial_xy(2);0;0];
P = [0 0 0 0;0 0 0 0; 0 0 1000 0; 0 0 0 1000];
H = [1 0 0 0; 0 1 0 0];
R = [0.1,0;0,0.1];

size_measurement = size(measurements);

for i=1:size_measurement(1)
    %Motion
    x = A*x;
    P = A*P*A';
    %Measurement
    K = P*H'/(H*P*H' + R);
    y = measurements(i,:)';
    x = x + K*(y - H*x)
    P = (eye(4) - K*H)*P

end