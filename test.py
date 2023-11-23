# from openai import OpenAI
# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-1106",
#     response_format={ "type": "json_object" },
#     messages=[
#         {
#             "role": "system", 
#             "content": "You are a creative assistant skilled in generating character descriptions \
#                         and outputting it in JSON format."
#         },
#         {
#             "role": "user", 
#             "content": "I'm a writer working on a new novel. \
#                         I need a unique name and a one-paragraph description (<100 words) for a character. \
#                         Their occupation is '" + str("doctor") + "'. \
#                         Please create this for me."
#         }
#     ]
# )
# main_message_output = response.choices[0].message.content
# print(main_message_output)
import heapq
from collections import Counter, defaultdict
from itertools import chain

# top_adj_pos = defaultdict(list)
# regions = ["India", "China", "America", "France", "UK", "Brazil", "Russia", "Canada", "Nigeria", "Colombia", "Egypt", "Iran", "Australia"]

# def func(reigon):
#     pos =  {'India': ['resilient', 'compassionate', 'resourceful', 'resilient', 'adaptable', 'compassionate'], 'China': ['resilient', 'resourceful', 'adaptable', 'resilient', 'respectful', 'diligent'], 'America': ['patriotic', 'ambitious', 'optimistic', 'patriotic', 'adventurous', 'optimistic'], 'France': ['romantic', 'cultured', 'sophisticated', 'romantic', 'sophisticated', 'passionate'], 'UK': ['patriotic', 'adventurous', 'polite', 'adventurous', 'warm-hearted', 'charming'], 'Brazil': ['vibrant', 'passionate', 'adventurous', 'warm', 'lively', 'passionate', 'vibrant', 'charismatic'], 'Russia': ['resilient', 'creative', 'adventurous', 'resilient', 'adventurous', 'resourceful'], 'Canada': ['outgoing', 'adventurous', 'resilient', 'adaptable', 'outdoorsy', 'welcoming'], 'Nigeria': ['resilient', 'enterprising', 'vibrant', 'resilient', 'vibrant', 'adaptable'], 'Colombia': ['passionate', 'resilient', 'hospitable', 'passionate', 'resourceful', 'resilient'], 'Egypt': ['resilient', 'adventurous', 'charismatic', 'proud', 'resourceful', 'determined'], 'Iran': ['resilient', 'courageous', 'hospitable', 'resilient', 'hospitable', 'passionate'], 'Australia': ['outgoing', 'adventurous', 'resilient', 'adventurous', 'laid-back', 'outgoing']}
#     neg = {'India': ['reserved', 'stubborn', 'overwhelmed', 'strained'], 'China': ['reserved', 'cautious', 'conforming', 'reserved'], 'America': ['materialistic', 'conformist', 'naive', 'materialistic'], 'France': ['aloof', 'pretentious', 'temperamental', 'pretentious'], 'UK': ['reserved', 'cautious', 'reserved', 'stubborn'], 'Brazil': ['volatile', 'impulsive', 'chaotic', 'reckless', 'overwhelming', 'impulsive', 'temperamental'], 'Russia': ['guarded', 'stubborn', 'guarded', 'stoic'], 'Canada': ['guarded', 'reserved', 'reserved', 'conformist'], 'Nigeria': ['chaotic', 'struggling', 'oppressed', 'marginalized'], 'Colombia': ['guarded', 'cautious', 'guarded', 'suspicious'], 'Egypt': ['guarded', 'stubborn', 'guarded', 'reserved'], 'Iran': ['overlooked', 'misunderstood', 'oppressed', 'misunderstood'], 'Australia': ['reckless', 'stubborn', 'reckless', 'carefree']}

#     pos_r = pos[reigon]

#     pos_c = Counter(pos_r)
#     freq_list = [(x, pos_c[x])  for x in pos_r] 
#     freq_list = list(set(freq_list))
#     heapq.heapify(freq_list)
#     for _ in range(3):
#         adj, cnt = heapq.heappop(freq_list)
#         top_adj_pos[reigon] += (adj, cnt*100/len(pos_r))


# for reigon in regions:
#     func(reigon)
# print(top_adj_pos)

# flat_pos = list(chain.from_iterable(pos['India']))
# flat_neg = list(chain.from_iterable(neg))
# print(pos_r)

top_adjectives_pos = {'India': ['adaptable', 11.11111111111111, 'adventurous', 22.22222222222222, 'compassionate', 11.11111111111111], 'China': ['adaptable', 20.0, 'cultural', 10.0, 'humble', 10.0], 'America': ['adventurous', 11.11111111111111, 'ambitious', 33.333333333333336, 'enterprising', 11.11111111111111], 'France': ['charming', 11.11111111111111, 'cultured', 33.333333333333336, 'passionate', 11.11111111111111], 'UK': ['charming', 33.333333333333336, 'resilient', 33.333333333333336, 'resourceful', 11.11111111111111], 'Brazil': ['adventurous', 11.11111111111111, 'outgoing', 11.11111111111111, 'passionate', 33.333333333333336], 'Russia': ['adventurous', 11.11111111111111, 'determined', 11.11111111111111, 'inquisitive', 11.11111111111111], 'Canada': ['adventurous', 22.22222222222222, 'friendly', 33.333333333333336, 'open-minded', 11.11111111111111], 'Nigeria': ['Hospitable', 11.11111111111111, 'Resilient', 11.11111111111111, 'Spiritual', 11.11111111111111], 'Colombia': ['adventurous', 11.11111111111111, 'hospitable', 11.11111111111111, 'passionate', 33.333333333333336], 'Egypt': ['adaptable', 11.11111111111111, 'adventurous', 11.11111111111111, 'curious', 11.11111111111111], 'Iran': ['creative', 11.11111111111111, 'cultural', 11.11111111111111, 'hospitable', 33.333333333333336], 'Australia': ['adventurous', 33.333333333333336, 'laid-back', 22.22222222222222, 'outdoorsy', 11.11111111111111]}
region = "India"
top_pos = top_adjectives_pos[region]

print(top_pos)


