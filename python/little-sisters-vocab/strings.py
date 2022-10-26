"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un"+word

def make_word_groups(vocab_words):
    return (' :: '+ vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word):
    suffix = word.split('ness')[0]
    if suffix[-1] != 'i':
        return suffix
    else:
        return suffix.replace(suffix[-1],'y')


def adjective_to_verb(sentence, index):
    split_sentence = sentence.split()
    if split_sentence[index][-1] == '.':
        return split_sentence[index][:-1] + 'en'
    else:
        return split_sentence[index] + 'en'

#    new_sentence = list(map(lambda x: x.replace(split_sentence[index], verb), split_sentence))
    
#   return ' '.join(new_sentence)


