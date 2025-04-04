%% Lấy dữ liệu từ kết quả mô phỏng
% Giả sử dữ liệu được lưu dưới dạng ma trận
input_data = [out.e,out.e_dot]; % Đầu vào: sai số và đạo hàm sai số
output_data = out.theta;                   % Đầu ra: góc của thanh ngang

% Lưu dữ liệu vào file .mat
save('training_data.mat', 'input_data', 'output_data');
%% Load dữ liệu và huấn luyện
% Load dữ liệu
load('training_data.mat');

% Huấn luyện mạng nơ-ron
N = 10; % Số nơ-ron ẩn
net = newff(input_data', output_data', N, {'tansig', 'purelin'});
net = train(net, input_data', output_data');
% Lưu mô hình mạng neural network dưới dạng đối tượng
save('trainedNN.mat', 'net');
