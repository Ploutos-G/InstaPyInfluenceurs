from datetime import datetime

import pandas as pd

influencer = {
    "name": ["reda", "thomas"],
    "mail": ["reda.alaoui@hotmail.com", "thomas.canal@grenoble-inp.org"],
    "nb_followers": [35, 45],
    "like_rate": [22, 23],
    "comment_rate": [0.22, 0.78],
    "insta_score": [40, 60]
}

# loading results in an xl sheet
final_list = pd.DataFrame(influencer)
xl_result = pd.ExcelWriter(r'results/result_' + datetime.now().strftime("%Y-%d-%m_%H-%M-%S")+'.xlsx')
final_list.to_excel(xl_result, 'Influencers', index=False)
xl_result.save()




