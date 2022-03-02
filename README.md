# simple-pip-example
Simple example showing how to use setup.py

## usage

```
pip install git+https://github.com/xhlulu/simple-pip-example
```

then in python:

```python
import simple_pip_library

print(simple_pip_library.add_numbers(1, 5))
# => 6

my_obj = simple_pip_library.SimpleClass(x=10)
print(my_obj.x)
# => 10