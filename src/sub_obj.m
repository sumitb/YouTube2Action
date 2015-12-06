% Load mat file
datapath = '../data/YouTubeOutput/';
category = dir(datapath);

% keySet =   {'Jan', 'Feb', 'Mar', 'Apr'};
% valueSet = [327.2, 368.2, 197.6, 178.4];
% mapObj = containers.Map(keySet,valueSet)

obj_ids = [];     
obj_label = [];        
obj_scores = [];
obj_count = [];
% obj_score_list = [];
row = 1;
hash_data = {};

for i = 1:length(category)
    if category(i).name(1) == '.'
        continue;
    else
        load(strcat(datapath, category(i).name));

	% Total no. of rows
        len = size(fdata,1);
        
        for j  = 1 : len
            intlen = size(fdata{j, 1}, 1); 
            % intlen = cellfun(@size, pdata, 'uni', false){:}(1, 1);

            for k = 1: intlen
		if isempty(hash_data)
                    hash_data{row, 1} = [fdata{j, 1}(k)];
                    hash_data{row, 2} = [1];			% Object_Count    
                    hash_data{row, 3} = [fdata{j, 2}(k)];
                    hash_data{row, 4} = [fdata{j, 3}(k)];  % Object_score_list
		    row = row + 1;
		    continue;
		elseif ~sum([hash_data{:, 1}] == fdata{j, 1}(k)) 
		    % If it doesn't exists, add
                    hash_data{row, 1} = [fdata{j, 1}(k)];
                    hash_data{row, 2} = [1];			% Object_Count    
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
    end
end
