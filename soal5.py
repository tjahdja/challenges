def kevin(words):
    vowels = 'AIEOU'
    jums =sorted(words[i:j] for i, x in enumerate(words) for j in range(i + 1, len(words) + 1) if x in vowels)
    print(jums)
    return len(jums)
def stuart(words):
    vowels = 'AIEOU'
    jums =sorted(words[i:j] for i, x in enumerate(words) for j in range(i + 1, len(words) + 1) if x not in vowels)
    print(jums)
    return(len(jums))

def main(obj):
    if stuart(obj) > kevin (obj):
        return 'stuart menang'
    elif stuart(obj) == kevin (obj):
        return 'seri'
    else:
        return 'kevin menang'

print(main('DINGDINGDONGDINGTALK'))