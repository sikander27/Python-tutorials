data = {
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": {
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": [
              "GML",
              "XML"
            ]
          },
          "GlossSee": "markup"
        }
      }
    }
  }
}
out_data = {
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": {
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": [
              "GML",
              "XML"
            ]
          },
          "GlossSee": "markup"
        }
      }
    }
  }
}


res = {}


def flat_dict(data, res, parent="first"):
    for key, value in data.items():
        print(type(value), type(value) is dict)
        if type(value) is dict:
            flat_dict(value, res, key)
        else:
            if not res.get(key):
                res[key] = value
            else:
                res[f"{str(parent)}_{str(key)}"] = value
    return res


# print(flat_dict(out_data, res))

# {'title': 'S', 'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'Standard Generalized Markup Language', 'Acronym': 'SGML', 'Abbrev': 'ISO 8879:1986', 'para': 'A meta-markup language, used to create markup languages such as DocBook.', 'GlossSeeAlso': ['GML', 'XML'], 'GlossSee': 'markup'}

a = {
    "name": "hariom",
    "age": 20
}


def modify(a):
    a.pop('age')


print(a)
# {
#     "name": "hariom",
#     "age": 20
# }
modify(a)
print(a)
# {
#     "name": "hariom",
# }


# Employee ID	Employee Name	Department ID 	Salary
# Q: Second max salary of each department

# SELECT 
