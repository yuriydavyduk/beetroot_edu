def stop_words(words: list):
    def stop_words_dec(func):
        def wrap(name):
            slogan = func(name)
            for word in words:
                slogan = slogan.replace(word, '*')
            return slogan
        return wrap
    return stop_words_dec


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
