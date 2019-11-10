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

    result = [202]

    result[20] = "dog"

    print(result)




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

formatParagraph(result)