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

# Dans un second temps, ça serait
# interessant de traiter ce type d'influenceur.

# influencer = {
#     "name": ["reda", "thomas"],
#     "mail": ["reda.alaoui@hotmail.com", "thomas.canal@grenoble-inp.org"],
#     "insta_nb_followers": [35, 45],
#     "insta_like_rate": [22, 23],
#     "insta_comment_rate": [0.22, 0.78],
#     "insta_score": [40, 60],
#
#     # Youtube
#     "yt_nb_followers": [231, 456],
#     "yt_nb_views": [23, 56],
#    "yt_score": [32, 65],
#
#     #HypeAudtor
#     "score_hpa": [76, 89],
#
#     "final_score": [45, 65]
# }

# loading results in an xl sheet
final_list = pd.DataFrame(influencer)
xl_result = pd.ExcelWriter(r'results/result_' + datetime.now().strftime("%Y-%d-%m_%H-%M-%S")+'.xlsx')
final_list.to_excel(xl_result, 'Influencers', index=False)
xl_result.save()




