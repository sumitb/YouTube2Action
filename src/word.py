from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
nltk.data.path.append('./nltk_data/')


def binary_eval(subj, verb, obj):
    sucs_subj = 0
    sucs_verb = 0
    sucs_obj = 0
    
    with open('ground_truth_most_common_Triplet.txt') as f:
        for i, line in enumerate(f):
            line = line.split('|')
            subj_g = line[0].split(' ')[1].strip()
            verb_g = line[1].strip()
            obj_g = line[2].strip()

            # Swap subject and object, if cond arise
            if subj_g == obj[i] or obj_g == subj[i] and subj_g != obj_g:
                subj[i], obj[i] = obj[i], subj[i]
            if subj_g == subj[i]:
                sucs_subj += 1
            if verb_g == verb[i]:
                sucs_verb += 1
            if obj_g == obj[i]:
                sucs_obj += 1

    print 'Binary Approach rate: ', 100*(sucs_subj/len(subj)), 100*(sucs_verb/len(verb)), 100*(sucs_obj/len(obj)) 


def wup_eval(subj, verb, obj):
    sucs_subj = 0
    sucs_verb = 0
    sucs_obj = 0
    
    with open('ground_truth_most_common_Triplet.txt') as f:
        for i, line in enumerate(f):
            line = line.split('|')
            subj_g = line[0].split(' ')[1].strip()
            verb_g = line[1].strip()
            obj_g = line[2].strip()

            # Swap subject and object, if cond arise
            if subj_g == obj[i] or obj_g == subj[i] and subj_g != obj_g:
                subj[i], obj[i] = obj[i], subj[i]
            if subj_g == subj[i]:
                sucs_subj += 1
            if verb_g == verb[i]:
                sucs_verb += 1
            if obj_g == obj[i]:
                sucs_obj += 1

    print 'WPU Approach rate: ', 100*(sucs_subj/len(subj)), 100*(sucs_verb/len(verb)), 100*(sucs_obj/len(obj)) 


def process_subj(subj, flag):
    if flag == 1:
        with open('youtube_setof_subjects.txt') as f:
            subj_dict = f.read()
        subj_dict = subj_dict.split('\n')
    elif flag == 2:
        with open('youtube_setof_objects.txt') as f:
            obj_dict = f.read()
        subj_dict = obj_dict.split('\n')
    
    max_score = 0
    finl_subj = (subj, '<>')
    subj_list = subj.split(',')

    if len(subj_list) == 1:
        return subj
    for prob_subj in subj_list:
        prob_subj = prob_subj.strip()
        if wn.synsets(prob_subj):
            try:
                v1 = wn.synset(prob_subj + '.n.01')
                for yout_subj in subj_dict:
                    if yout_subj != '':
                        v2 = wn.synset(yout_subj + '.n.01')
                        score = v1.wup_similarity(v2)
                        if score > max_score:
                            finl_subj = (prob_subj, yout_subj)
                            max_score = score
            except:
                finl_subj = (prob_subj, '<>')
                pass
                
    # print finl_verb, max_score
    return (finl_subj[1])


def process_verb(verb):
    verb = verb[:-1] # Remove newline char
    with open('youtube_setof_verbs.txt') as f:
        verb_dict = f.read()
    verb_dict = verb_dict.split('\n')
    
    max_score = 0
    finl_verb = (verb, '<>')
    verb_list = re.findall('[A-Z][^A-Z]*', verb)
    
    for prob_verb in verb_list:
        if prob_verb[len(prob_verb)-3:] == 'ing':
            prob_verb = prob_verb[:-3] # Remove 'ing' from verb
            if prob_verb.lower() == 'cutt':
                prob_verb = 'cut'
        if wn.synsets(prob_verb):
            try:
                v1 = wn.synset(prob_verb + '.v.01')
                for yout_verb in verb_dict:
                    if yout_verb != '':
                        # if wn.synsets(yout_verb):
                        v2 = wn.synset(yout_verb + '.v.01')
                        score = v1.wup_similarity(v2)
                        if score > max_score:
                            finl_verb = (prob_verb, yout_verb)
                            max_score = score
            except:
                finl_verb = (prob_verb, '<>')
                pass
                
    # print finl_verb, max_score
    return finl_verb[1]


def main():
    subj = []
    obj = []
    subj_m = []
    obj_m = []
    verb = []

    with open('result_svo.txt') as f, open('final_svo.txt', 'w') as fw: 
        for i,line in enumerate(f):
            line = line.split('\t')
            subj.append(line[2])
            obj.append(line[3])
            verb.append(process_verb(line[4]))
            subj_m.append(process_subj(line[2], 1))
            obj_m.append(process_subj(line[3], 2))
            fw.write(line[0]+'\t'+subj_m[i]+'\t'+verb[i]+'\t'+obj_m[i]+'\n')
    binary_eval(subj, verb, obj)
    wup_eval(subj_m, verb, obj_m)

if __name__ == "__main__":
    # Process results
    main()
