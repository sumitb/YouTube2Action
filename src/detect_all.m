% It expects img as main folder. img contains different folders for frames
% from each video
    caltechPath = '../data/YouTubeImgs'; % image folder path
    category = dir(caltechPath);
    count_train = 0;
    count_test = 0;
    for i = 1:length(category)
        if category(i).name(1) == '.' 
            continue
        else
            fprintf('processing %s\n', category(i).name);
            % TODO: change image* to corresponding name
            imageFile = dir(fullfile(caltechPath, category(i).name, 'Picture*'));
            len = length(imageFile);

            for j = 1:len
                if imageFile(j).name(1) == '.'
                    continue
                else    
                    
                    fprintf('frame %s\n', imageFile(j).name);
                    
                    im = fullfile(caltechPath,category(i).name, imageFile(j).name);
                    [top_boxes obj_found obj_ids count] = detect10k_demo(rcnn_model, rcnn_feat, im, 'out.jpg');
                    obj_found = obj_found';
%                     vid(1:count) = category(i).name;
%                     frame(1:count) = imageFile(j).name;
%                     vid = vid';
%                     frame = frame';
                    % TODO: save return values from detect10k_demo 
		    % have to maintain DS to save all or append every time
                    % this is for one image only
                    save('test.mat', 'top_boxes','obj_found','obj_ids','-append')                      
               end
            end
        end
    end
