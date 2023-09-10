<p align="center">
  <img src="https://s6.uupload.ir/files/black_amp_white_minimalist_business_logo_knwj.png" alt="Logo">
</p>






## About
Tasker.py is a Python module that helps developers with logging and timing their code. It provides utility functions for package installation and importing, time formatting, and caching, as well as a customizable print function with different code options. The module also includes a t class for configuring timer and filename options, making it easier to log code execution and time tasks

## Installation

To install, download the Tasker.py file and import it into your project folder.
```python
  from Tasker import t
```
**note** : Ensure that your project file and Tasker.py are in the same folder.

## Usage
First, import the Tasker module:
```python
from Tasker import t
```
Now, you can use Tasker in your project.

### t.print
Here are some examples for your reference.
#### **Simple Print:**
```python
t.print(message='hi')
```
![Output](https://s6.uupload.ir/files/capture_mxu.png)

The number 2 is the line number. If you don't provide any code option, the D tag will be used in the output. The MainModule is the name of the function that ran your code.

#### **Print With code:**
```python
t.print(message='error',code=2)
```
![Output](https://s6.uupload.ir/files/capture_2exe.png)

Code 2 is for error outputs. Use this code when you encounter an error.

**note*: Code range is from 0 to 3.
This method prints a formatted message with additional information based on the provided code:

  -0: Start Code, used when starting something
  
  -1: Down Code, used when completing tasks
  
  -2: Error Code, used for showing errors (should be used in exceptions)
  
  -3: Info Code, used for showing information like stdout

#### **Print With optional function name:**
```python
t.print(message='test',function_name='My Function Name')
```
![Output](https://s6.uupload.ir/files/capture_qimg.png)

As you can see, the MainModule changes to **My Function Name**. It's as if your code ran inside a function named "My Function Name".
The function_name parameter can be used to override the automatically detected function name.

### t.config
Currently, there are two configuration options available.

#### **filename**
```python
t.config(filename=True)
t.print(message='test')
```
![Output](https://s6.uupload.ir/files/capture_m4s.png)

Now, the output includes the name of your Python file at the beginning.

#### **timer**
```python
t.config(timer=True)
t.print(message='test')
```
![Output](https://s6.uupload.ir/files/capture_5aq0.png)

With this configuration, you can see the time taken for your code to execute the t.print(s) command.

## Another example
```python
1 from Tasker import t
2 t.config(timer=True)
3
4 def my_func():
5    t.print('start my-func',0)
6    try:
7       some_error = 10/0
8    except Exception as e :
9       t.print(e,2)
10    
11 if __name__ == '__main__':
12     t.print('my code is start',0)
13     my_func()
14     t.print('my code is down',1)
```
### output 

![Output](https://s6.uupload.ir/files/capture_6y3c.png)
