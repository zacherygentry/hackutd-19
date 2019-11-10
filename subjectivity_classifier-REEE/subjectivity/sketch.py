# Python Sketch


# input:
# {
#   {
#    index: 0
#     "this is a sentace 1."
#   },
#   {
#     index: 2,
#     "this is a sentace 3."
#   }
# }


def formatParagraph(data):
    size = data["size"]
    opinion = data["opinion"]
    nonOpinion = data["nonOpinion"]





result = {
    "size": 3,
    "opinion": [
        {
            "index": 0,
            "sentance": "this is sentance 1"
        },
        {
            "index": 2,
            "sentance": "this is sentance 3"
        }
    ],
    "nonOpinion": [
        {
            "index": 1,
            "sentance": "this is sentance 2"
        },
    ]
}

# formatParagraph(result)


data = b'{"data":["Fox News Flash top headlines for Nov. 9 are here. Check out what\'s clicking on Foxnews.com","A missing hiker from Huntington Beach, California, was found dead on Thursday at the top of the Darwin glacier in the Inyo National Forest following a nearly weeklong search.","This is me trying to whateer whatever whatever this and that something trying tom ake stuff up.","\\"A good friend of ours tragically lost her husband this week, and she is 37 weeks pregnant with their first baby. We\xe2\x80\x99d like to gather baby and mama essentials for her so she doesn\xe2\x80\x99t have to worry for the first year,\\" a GoFundMe page created for their family\xc2\xa0said.","TOURISTS NEED TO BE CAREFUL TRAVELING TO MEXICO WARNS FATHER OF SLAIN AMERICAN","\\n      The body of 40-year-old Alan Stringer was found around 2:30 p.m. just below Mount Darwin, according to the Inyo County Sheriff\'s Office.\xc2\xa0\\n      (Inyo County Sheriffs Office)","\\"Sequoia and Kings National Park located Alan Stringer deceased at the top of the Darwin Glacier, near the base of the notch to go up Mount Darwin. Sequoia and Kings will be conducting the investigation and recovery,\\" it said.","He was reported missing on Monday evening after going for a\xc2\xa0hike near the Bishop area on Sunday but not returning. Cellphone activity on his phone revealed only one call early in the morning on Sunday before his planned hike.","This is me trying to whateer whatever whatever this and that something trying tom ake stuff up.","Stringer was described as an experienced hiker who loved the outdoors,\xc2\xa0although he didn\'t disclose his hiking plans or routes he was going to take.","ANGEL MOM BLASTS SANCTUARY CITY POLICIES, CALLS FOR CA GOV. GAVIN NEWSOM\'S REMOVAL","\\"He recently purchased an ice\xc2\xa0ax and crampons, and participated in mountaineering training courses. Stringer was equipped for day-hiking only; he had an InReach device that he hiked with, but it was never activated,\\" the Facebook post said.","\\"After checking trailheads throughout the Bishop area, Sheriff\xe2\x80\x99s Deputies located Stringer\xe2\x80\x99s vehicle at North Lake shortly after midnight on Tuesday morning,\\" the post added.","Temperatures dropped well below freezing last week in the high elevation of the trails at North Lake, near where his vehicle was spotted, according to KTLA.","A cause of death has not been released.","CLICK HERE TO GET THE FOX NEWS APP","\\"We are heartbroken, and we just want to help his wife, family, and unborn baby girl,\\" the GoFundMe page said."]}'


import json
my_json = data.decode('utf8')#.replace("'", '"')
# print(my_json)
# print('- ' * 20)

data = json.loads(my_json)
# s = json.dumps(data, indent=4, sort_keys=True)
# print(s)

for sent in data["data"]:
    print(sent)
    print()
