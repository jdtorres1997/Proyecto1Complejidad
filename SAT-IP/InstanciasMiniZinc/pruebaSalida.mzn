var 0..1: v1; var 0..1: n_v1;
constraint v1 + n_v1 = 1;

var 0..1: v2; var 0..1: n_v2;
constraint v2 + n_v2 = 1;

var 0..1: v3; var 0..1: n_v3;
constraint v3 + n_v3 = 1;

var 0..1: v4; var 0..1: n_v4;
constraint v4 + n_v4 = 1;

var 0..1: v5; var 0..1: n_v5;
constraint v5 + n_v5 = 1;

var 0..1: v6; var 0..1: n_v6;
constraint v6 + n_v6 = 1;

constraint v1 + n_v2 + v3 >= 1;
constraint v2 + v4 + v5 >= 1;
constraint v4 + v6 >= 1;
solve satisfy;