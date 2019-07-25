var 0..1: v1; var 0..1: n_v1;
constraint v1 + n_v1 = 1;

var 0..1: v2; var 0..1: n_v2;
constraint v2 + n_v2 = 1;

var 0..1: v3; var 0..1: n_v3;
constraint v3 + n_v3 = 1;

constraint v1 + v2 + v3 >= 1;
constraint v3 + v2 + v1 >= 1;
constraint v2 + v1 >= 1;
solve satisfy;