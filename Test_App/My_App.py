# import test_pkg.mod1
# import test_pkg.mod2

# test_pkg.mod1.foo()
# x = test_pkg.mod2.bar()
# x

# from test_pkg.mod1 import foo
# foo()

# import test_pkg
# print(test_pkg.var_init)
# from test_pkg import mod1
# mod1.foo()

import test_pkg
test_pkg.mod1.foo()
test_pkg.mod2.bar()
