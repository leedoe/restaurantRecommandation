#-*- encoding=utf-8 -*-

class Singleton(type):
    # 메타 클래스를 이용한 싱글톤
    # 참고 : http://http://wonjayk.tistory.com/262
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]
