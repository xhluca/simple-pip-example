# simple-pip-example
Simple example showing how to use setup.py

## usage

```
pip install git+https://github.com/xhlulu/simple-pip-example
```

then in python:

```python
# The following were included in setup.py
import simple_pip_module
import simple_extra_module

print(simple_pip_module.add_numbers(1, 5))
# => 6

my_obj = simple_pip_module.SimpleClass(x=10)
print(my_obj.x)
# => 10

print(simple_extra_module.maybe_useful_to_user())
# => "I'm trying to help"

# Let's see where those modules are located
print(simple_pip_module)
print(simple_extra_module)

# If you do this it will fail as it was excluded in setup.py
import simple_hidden_module
```

## Special installs

You can install extra requirements (`extras_require` in setup.py) with bracket:
```
pip install simple-pip-example[dev]
```