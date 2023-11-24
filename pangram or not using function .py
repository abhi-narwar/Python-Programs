def pangram(phrase):
        letters={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        phrase=set(phrase)
        if phrase>=letters:
            return True
        else:
            return False
print(pangram('abcde'))

    
