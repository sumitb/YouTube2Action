% Load subject-object matfile
sub_obj_file = '../data/subject_object.mat';
verb_file = '../data/verb.txt';
sub_ver_obj_file = '../data/result_svo.txt';

load(sub_obj_file);
T1 = readtable(verb_file,'Delimiter',' ','ReadVariableNames',false);

temp = sortrows(T1,[1]);
tuple_data = sortrows(tuple_data,[2]);

% Compare video ids
if ~strcmp(char(tuple_data{:,2}), char(temp.Var1))
    tuple_data = [tuple_data temp.Var2];
    T2 = cell2table(tuple_data,'VariableNames',{'VideoNum','VideoID','Subject','Object','Verb'});
    writetable(T2,sub_ver_obj_file,'Delimiter','\t','WriteVariableNames',false);
end
