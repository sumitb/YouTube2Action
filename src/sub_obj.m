% Parameters
psi = 0.3;
rho = 0.7;

% Variable initialization
% vid_id = [];
% object = [];
% subject = [];
% vid_name = [];
% object_id = [];
% subject_id = [];
tuple_data = {};

output_file = '../data/subject_object.mat';
% Load mat file
datapath = '../data/YouTubeOutput/';
category = dir(datapath);

for i = 1: length(category)
    if category(i).name(1) == '.' | category(i).name(1) == '..'
        continue;
    else
	% Load matfile and obtain subject-object tuple
        load(strcat(datapath, category(i).name));
	row = 1;
	hash_data = {};

	% Total no. of rows
        len = size(fdata,1);
        
        for j  = 1: len
            intlen = size(fdata{j, 1}, 1); 
            % intlen = cellfun(@size, pdata, 'uni', false){:}(1, 1);

            for k = 1: intlen
		if isempty(hash_data)
                    hash_data{row, 1} = [fdata{j, 1}(k)];
                    hash_data{row, 2} = 1;			% Object_Count    
                    hash_data{row, 3} = [fdata{j, 2}(k)];
                    hash_data{row, 4} = [fdata{j, 3}(k)];  % Object_score_list
		    row = row + 1;
		    continue;
		elseif ~sum([hash_data{:, 1}] == fdata{j, 1}(k)) 
		    % If it doesn't exists, add
                    hash_data{row, 1} = [fdata{j, 1}(k)];
                    hash_data{row, 2} = 1;			% Object_Count    
                    hash_data{row, 3} = [fdata{j, 2}(k)];
                    hash_data{row, 4} = [fdata{j, 3}(k)];  % Object_score_list
		    % Increment row counter
		    row = row + 1;
		else
		    % else update existing values
		    % obtain index of value
		    index = find([hash_data{:, 1}] == fdata{j, 1}(k));
                    hash_data{index, 2} = hash_data{index, 2} + 1;    
                    hash_data{index, 4} = [hash_data{index, 4}, fdata{j, 3}(k)];    
		end
            end
        end

        %Subject -object distinction 
        %% Assuming a Matlab workspace file with first column having object ids
        %% Second col having the count
        %% Fourth column having an array of the the scores the id has scored 
        for j = 1:size(hash_data, 1)		% Might be same as 'row'
           hash_data{j, 5} = sum(hash_data{j, 4});			% Sum of Object_scores
           hash_data{j, 6} = psi* hash_data{j, 2} + rho* hash_data{j, 5};	% Weighted Pic_score
        end

	[sortedValues, sortIndex] = sort([hash_data{:, 6}], 'descend');  % Sort the values in descending order
	maxIndex = sortIndex(1:2);  %# Get a linear index
	ind = i - 2;		% Decrement i by 2 for 'parent and current dir' 
	tuple_data{ind, 1} = strcat('vid', int2str(ind));	
        tuple_data{ind, 2} = category(i).name(1:end-4);
	% subject_id = [subject_id; hash_data{maxIndex(1), 1}];
        % object_id = [object_id; hash_data{maxIndex(2), 1}];

        tuple_data{ind, 3} = [hash_data{maxIndex(1), 3}];
        tuple_data{ind, 4} = [hash_data{maxIndex(2), 3}];
    end
end

% Save vid subject object to a file
save(output_file,'tuple_data');

