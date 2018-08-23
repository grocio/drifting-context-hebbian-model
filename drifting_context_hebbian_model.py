#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# It calculates Cosine Similarity
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# It gives a random vector with the elements being 1 or -1
# e.g., [1,1,-1,1,1,-1,-1,1]
def random_posi_neg_vec(unit_num):
    zero_one_vec = np.random.randint(0,2, unit_num)
    return 1 - 2*zero_one_vec

# It stochastically changes the elements of a vector
# e.g., [1,1,1,-1,-1,-1] -> [-1,1,1,-1,1,-1]
def random_flip(vec, drift_rate):
    target_vec = np.copy(vec)
    unit_num = len(vec)
    change_num = round(unit_num*drift_rate)
    change_index = np.random.choice(unit_num, change_num)
    
    target_vec[change_index] = -1 * target_vec[change_index]

    return target_vec

# It calculates similarity between two vectors and gives a two-deimentional list
def similarity_two_dim_list(two_dim_list):
    vec_num = len(two_dim_list)
    results = np.zeros((vec_num, vec_num))

    for i in range(vec_num):
        for j in range(vec_num):
            results[i][j] = cos_sim(two_dim_list[i], two_dim_list[j])

    return results

# It gives the vectors that represent the drifting context
def context_vecs(position_num, drift_rate, unit_num):
    context_vecs = [0 for i in range(position_num)]
    for i in range(position_num):
        if i == 0:
            context_vecs[i] = random_posi_neg_vec(unit_num)
            # context_vecs[i] = random_flip(random_posi_neg_vec(unit_num), drift_rate)
        else:
            context_vecs[i] = random_flip(context_vecs[i-1], drift_rate)
    return context_vecs

# Simple hebbian rule for encoding
def hebbian_encoding(target_vec, cue_vec, alpha=1.0):
    return alpha*np.outer(target_vec, cue_vec)

# Simple hebbian rule for retrieval
def hebbian_retrieval(W, cue_vec):
    return np.dot(W, cue_vec)

if __name__ == '__main__':
    position_num = 9
    unit_num = 2**12
    run_num = 10

    output_target_cos_sim = np.zeros((position_num, position_num)) 
    context_similarity = np.zeros((position_num, position_num))

    for run in range(run_num):
        position_vecs = context_vecs(position_num, 0.3, unit_num)

        context_similarity += similarity_two_dim_list(position_vecs)

        target_vecs = [random_posi_neg_vec(unit_num) for i in range(position_num)] 
       
        W = np.zeros((unit_num, unit_num))

        # Encoding
        for i in range(position_num):
            W = W + hebbian_encoding(target_vecs[i], position_vecs[i], alpha=1.0)

        output = []

        # Retrieval
        for i in range(position_num):
            output.append(hebbian_retrieval(W, position_vecs[i]))

        for i in range(position_num):
            for j in range(position_num):
                output_target_cos_sim[i][j] += cos_sim(target_vecs[i], output[j])
    
    output_target_cos_sim = output_target_cos_sim / run_num
    context_similarity = context_similarity / run_num

    # The values for accuracy are re-scaled by Luce's choice rule
    for i in range(len(output_target_cos_sim)):
        output_target_cos_sim[i] =  output_target_cos_sim[i] / sum(output_target_cos_sim[i])

    print('Context similarity\n', np.round(context_similarity, 2))
    print('Transposition & Accuracy\n', np.round(output_target_cos_sim, 2))

    """
    # Graph
    x = np.array(range(position_num))

    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10,8), sharex=True, sharey=True)

    axes[0,0].set_xticks(np.array(range(position_num)))
    axes[0,0].set_xlim(-0.5,position_num-1+0.5)
    axes[0,0].set_yticks(np.linspace(0,1,11))
    axes[0,0].set_ylim(-0.05,1.05)

    def subplots_draw(i,j,output_num,title,position_num):
        axes[i,j].plot(x, output_target_cos_sim[output_num], marker='o')
        axes[i,j].set_title(title)

    # They look ugly. Wanna make them beautiful!
    subplots_draw(0,0,0,'position 0',position_num)
    subplots_draw(0,1,1,'position 1',position_num)
    subplots_draw(0,2,2,'position 2',position_num)
    subplots_draw(1,0,3,'position 3',position_num)
    subplots_draw(1,1,4,'position 4',position_num)
    subplots_draw(1,2,5,'position 5',position_num)
    subplots_draw(2,0,6,'position 6',position_num)
    subplots_draw(2,1,7,'position 7',position_num)
    subplots_draw(2,2,8,'position 8',position_num)

    plt.show()
    
    """
    results_diagonal = []
    for i in range(position_num):
        results_diagonal.append(output_target_cos_sim[i][i])

    x = np.array(range(9))
    y = results_diagonal
    plt.plot(x, y, marker='o')
    plt.xticks(np.array(range(position_num)))
    plt.xlim(-0.5,position_num-1+0.5)
    plt.yticks(np.linspace(0,1,11))
    plt.ylim(-0.05,1.05)
    plt.show()
    #"""
